from Task_1  import add_inventory_item

def display_inventory_item():

   item_id, item_name, quantity, price_per_item = add_inventory_item()

   total_value = quantity * price_per_item

   print("\nDisplaying Inventory Item:\n")
   print(f"Item Name: {item_name}")
   print(f"Item ID: {item_id}")
   print(f"Quantity: {quantity}")
   print(f"Price per Item: ${price_per_item}")
   print(f"Total Value: ${total_value: }")


   return item_id, item_name, quantity, price_per_item, total_value

if __name__ == "__main__":
    
 display_inventory_item()
