def is_even(n):
    return n % 2 ==0

def find_max(a, b, c):
    return max(a, b, c)
    
        
def factorial(n):
    result = 1
    for l in range(1, n + 1):
        result = result * l
    return result

print("is_even(8):", is_even(8))  
print("is_even(9):", is_even(9))  
print("find_max(3, 5, 10):",find_max(3,5,10))
print("factorial(5):", factorial(5))