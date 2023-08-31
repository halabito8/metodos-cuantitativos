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


# Gather coefficients of the objective function to maximize
list_coefficients = []
coefficient = 0
print("Enter a number to add to the coefficients when done enter N:")
while(True):
    if coefficient == "N" or coefficient == "n":
        break
    coefficient = input("Coefficient: ")
    if coefficient.isdigit():
        list_coefficients.append(int(coefficient))

# Example problem
A_ub = np.array([[100, 80, 0], [90, 50, 100], [30, 100, 40]])  # Coefficients matrix for inequality constraints
b_ub = np.array([200, 250, 180])  # Right-hand side values for inequality constraints

list_coefficients = np.array(list_coefficients)
solve_simplex(list_coefficients, A_ub, b_ub)
