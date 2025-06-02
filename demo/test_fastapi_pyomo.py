from fastapi import FastAPI
from pyomo.environ import *
import math

def parse_json(file):
	model = ConcreteModel()

	data = DataPortal()
	data.load(filename=file)

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

def linear_programming_diet(file, number):
	model = parse_json(file)
	
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
		return sum(model.y[i] for i in model.F) == number
	model.select = Constraint(rule=select_rule)

	def linking_upper_rule(model, f):
		return model.x[f] <= model.y[f] * 1e6
	model.linking_upper = Constraint(model.F, rule=linking_upper_rule)

	def linking_lower_rule(model, f):
		return model.x[f] >= model.y[f]
	model.linking_lower = Constraint(model.F, rule=linking_lower_rule)

	solver = SolverFactory('glpk')
	results = solver.solve(model)
	if results.solver.termination_condition != TerminationCondition.optimal:
		return {"result":"no optimal solution"}

	results = {}
	results["total const"] = f"{value(model.cost):.2f}"

	foods = {}
	count = 0
	for f in model.F:
		v = int(value(model.x[f]))
		if v != 0:
			foods[f] = v
			count += 1

	results["selected food"] = foods
	if count != number:
		return {"result":"solution result is wrong, number of food types does not match"}

	nutrients = {}	
	for n in model.N:
		actual = sum(value(model.a[f,n] * model.x[f]) for f in model.F)
		nutrients[n] = f"{actual:.2f}"

	results["nutrients"] = nutrients
	return results


app = FastAPI()

@app.get("/diet")
def diet_optimization():
	return linear_programming_diet("../test_data/diet.json", 5)
