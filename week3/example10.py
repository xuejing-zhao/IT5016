print("Kia Ora, this is a parking meter")
park_time = 4
print("park_time time is", park_time,"hours.")

rate = 4
cost = 0
if park_time > 3:
    cost = rate *3
    rate -= 2
    park_time -= 3
    cost += rate * park_time
    print("The cost of the parking is $", cost)

else:
    cost = rate * park_time
    print("The cost of the parking is $", cost)
