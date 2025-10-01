correct_password = "python123"
attempts = 3
while attempts > 0:
    password = input("Enter password: " )
    if password == correct_password:
        print("Access granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect! (attempts) attempts left.")
if attempts == 0:
    print("Access denied. Too many failed attempts. ") 
    choice = input(" DO you want to reset your password? (yes/no:) ")       
    if choice == "yes":
        new_password = input("Enter new password: ")
        correct_password = new_password
        attempts = 3
        print("password has been reset. please try again.")