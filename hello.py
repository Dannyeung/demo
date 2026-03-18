"""
Simple Python Demo Project
"""


def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}! Welcome to Python GitHub workflow."


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract two numbers."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def calculator():
    """Simple calculator demo."""
    operations = [
        ("Add", add, 10, 5),
        ("Subtract", subtract, 10, 5),
        ("Multiply", multiply, 10, 5),
        ("Divide", divide, 10, 5),
    ]

    for name, func, a, b in operations:
        result = func(a, b)
        print(f"{name}: {a} {['+', '-', '*', '/'][operations.index((name, func, a, b))]} {b} = {result}")


def main():
    """Main function to demonstrate the project."""
    names = ["World", "GitHub User", "Python Developer"]

    for name in names:
        print(greet(name))

    print("\n--- Calculator Demo ---")
    calculator()


if __name__ == "__main__":
    main()
