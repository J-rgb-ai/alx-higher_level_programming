#!/usr/bin/python3


def handle_division(a, b):
    """Performs division and handles ZeroDivisionError exception."""
    try:
        return int(a / b)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        exit(1)


def handle_operation(a, operator, b):
    """Selects and performs the appropriate operation based on the operator."""
    operators = {"+": lambda a, b: a + b,
                 "-": lambda a, b: a - b,
                 "*": lambda a, b: a * b,
                 "/": handle_division}
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    return operators[operator](a, b)


def main():
    """Gets arguments, validates them, and performs the calculation."""
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    try:
        # Validate arguments are integers
        a = int(sys.argv[1])
        operator = sys.argv[2]
        b = int(sys.argv[3])
    except ValueError:
        print("All arguments must be integers")
        exit(1)

    result = handle_operation(a, operator, b)
    print(f"{a} {operator} {b} = {result}")


if __name__ == "__main__":
    main()
