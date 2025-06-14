while True:
    print("\nWelcome to the Bill Splitter App!")

    bill = float(input("Enter total bill amount: "))
    if bill <= 0:
        print("Bill must be positive.")
        continue

    people = int(input("Enter number of people: "))
    if people <= 0:
        print("Number of people must be greater than 0.")
        continue

    tip_percent = int(input("Enter tip percentage (0/5/10/15/20): "))
    if tip_percent not in [0, 5, 10, 15, 20]:
        print("Tip must be one of 0, 5, 10, 15, 20.")
        continue

    tip = (tip_percent / 100) * bill
    final_bill = bill + tip
    per_person = final_bill / people

    print(f"\ntip amount: ₹{tip}")
    print(f"\ntotal bill: ₹{bill + tip}")
    print(f"\neach person should pay: ₹{final_bill / people }:")

    print(input("\nwould you like calculet another bill? (y/n): y"))
    print ("...")
