from Task2 import requisitions_total

def requisition_approval():
    
    requisition, staff_id, date, name, total = requisitions_total()

    if total < 500:
        status= "Approved"

    elif total >= 500:
        status = "Pending"    

    else:
        print("Error !")    

    reference = str(staff_id) + str(requisition)[-3:]
    print(f"Status:{status}")
    print(f"Approval Reference Number:{reference}\n")

    return requisition, staff_id, date, name, total, status, reference

if __name__ == "__main__":

  requisition_approval()