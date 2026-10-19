# A clean Python file with no security issues
def add(a, b):
    """Add two numbers."""
    return a + b


def greet(name):
    """Greet a user."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("World"))
    print(add(1, 2))
