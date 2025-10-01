from Task_1 import add_inventory_item

inventory = {}

def update_inventory():
    item_id = int(input("Enter Item ID to update: "))
   
    if item_id in inventory:
        new_quantity = int(input("Enter new quantity: "))
        new_price = float(input("Enter new price per item: "))

        inventory[item_id]["quantity"] = new_quantity
        inventory[item_id]["price"] = new_price
        print(f"Item ID {item_id} updated -> Quantity {new_quantity}, price ${new_price:}")
    else:
         print("Item not found !")

         if__name__ == "__main__"

    item_id, name, quantity, price = add_inventory_item()
    inventory[item_id] = {"name": name, "quantity": quantity, "price": price}
    
    update_inventory()
    