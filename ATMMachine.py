correct_pin = "1234"
balance = 5000
attempts=0

print("===Welcome to ATM ====")

print("Select language: ")
print("1. English")
print("2. Hindi")
language = input("Enter 1 or 2: ")

if language == "1":
    print("Thank you for choicing this labguage.")
else:
    print("Sorry currently only english language is available.")

while attempts <3:
    pin = input("\nEnter 4-digit PIN: ")

    if len(pin) !=4:
        print("PIN must be exactly 4 digits ")
        continue

    if pin == correct_pin:
        print("PIN verified")
        print("Menu:")
        print("1. Balance Check")
        print("2. Deposit")
        print("3. Withdraw")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            print("YOUr Balance = ", balance)

        elif choice == "2":
            amount = int(input("Enter Amount to Deposit : "))
            balance = balance +amount
            print("Deposit Successful")
            print("Updated balance = ",balance)

        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))
            if amount> balance:
                print("Not Enough Balance")
            else:
                balance = balance-amount
                print("Withdraw Successful")
                print("Updated balance =", balance)

                
        else:
            print("Invalid option")
        break
    else:
        attempts += 1
        print("incorrect PIN")

if attempts == 3:
    print("3 Wrong attempts")
    print("Your ATm Card is locked for 24 hours")
    
    