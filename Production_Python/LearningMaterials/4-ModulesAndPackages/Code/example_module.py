# example_module.py
def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


print("Hello world!")

if __name__ == "__main__":
    print("This is the main module.")
    print(f"Addition: {add(5, 3)}")
