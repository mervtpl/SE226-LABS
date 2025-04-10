import math_utils
def main():

    x=input("enter a number: ")
    y=input("enter another number: ")
    operation=input("enter an operation (add, subtract, multiply, divide, squere,): ")

    dict={ "add":math_utils.add,
            "subtract":math_utils.subtract,
            "multiply": math_utils.multiply,
            "divide": math_utils.divide,
            "square":math_utils.square,
            "mod": math_utils.mod}

    if operation in dict:

        print("the result of ",operation, "is: ", dict[operation](int(x), int(y)))
    else:
        raise ValueError("operation not found")

if __name__ == "__main__":
    main()




