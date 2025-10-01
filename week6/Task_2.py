from Task_1  import add_inventory_item

def calculate_total_value():
    item_id, item_name, quantity, price_per_item = add_inventory_item()
    total_value = quantity * price_per_item
    print(f"\nTotal Value: ${total_value: }")

    return total_value

if __name__ == "__main__":
    calculate_total_value()