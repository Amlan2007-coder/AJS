contacts = []
menu = 0
while menu != 3:
    menu = int(input("Pick the option from menu - 1 or 2 or 3 !"))
    if menu == 1:
        result = input("Give the name!")
        result_1 = input("Give the phone number!")
        result_3 = {"name" : result, "phone-" : result_1 }
        contacts.append(result_3)
        print("Saved")
    elif menu == 2:
        for contact in contacts:
            print(contact)

print("You are welcome!")






