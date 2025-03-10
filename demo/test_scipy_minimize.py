import numpy as np
from scipy.optimize import minimize
from functools import partial

# Blog: https://blog.csdn.net/fengbingchun/article/details/146128071

def solve_equations():
    # 0.033x+0.08y+0.22z=6
    # 46.07x+64.58y+64.81z=6200
    # 14.15x+0.63y+0.53z=9.9

    A = np.array([
        [0.033, 0.08, 0.22],
        [46.07, 64.58, 64.81],
        [14.15, 0.63, 0.53]
    ])

    B = np.array([6., 6200, 9.9])

    try:
        x, y, z = np.linalg.solve(A, B)
        print(f"result: x:{x:.4f}, y:{y:.4f}, z:{z:.4f}")
        print(f"value1(expected:6): {0.033*x+0.08*y+0.22*z:.2f}")
        print(f"value2(expected:6200): {46.07*x+64.58*y+64.81*z:.2f}")
        print(f"value3:(expected:9.9): {14.15*x+0.63*y+0.53*z:.2f}")
    except np.linalg.LinAlgError:
        print("Error: the system of equations has no solutions or has infinitely many solutions")

def objective(x):
    return 0

def constraint(x, a, b, c, value, inequality_type):
    if inequality_type == "lower":
        return a * x[0] + b * x[1] + c * x[2] - value # a*x + b*y + c*z >= value
    elif inequality_type == "upper":
        return value - (a * x[0] + b * x[1] + c * x[2]) # a*x + b*y + c*z <= value
    elif inequality_type == "eq":
        return a * x[0] + b * x[1] + c * x[2] - value # a*x + b*y + c*z == value
    else:
        raise ValueError(f"invalid inequality_type: {inequality_type}")

def solve_inequalities():
    # 0.033x+0.08y+0.22z = 6
    # 6200 < 46.07x+64.58y+64.81z < 6230
    # 9.9 < 14.15x+0.63y+0.53z < 78

    a1, b1, c1 = 0.033, 0.08, 0.22
    a2, b2, c2 = 46.07, 64.58, 64.81
    a3, b3, c3 = 14.15, 0.63, 0.53

    bounds = [(-4, -2), (110, 113), (-13, -11)] # x,y,z
    num = 10
    samplesx = np.linspace(bounds[0][0], bounds[0][1], num=num, endpoint=False, dtype=float)
    samplesy = np.linspace(bounds[1][0], bounds[1][1], num=num, endpoint=False, dtype=float)
    samplesz = np.linspace(bounds[2][1], bounds[2][1], num=num, endpoint=False, dtype=float)

    cons = [
        {"type": "eq", "fun": partial(constraint, a=a1, b=b1, c=c1, value=6, inequality_type="eq")},
        {"type": "ineq", "fun": partial(constraint, a=a2, b=b2, c=c2, value=6200, inequality_type="lower")},
        {"type": "ineq", "fun": partial(constraint, a=a2, b=b2, c=c2, value=6230, inequality_type="upper")},
        {"type": "ineq", "fun": partial(constraint, a=a3, b=b3, c=c3, value=9.9, inequality_type="lower")},
        {"type": "ineq", "fun": partial(constraint, a=a3, b=b3, c=c3, value=78, inequality_type="upper")}
    ]

    results = set()

    for index, xvalue in enumerate(samplesx):
        # print(f"index: {index}, xvalue:{xvalue}")
        for yvalue in samplesy:
            for zvalue in samplesz:
                x0 = [xvalue, yvalue, zvalue]

                solution = minimize(objective, x0, method="SLSQP", bounds=bounds, constraints=cons)
                if solution.success:
                    x, y, z = solution.x
                    if abs(a1*x+b1*y+c1*z-6) < 0.1 and 6200 < a2*x+b2*y+c2*z < 6230 and 9.9 < a3*x+b3*y+c3*z < 78:
                        result = (float(round(x, 4)), float(round(y, 4)), float(round(z, 4)), float(round(a1*x+b1*y+c1*z, 4)), float(round(a2*x+b2*y+c2*z, 4)), float(round(a3*x+b3*y+c3*z, 4)))
                        results.add(result)
                        # print(f"result: x:{x:.4f}, y:{y:.4f}, z:{z:.4f}")
                        # print(f"value1(expected:6): {a1*x+b1*y+c1*z:.2f}")
                        # print(f"value2(expected:(6200,6230)): {a2*x+b2*y+c2*z:.2f}")
                        # print(f"value3:(expected:(9.9,78)): {a3*x+b3*y+c3*z:.2f}")
                # else:
                #     print("no solutions")

    for index, result in enumerate(results):
        print(f"index: {index}, result: {result}")

if __name__ == "__main__":
    # solve_equations()
    solve_inequalities()

    print("====== execution completed ======")
