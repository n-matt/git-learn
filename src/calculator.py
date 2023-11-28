class Calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return 'Cannot divide by 0'
        return x * 1.0 / y

    def square(x, y):
        return x ** y

    def get_split(val):
        l1 = val.split("/")
        name = l1[-1]
        age = l1[-2]
        pla = l1[-2]
        return name, age, pla