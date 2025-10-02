from Task3 import requisition_approval

def display_requisitons():
    requisition, staff_id, date, name, total, status, reference = requisition_approval()

    print("\nPrinting Requisitions:\n")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {name}")
    print(f"Total: ${total}")
    print(f"\nStatus: {status}\n")
    print(f"Approval Reference Nuber: {reference}")

display_requisitons()
    

