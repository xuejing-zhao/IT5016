from Task1 import staff_info
def requisitions_total():
    requisition, date, staff_id, name = staff_info()

    total = 0
    grocery = {}

    enter_item = input("Enter your requistion items?\n (or input 'done' if you want to finish):")
    while enter_item.lower() != "done":
        price = float(input("Ehter the price $:"))
        grocery[enter_item] = price

        total = total + price

        enter_item = input("what would you like to order?\n (or 'done' if you want to finish):")

    print(f"Total is ${total}\n")        
    print(f"Here is your purchace:")

    for enter_item,price in grocery.items():
        print(f"{enter_item}:${price}")
    print(f"Total is ${total}\n") 


    return requisition, staff_id, date, name, total

if __name__ == "__main__":

   requisitions_total()


