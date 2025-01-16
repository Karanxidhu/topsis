import argparse
import sys

def valid_operators(value):
    operators = value.split(',')  # Split by comma
    valid_ops = ['+', '-']
    for op in operators:
        if op not in valid_ops:
            raise argparse.ArgumentTypeError(f"Invalid operator: '{op}'. Allowed operators are {valid_ops}.")
    return operators

def valid_numbers(value):
    try:
        numbers = [float(num) for num in value.split(',')]
        return numbers
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid numbers. Provide a comma-separated list of numbers.")

# parser = argparse.ArgumentParser(description="Process numbers and operators")

# Add arguments

# parser.add_argument(
#     '--data',
#     type=str,
#     required=True,
#     help="Enter the CSV file"
# )

# parser.add_argument(
#     '--weights',
#     type=valid_numbers,
#     required=True,
#     help="Comma-separated list of numbers (e.g., 1,2,3.5)"
# )

# parser.add_argument(
#     '--impact',
#     type=str,
#     required=True,
#     help="Comma-separated list of operators (e.g., +,-)"
# )

# args = parser.parse_args()
args = sys.argv

data = args[1]
weights = valid_numbers(args[2])
impact = valid_operators(args[3])
output = args[4]

print(f"Data: {data}")
print(f"Weights: {weights}")
print(f"Impact: {impact}")
