import numpy as np
from scipy.optimize import linprog

def solve_simplex(c, A_ub, b_ub):
    result = linprog(-c, A_ub=A_ub, b_ub=b_ub, method='simplex')
    
    if result.success:
        print("Optimal solution found:")
        print("Objective value:", -result.fun)  # Negate the objective value for maximization
        print("Solution:", result.x)
    else:
        print("Optimization failed:", result.message)

# Example problem
c = np.array([1000, 500, 2500])  # Coefficients of the objective function to maximize
A_ub = np.array([[100, 80, 0], [90, 50, 100], [30, 100, 40]])  # Coefficients matrix for inequality constraints
b_ub = np.array([200, 250, 180])  # Right-hand side values for inequality constraints

solve_simplex(c, A_ub, b_ub)

# entrada = 0
# while(True):
#     if entrada == 1:
#         break
#     entrada = int(input("1. Salir\n2. Ingresar datos\n"))