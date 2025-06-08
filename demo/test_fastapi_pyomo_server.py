from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pyomo.environ import *
import math
import json

# Blog: https://blog.csdn.net/fengbingchun/article/details/148513653

def parse_json(data):
	model = ConcreteModel()

	model.F = Set(initialize=data['sets']['F'])
	model.N = Set(initialize=data['sets']['N'])

	model.c = Param(model.F, initialize=data['params']['c'], within=PositiveReals)
	def parse_a(model, food, nutr):
		return data['params']['a'][food][nutr]
	model.a = Param(model.F, model.N, initialize=parse_a, within=NonNegativeReals)
	model.V = Param(model.F, initialize=data['params']['V'], within=PositiveReals)
	model.Nmin = Param(model.N, initialize=data['params']['Nmin'], within=NonNegativeReals, default=0.0)
	def parse_Nmax(model, nutr):
		val = data['params']['Nmax'][nutr]
		return val if val != "inf" else math.inf
	model.Nmax = Param(model.N, initialize=parse_Nmax, within=NonNegativeReals)
	model.Vmax = Param(initialize=data['params']['Vmax'], within=PositiveReals)

	return model

def linear_programming(data):
	model = parse_json(data)

	model.x = Var(model.F, within=NonNegativeIntegers)
	model.y = Var(model.F, within=Binary)

	model.cost = Objective(expr=sum(model.c[i]*model.x[i] for i in model.F), sense=minimize)

	def nutrient_rule(model, j):
		value = sum(model.a[i,j]*model.x[i] for i in model.F)
		return inequality(model.Nmin[j], value, model.Nmax[j])
	model.nutrient_limit = Constraint(model.N, rule=nutrient_rule)

	def volume_rule(model):
		return sum(model.V[i]*model.x[i] for i in model.F) <= model.Vmax
	model.volume = Constraint(rule=volume_rule)

	def select_rule(model):
		return sum(model.y[i] for i in model.F) == data['number']
	model.select = Constraint(rule=select_rule)

	def linking_upper_rule(model, f):
		return model.x[f] <= model.y[f] * 1e6
	model.linking_upper = Constraint(model.F, rule=linking_upper_rule)

	def linking_lower_rule(model, f):
		return model.x[f] >= model.y[f]
	model.linking_lower = Constraint(model.F, rule=linking_lower_rule)

	solver = SolverFactory('glpk')
	ret = solver.solve(model)
	if ret.solver.termination_condition != TerminationCondition.optimal:
		return JSONResponse(status_code=400, content={"error": "no optimal solution"})

	results = {"selected_food": [], "nutrients": []}
	results["cost"] = f"{value(model.cost):.2f}"

	count = 0
	for f in model.F:
		v = int(value(model.x[f]))
		if v != 0:
			results["selected_food"].append({f:v})
			count += 1

	if count != data['number']:
		return JSONResponse(status_code=400, content={"error": "unmatched number", "count": count, "number": data['number']})

	def inf_convert(val):
		if val == math.inf:
			return "INF"
		elif val == -math.inf:
			return "-INF"
		return val

	for n in model.N:
		actual = sum(value(model.a[f,n] * model.x[f]) for f in model.F)
		results["nutrients"].append({
			n:f"{actual:.4f}",
			"boundary":[inf_convert(value(model.Nmin[n])), inf_convert(value(model.Nmax[n]))]
		})

	return JSONResponse(status_code=200, content=results)

app = FastAPI()

@app.post("/api/optimize")
async def optimize_diet(request: Request):
	json_bytes = await request.body()

	json_str = json_bytes.decode('utf-8')
	data = json.loads(json_str)
	if not isinstance(data, dict):
		return JSONResponse(status_code=400, content={"error": "Invalid JSON format"})

	return linear_programming(data)
