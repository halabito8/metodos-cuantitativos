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

inequality_constraints = []
inequality_matrix = []
right_hand_side = []
new_equation = True
while(new_equation):
    add_equation = input("Do you want to add a new equation? (Y/N): ")
    if add_equation == "N" or add_equation == "n":
        break
    matrix = []
    for i in range(len(list_coefficients)):
        x = input(f"Enter the value of x{str(i + 1)} for equation: ")
        matrix.append(int(x))
    inequality_matrix.append(matrix)
    x = input("Enter the right hand side value: ")
    inequality_constraints.append(int(x))

list_coefficients = np.array(list_coefficients)
inequality_matrix = np.array(inequality_matrix)
inequality_constraints = np.array(inequality_constraints)
solve_simplex(list_coefficients, inequality_matrix, inequality_constraints)
