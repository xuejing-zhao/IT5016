from itertools import count

def staff_info():
    requisition = 10000
    print("Printing Staff Information:")
    date =input("Date:")
    staff_id =input("Staff ID:")
    staff_name=input("Staff Name:")
   #Requisition ID
    requisition = requisition + 1
    print(f"Requisition ID:{requisition}")
    
    return requisition,date,staff_id,staff_name

if __name__ == "__main__":
    print(staff_info())

