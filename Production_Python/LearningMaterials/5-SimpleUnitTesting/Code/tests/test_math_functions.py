# test_math_operations.py

from src.math_operations import add, subtract, multiply, divide

# dont need to define an add or testadd since we imported it
# def add(arg1, arg2):
#     return arg1 + arg2

# def test_add():
#     assert add(10, 20) == 30

def test_add():
    # Arrange 
    input_value_1 = 10
    input_value_2 = 20
    expected_output = 30

    # Act
    actual_output = add(input_value_1, input_value_2)
    
    # Assert
    assert actual_output == expected_output
    
def test_subtract():
    # Arrange 
    input_value_1 = 20
    input_value_2 = 10
    expected_output = 10

    # Act
    actual_output = subtract(input_value_1, input_value_2)
    
    # Assert
    assert actual_output == expected_output

# SO THIS IS AN EXAMPLE OF A PARAMETRIZED TEST, USING RANGES TO STRENGTHEN THE TEST

# def test_subtract():
#     #arrange
#     input_value_1 = range(1,100,1)
#     input_value_2 = range(100,1,-1)
#     expected_output = list(range(-99, 99, 2))
#     actual_outputs = list()

#     #act
#     for input_value_1, input_value_2 in zip(input_value_1, input_value_2):
#         actual_output = subtract(input_value_1, input_value_2)
#         actual_outputs.append(actual_output)
#         actual_outputs.append(subtract(input_value_1, input_value_2))

#     #assert
#     assert actual_outputs == expected_output

def test_multiply():
    # Arrange 
    input_value_1 = 10
    input_value_2 = 20
    expected_output = 200

    # Act
    actual_output = multiply(input_value_1, input_value_2)
    
    # Assert
    assert actual_output == expected_output

def test_divide():
    # Arrange 
    input_value_1 = 20
    input_value_2 = 10
    expected_output = 2

    # Act
    actual_output = divide(input_value_1, input_value_2)
    
    # Assert
    assert actual_output == expected_output