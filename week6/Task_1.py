
item_id = 1000 

def add_inventory_item():
    Item_Name = input("Enter item name: ")
    Quantity = int(input("Enter quantity: "))
    Price_per_item = float(input("Enter price per item: "))
    global item_id
    item_id += 1
    return item_id,Item_Name,Quantity,Price_per_item


item_id,Item_Name,Quantity,Price_per_item = add_inventory_item()

print(f"Added item '{Item_Name}'  With ID {item_id}")
print(f"Item details: ID={item_id}, Name={Item_Name},Quantity={Quantity},Price per item={Price_per_item}")