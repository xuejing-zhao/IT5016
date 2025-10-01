def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b 
  
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "error: cannot divide by zero"

print(add(10, 2))
print(subtract(10, 2))
print(multiply(10, 2))
print(divide(10, 2))
print(divide(10, 2))