from scipy.optimize import linprog
 
def get_positive_float_input(prompt):
    """Gets a positive float value from the user with error handling."""
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            else:
                print("Please enter a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a number.")
 
# ---------------- USER INPUTS ----------------
num_products = int(get_positive_float_input("Enter the number of products: "))
num_ingredients = int(get_positive_float_input("Enter the number of ingredients: "))
 
ingredient_names = [input(f"Enter name for ingredient {i+1}: ") for i in range(num_ingredients)]
product_names = [input(f"Enter name for product {i+1}: ") for i in range(num_products)]
 
ingredient_availability = {name: get_positive_float_input(f"Enter total available units of {name}: ") for name in ingredient_names}
 
product_profits = {}
product_consumption = {}
 
for p_name in product_names:
    print(f"\n--- Data for Product: {p_name} ---")
    product_profits[p_name] = get_positive_float_input(f"Enter profit for each unit of {p_name}: ")
    product_consumption[p_name] = {i_name: get_positive_float_input(f"Enter {i_name} required for each unit of {p_name}: ") for i_name in ingredient_names}
 
# ---------------- BUILD MATRICES FOR LINEAR PROGRAM ----------------
objective = [-product_profits[p_name] for p_name in product_names]  # negate for maximization
lhs_ineq = [
    [product_consumption[p_name][i_name] for p_name in product_names]
    for i_name in ingredient_names
]
rhs_ineq = [ingredient_availability[i_name] for i_name in ingredient_names]
variable_bounds = [(0, None) for _ in product_names]

# ---------------- SOLVE MODEL ----------------
result = linprog(
    c=objective,
    A_ub=lhs_ineq,
    b_ub=rhs_ineq,
    bounds=variable_bounds,
    method="highs",
)

# ---------------- DISPLAY RESULTS ----------------
print("\nOptimization Result:")
if result.success:
    for p_name, quantity in zip(product_names, result.x):
        print(f"Units of {p_name} to produce: {quantity}")
    print(f"Maximum Profit: Rs {-result.fun}")
else:
    print("Solver failed:", result.message)
