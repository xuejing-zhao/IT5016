far_temperature = float(input("Enter temperature in fahrenheit:" ))
temperature=(far_temperature - 32)/1.8
print(temperature)
print()
if temperature >= 50 or temperature <-30 :
    print("Waring: Extyeme temperature .")
elif temperature > 30:
    print("It's a hot day. ")
elif temperature >= 20:
    print("It's a warm day. ")    
else:
    print("It's a cold day. ")    
