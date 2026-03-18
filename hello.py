"""
Simple Python Demo Project
"""


def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}! Welcome to Python GitHub workflow."


def main():
    """Main function to demonstrate the project."""
    names = ["World", "GitHub User", "Python Developer"]

    for name in names:
        print(greet(name))


if __name__ == "__main__":
    main()
