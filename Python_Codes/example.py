#!/usr/bin/env python3
"""
A basic Python script example.
"""


def greet(name):
    """Greet a person by name."""
    return f"Hello, {name}!"


def main():
    """Main function."""
    print(greet("World"))
    
    # Example: Simple arithmetic
    numbers = [1, 2, 3, 4, 5]
    total = sum(numbers)
    average = total / len(numbers)
    
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    print(f"Average: {average}")


if __name__ == "__main__":
    main()
