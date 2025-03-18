from pyomo.environ import *
infinity = float('inf')
ninfinity = float('-inf')

# 1. creating a model object
model = AbstractModel()

# 2. F and N are declared abstractly using the Set component
model.F = Set() # Foods
model.N = Set() # Nutrients

# 3. the model parameters are defined abstractly using the Param component
model.c    = Param(model.F, within=PositiveReals) # Cost of each food
model.a    = Param(model.F, model.N, within=NonNegativeReals) # Amount of nutrient in each food
model.Nmin = Param(model.N, within=NonNegativeReals, default=0.0) # Lower bound on each nutrient
model.Nmax = Param(model.N, within=NonNegativeReals, default=infinity) # Upper bound on each nutrient
model.V    = Param(model.F, within=PositiveReals) # Volume per serving of food
model.Vmax = Param(within=PositiveReals) # Maximum volume of food consumed

# 4. Var component is used to define the decision variables
model.x = Var(model.F, within=NonNegativeIntegers) # Number of servings consumed of each food
model.y = Var(model.F, within=Binary) # decide whether to choose this food

# 5. Objective component is used to define the cost objective
def cost_rule(model): # Minimize the cost of food that is consumed
    return sum(model.c[i]*model.x[i] for i in model.F)
model.cost = Objective(rule=cost_rule, sense=minimize)

# 6. rule functions are used to define constraint expressions in the Constraint component:
def nutrient_rule(model, j): # Limit nutrient consumption for each nutrient
    value = sum(model.a[i,j]*model.x[i] for i in model.F)
    return inequality(model.Nmin[j], value, model.Nmax[j])
model.nutrient_limit = Constraint(model.N, rule=nutrient_rule)

def volume_rule(model): # Limit the volume of food consumed
    return sum(model.V[i]*model.x[i] for i in model.F) <= model.Vmax
model.volume = Constraint(rule=volume_rule)

def select_rule(model):
    return sum(model.y[i] for i in model.F) == 5
model.select = Constraint(rule=select_rule)

def linking_upper_rule(model, f):
    return model.x[f] <= model.y[f] * 1e6
model.linking_upper = Constraint(model.F, rule=linking_upper_rule)

def linking_lower_rule(model, f):
    return model.x[f] >= model.y[f]
model.linking_lower = Constraint(model.F, rule=linking_lower_rule)
