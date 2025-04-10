def add(x,y):
    return x+y

def subtract(x,y):
    return x-y


def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x/y

def square(x,y):
    return x**y

def mod(x,y):
    return x%y

if __name__ == "__main__":

    print("Addition: ", add(5, 3))
    print("Subtraction: ", subtract(5, 3))
    print("Multiplication: ", multiply(5, 3))
    print("Division: ", divide(5, 3))
    print("Power: ", square(2, 4))
    print("Modulus: ", mod(10, 3))

