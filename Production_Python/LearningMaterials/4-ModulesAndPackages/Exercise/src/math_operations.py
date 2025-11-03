def add(int1, int2):
    return int1 + int2


def subtract(int1, int2):
    return int1 - int2


def multiply(int1, int2):
    return int1 * int2


def divide(int1, int2):
    if int2 == 0:
        raise ValueError("Cannot divide by zero.")
    return int1 / int2


if __name__ == "__main__":
    print("src.math_operations is being executed directly.")
