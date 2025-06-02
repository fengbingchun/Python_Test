from pyomo.environ import *
import argparse
import colorama
import time
import math
from pathlib import Path

# Blog: https://blog.csdn.net/fengbingchun/article/details/148379059

def parse_args():
	parser = argparse.ArgumentParser(description="pyomo glpk diet")
	parser.add_argument("--file", required=True, type=str, help="*.dat file or *.json file")
	parser.add_argument("--number", type=int, default=5, help="must select number of food types from all food types")

	args = parser.parse_args()
	return args

def parse_dat(file):
	# creating a model object
	model = ConcreteModel()

	# load data file
	data = DataPortal()
	data.load(filename=file)

	# define sets and parameters
	model.F = Set(initialize=data['F'])
	model.N = Set(initialize=data['N'])

	model.c = Param(model.F, initialize=data['c'], within=PositiveReals)
	model.a = Param(model.F, model.N, initialize=data['a'], within=NonNegativeReals)
	model.V = Param(model.F, initialize=data['V'], within=PositiveReals)
	model.Nmin = Param(model.N, initialize=data['Nmin'], within=NonNegativeReals, default=0.0)
	model.Nmax = Param(model.N, initialize=data['Nmax'], within=NonNegativeReals, default=float('inf'))
	model.Vmax = Param(initialize=data['Vmax'], within=PositiveReals)

	return model

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

def main(file, number):
	if Path(file).suffix.lower() == ".dat":
		model = parse_dat(file)
	elif Path(file).suffix.lower() == ".json":
		model = parse_json(file)
	else:
		raise ValueError(colorama.Fore.RED + f"unsupported file format: {file}")

	# define variables
	model.x = Var(model.F, within=NonNegativeIntegers)
	model.y = Var(model.F, within=Binary)

	# define the cost objective
	model.cost = Objective(expr=sum(model.c[i]*model.x[i] for i in model.F), sense=minimize)

	# define constraint
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

	# model.pprint() # print model structure

	# solve the model
	solver = SolverFactory('glpk')
	results = solver.solve(model)
	# print(f"results: {results}")
	if results.solver.termination_condition != TerminationCondition.optimal:
		raise ValueError(colorama.Fore.RED + f"no optimal solution was found")

	# print result
	print(f"total cost: {value(model.cost):.2f}")
	count = 0
	print("selected food:")
	for f in model.F:
		v = int(value(model.x[f]))
		if v != 0:
			print(f"  {f}: {v}")
			count += 1

	if count != number:
		raise ValueError(colorama.Fore.RED + f"solution result is wrong, number of food types does not match: {count}:{number}")

	print("nutrients:")
	for n in model.N:
		actual = sum(value(model.a[f,n] * model.x[f]) for f in model.F)
		print(f"  {n}: actual value: {actual:.2f}; boundary:[{value(model.Nmin[n])},{value(model.Nmax[n])}]")


if __name__ == "__main__":
	colorama.init(autoreset=True)
	args = parse_args()
	start = time.perf_counter()
	main(args.file, args.number)
	end = time.perf_counter()
	print(f"elapsed time: {end-start:.2f} seconds")

	print(colorama.Fore.GREEN + "====== execution completed ======")
