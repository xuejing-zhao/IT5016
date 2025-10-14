def add(a, b):
    return a + b

def multiply(x, y):
    return x * y

def add_end_multiply(a, b, c):
    sun_result = add(a, b)
    product_result = multiply(sun_result, c)
    return product_result

result = add_end_multiply(2, 3, 4)
print(result)