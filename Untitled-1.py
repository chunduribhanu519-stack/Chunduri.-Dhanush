list_a = [["Apexium", "9391899088", "4212", "9000", "19/06/2008"]]

list_b = [["Apexium", "9391899088", "4212", "3000", "19/06/2008"], ["ss", "1234567890","1234","1234567890","31/10/2000"]]

list_c = [["Apexium", "9391899088", "4212", "5000", "19/06/2008"],["MEHAR", "9100926028", "2536", "1234567890", "15/12/2006"]]

list_of_leap_years = [1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024]

list_of_mobile_recharges = [1799, 3599, 91, 75, 179, 155, 77, 5999, 599, 399, 349, 299, 239, 199]

list_all = [list_c, list_a, list_b]

def Deposite_incorrect_pin():
    print("Incorrect Pin Number ")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        i[3] = str(int(i[3]) + int(deposit_amount))
        print("Amount Deposited Successfully")
        print("Your New Balance is: ", i[3])
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            i[3] = str(int(i[3]) + int(deposit_amount))
            print("Amount Deposited Successfully")
            print("Your New Balance is: ", i[3])
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Withdraw_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        if int(withdraw_amount) <= int(i[3]):
            i[3] = str(int(i[3]) - int(withdraw_amount))
            print("Amount Withdrawn Successfully")
            print("Your New Balance is: ", i[3])
        else:
            print("Insufficient Balance")
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            if int(withdraw_amount) <= int(i[3]):
                i[3] = str(int(i[3]) - int(withdraw_amount))
                print("Amount Withdrawn Successfully")
                print("Your New Balance is: ", i[3])
            else:
                print("Insufficient Balance")
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Check_balance_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        print("Your Balance is: ", i[3])
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            print("Your Balance is: ", i[3])
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Transfer_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        if int(transfer_amount) <= int(i[3]):
            for j in list_c:
                if receiver_phone == j[1]:
                    i[3] = str(int(i[3]) - int(transfer_amount))
                    j[3] = str(int(j[3]) + int(transfer_amount))
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            if int(transfer_amount) <= int(i[3]):
                for j in list_c:
                    if receiver_phone == j[1]:
                        i[3] = str(int(i[3]) - int(transfer_amount))
                        j[3] = str(int(j[3]) + int(transfer_amount))
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Delete_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        list_all.remove(i)
        print("Account Deleted Successfully")
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            list_all.remove(i)
            print("Account Deleted Successfully")
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def output_all_account_details_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        print("-----Invoice-----")
        print("Name: ", i[0])
        print("phone: ", i[1])
        print("Balance: ", i[3])
        print("-----------------")
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            print("-----Invoice-----")
            print("Name: ", i[0])
            print("phone: ", i[1])
            print("Balance: ", i[3])
            print("-----------------")
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Change_account_name_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        i[0] = new_name
        print("Name Changed Successfully")
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            i[0] = new_name
            print("Name Changed Successfully")
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Change_phone_number_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        i[1] = new_phone
        print("phone Number Changed Successfully")
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            i[1] = new_phone
            print("phone Number Changed Successfully")
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def E_commerce_shopping_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        if int(shopping_amount) <= int(i[3]):
            i[3] = str(int(i[3]) - int(shopping_amount))
            print("Shopping Amount Deducted Successfully")
            print("Your New Balance is: ", i[3])
        else:
            print("Insufficient Balance for Shopping")
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            if int(shopping_amount) <= int(i[3]):
                i[3] = str(int(i[3]) - int(shopping_amount))
                print("Shopping Amount Deducted Successfully")
                print("Your New Balance is: ", i[3])
            else:
                print("Insufficient Balance for Shopping")
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Apply_for_loan_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2] and int(i[3]) >= 5000:
        i[3] = str(int(i[3]) + int(loan_amount))
        print("Amount Deposited Successfully")
        print("Loan Application Successful for amount:", loan_amount)
        print("Your New Balance is: ", i[3])
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2] and int(i[3]) >= 5000:
            i[3] = str(int(i[3]) + int(loan_amount))
            print("Amount Deposited Successfully")
            print("Loan Application Successful for amount:", loan_amount)
            print("Your New Balance is: ", i[3])
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Mobile_recharge_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        if int(recharge_amount) <= int(i[3]):
            i[3] = str(int(i[3]) - int(recharge_amount))
            print("Mobile Recharged Successfully")
            print("Your New Balance is: ", i[3])
            print("your cashback 3% is credeted to your Bank account")
            i[3] = str(round(int(i[3]) + int(recharge_amount * 3) / 100))
            print("Your New Balence is:", i[3])
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            if int(recharge_amount) <= int(i[3]):
                i[3] = str(int(i[3]) - int(recharge_amount))
                print("Mobile Recharged Successfully")
                print("Your New Balance is: ", i[3])
                print("your cashback 3% is credeted to your Bank account")
                i[3] = str(round(int(i[3]) + int(recharge_amount * 3) / 100))
                print("Your New Balence is:", i[3])
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def fixed_deposit_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        if int(fd_amount) <= int(i[3]):
            i[3] = str(int(i[3]) - int(fd_amount))
            a = int(fd_amount) + ((int(fd_amount)) * 12.7410) / 100

            print("Fixed Deposit Created Successfully")
            print("Your amount will be credited after 1 year with interest of 12.7410% :", round(a, 3))
            print("Your New Balance is: ", i[3])
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            if int(fd_amount) <= int(i[3]):
                i[3] = str(int(i[3]) - int(fd_amount))
                a = int(fd_amount) + ((int(fd_amount)) * 12.7410) / 100

                print("Fixed Deposit Created Successfully")
                print("Your amount will be credited after 1 year with interest of 12.7410% :", round(a, 3))
                print("Your New Balance is: ", i[3])
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Bengulur_transfer_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        list_a.append(i)
        list_c.remove(i)
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            list_a.append(i)
            list_c.remove(i)
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Dolkpur_transfer_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        list_c.append(i)
        list_a.remove(i)
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            list_c.append(i)
            list_a.remove(i)
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def Hydrabad_transfer_incorrect_pin():
    print("Incorrect Pin Number")
    print("Try Again")
    print("2 attempts left")
    Pin = input("Enter your Pin Number: ")
    Pin = is_valid_Pin(Pin)
    if Pin == i[2]:
        list_b.append(i)
        list_c.remove(i)
        print("Account Transferred Successfully to Hydrabad Branch")
    elif Pin != i[2]:
        print("Incorrect Pin Number")
        print("Try Again")
        print("1 attempt left")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        if Pin == i[2]:
            list_b.append(i)
            list_c.remove(i)
        elif Pin != i[2]:
            print("Incorrect Pin Number")
            print("No attempts left")
            print("Choose forget Pin option to reset your Pin")

def dob_incorrect():
    print("Incorrect Date of Birth")
    print("Try Again")
    print("2 attempts left")
    dob = (f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1])
    dob = is_valid_dob(dob)
    if dob == i[4]:
        new_Pin = input("Enter your new Pin Number: ")
        new_Pin = is_valid_Pin(new_Pin)
        i[2] = new_Pin
        print("Pin Reset Successfully")
    elif dob != i[4]:
        print("Incorrect Date of Birth")
        print("Try Again")
        print("1 attempt left")
        dob = (f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1])
        dob = is_valid_dob(dob)
        if dob == i[4]:
            new_Pin = input("Enter your new Pin Number: ")
            new_Pin = is_valid_Pin(new_Pin)
            i[2] = new_Pin
            print("Pin Reset Successfully")
        elif dob != i[4]:
            print("Incorrect Date of Birth")
            print("No attempts left")
            print("Please contact customer care for further assistance")

def Create_account():
    print("you are going to create an account in Apexium Banking")
    print("choose your branch \n 1.Benguluru \n 2.Dolkpur \n 3.Hyderabad")
    branch_choice = input("Enter the branch number you want to choose: ")
    branch_choice = is_valid_branch_choice(branch_choice)
    if branch_choice == "1":
        name = input("Enter Your name with out dots : ")
        name = is_valid_name(name)
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        for i in list_c:
            if phone == i[1]:
                print("you have already an account in bengulur ")
                print("create again with another number")
                Create_account()
        Pin = input("Create a 4 digit Pin Number? ")
        Pin = is_valid_Pin(Pin)
        Amount = input("Enter the amount you want to deposit? ")
        Amount = is_valid_amount(Amount)
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        list_of_details = [name, phone, Pin, Amount, Date_of_birth]
        list_c.append(list_of_details)
        print("Account Created Successfully on Bengulur Branch")
        print("Name: ", name)
        print("phone: ", phone)
        print("Balance: ", Amount)
        print("dob: ", Date_of_birth)
        print("pin: ", Pin)
        print("Please Take a photo of your details for future reference")
        print("please remember your pin for future transactions")
        print("Thank you for choosing our bank")
    elif branch_choice == "2":
        name = input("Enter Your name with out dots : ")
        name = is_valid_name(name)
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        for i in list_a:
            if phone == i[1]:
                print("you have already an account in Dolkpur ")
                print("create again with another number")
                Create_account()
        Pin = input("Create a 4 digit Pin Number? ")
        Pin = is_valid_Pin(Pin)
        Amount = input("Enter the amount you want to deposit? ")
        Amount = is_valid_amount(Amount)
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        list_of_details = [name, phone, Pin, Amount, Date_of_birth]
        list_a.append(list_of_details)
        print("Account Created Successfully on Dolkpur Branch")
        print("Name: ", name)
        print("phone: ", phone)
        print("Balance: ", Amount)
        print("dob: ", Date_of_birth)
        print("pin: ", Pin)
        print("Please Take a photo of your details for future reference")
        print("please remember your pin for future transactions")
        print("Thank you for choosing our bank")
    elif branch_choice == "3":
        name = input("Enter Your name with out dots : ")
        name = is_valid_name(name)
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        for i in list_b:
            if phone == i[1]:
                print("you have already an account in Hydrabad ")
                print("create again with another number")
                Create_account()
        Pin = input("Create a 4 digit Pin Number? ")
        Pin = is_valid_Pin(Pin)
        Amount = input("Enter the amount you want to deposit? ")
        Amount = is_valid_amount(Amount)
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        list_of_details = [name, phone, Pin, Amount, Date_of_birth]
        list_b.append(list_of_details)
        print("Account Created Successfully on Hydrabad Branch")
        print("Name: ", name)
        print("phone: ", phone)
        print("Balance: ", Amount)
        print("dob: ", Date_of_birth)
        print("pin: ", Pin)
        print("Please Take a photo of your details for future reference")
        print("please remember your pin for future transactions")
        print("Thank you for choosing our bank")

def is_valid_branch_choice(branch_choice):
    if branch_choice.isdigit():
        if 0 < int(branch_choice) < 4:
            return branch_choice
        elif int(branch_choice) > 3:
            print("Your entering more than 3 \n you will give me only input less than 4 and greter than 0")
            branch_choice = input()
            branch_choice = is_valid_branch_choice(branch_choice)
            return branch_choice
        elif int(branch_choice) < 1:
            print("Your entering less than 1\n you will give me only input less than 4 and greter than 0")
            branch_choice = input()
            branch_choice = is_valid_branch_choice(branch_choice)
            return branch_choice
        else:
            print("invalid Choice")
            print("Enter a values only 1 ,2 ,3")
            branch_choice = input()
            branch_choice = is_valid_branch_choice(branch_choice)
            return branch_choice
    elif branch_choice.isalpha():
        print("You are entering Alphabets \n Enter values only 1,2,3")
        print("Try Again")
        branch_choice = input()
        branch_choice = is_valid_branch_choice(branch_choice)
        return branch_choice
    else:
        print("you are entering something not values 1,2,3")
        print("Try Again")
        branch_choice = input()
        branch_choice = is_valid_branch_choice(branch_choice)
        return branch_choice

def is_valid_choice(choice):
    if choice in ["DVKCSPKSSRTR", "!@#", "$%^", "&*()"]:
        return choice
    elif choice.isdigit():
        if 0 <= int(choice) < 4:
            return choice
        elif int(choice) > 3:
            print("Your entering more than 3 \n you will give me only input less than 4 and greter than 0")
            choice = input('Enter correct choice')
            choice = is_valid_choice(choice)
            return choice
        elif int(choice) < 0:
            print("Your entering less than are equal to 0\n you will give me only input less than 4 and greter than 0")
            choice = input()
            choice = is_valid_choice(choice)
            return choice
        else:
            print("invalid Choice")
            print("Enter a values only 0,1 ,2 ,3")
            choice = input()
            choice = is_valid_choice(choice)
            return choice
    elif choice.isalpha():
        print("You are entering Alphabets \n Enter values only 0,1,2,3")
        print("Try Again")
        choice = input()
        choice = is_valid_choice(choice)
        return is_valid_choice(choice)
    else:
        print("you are entering something not values 0,1,2,3")
        print("Try Again")
        choice = input()
        choice = is_valid_choice(choice)
        return is_valid_choice(choice)

def is_valid_name(name):
    name2 = name.strip().replace(" ", "")
    if name2.isalpha():
        return name
    elif name.isdigit():
        print('your entering the numbers instead of name')
        print("Try Again")
        name = input("Enter your  name: ")
        name = is_valid_name(name)
        return name
    else:
        print('Invalid name. Please enter a valid name.')
        print("your are using special characters\n or using both letters and numbers")
        print("Try Again")
        name = input("Enter your  name: ")
        name = is_valid_name(name)
        return name

def is_valid_Pin(Pin):
    if Pin.isdigit() and len(Pin) == 4:
        return Pin
    elif Pin.isalpha():
        print('your entering the letters instead of numbers')
        print("Try Again")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        return Pin
    elif Pin.isdigit() and len(Pin) < 4:
        print('Pin number should be 4 digits long')
        print("Try Again")
        Pin = input("Enter your Pin Number")
        Pin = is_valid_Pin(Pin)
        return Pin
    elif Pin.isdigit() and len(Pin) > 4:
        print('Pin number should be 4 digits long')
        print("you are entering more than 4 digits")
        print("Try Again")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)
        return Pin
    else :
        print("Try Again")
        Pin = input("Enter your Pin Number: ")
        Pin = is_valid_Pin(Pin)

def is_valid_amount(a):
    if a.isdigit():
        return a
    elif a.isalpha():
        print('your entering the letters instead of numbers')
        print('Invalid amount. Please enter a valid amount in numbers.')
        print("Try Again")
        a = input("Enter the amount you want to deposit: ")
        a = is_valid_amount(a)
        return a

def is_valid_phone(phone):
    if  len(phone)==10 and  phone.isdigit( ):
               return phone
    elif phone.isalpha():
        print('your entering the letters instead of numbers')
        print("Try Again")
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        return phone
    elif phone.isdigit( ) and len(phone) < 10:
        print('phone number should be 10 digits long')
        print("Try Again")
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        return phone
    elif phone.isdigit( ) and len(phone) > 10:
        print('phone number should be 10 digits long')
        print("you are entering more than 10 digits")
        print("Try Again")
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        return phone
    else:
        print("Try again")
        phone = input("Enter Your Mobile Number? ")
        phone = is_valid_phone(phone)
        return phone
        
def is_valid_dob(Date_of_birth):
    day, month, year = map(int, Date_of_birth.split('/'))
    if 1 <= day <= 31 and 1 <= month <= 12 and 2025 > year > 1926:
        if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12) and day <= 31:
            return Date_of_birth
        elif (month == 4 or month == 6 or month == 9 or month == 11) and day <= 30:
            return Date_of_birth
        elif (month == 2 and day <= 28) or year in list_of_leap_years and day == 29:
            return Date_of_birth
        else:
            print("Invalid Date of Birth")
    if year >= 2026:
        print('Invalid Date of Birth. Year should be less than 2026.')
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth
    if year <= 1926:
        print('Invalid Date of Birth. Year should be greater than 1926.')
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth
    if not (1 <= day <= 31):
        print('Invalid Date of Birth. Day should be between 1 and 31.')
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth
    if not (1 <= month <= 12):
        print('Invalid Date of Birth. Month should be between 1 and 12.')
        print("Try Again")
        print("Re enter the Full Date of Birth")
        Date_of_birth = f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1]
        Date_of_birth = is_valid_dob(Date_of_birth)
        return Date_of_birth

def is_choice_valid(choice):
    if choice in ["DVKCSPKSSRTR", "!@#", "$%^", "&*()"]:
        return choice
    elif choice.isdigit():
        if 0 < int(choice) < 18:
            return choice
        elif int(choice) > 17:
            print("Your entering more than 17 \n you will give me only input less than 18 and greter than 0")
            choice = input()
            choice = is_choice_valid(choice)
            return choice
        elif int(choice) < 1:
            print("Your entering less than are equal to 1\n you will give me only input less than 18 and greter than 0")
            choice = input()
            choice = is_choice_valid(choice)
            return choice
        else:
            print("invalid Choice")
            print("Enter a values only between 1 to 17")
            choice = input()
            choice = is_choice_valid(choice)
            return choice
    elif choice.isalpha():
        print("You are entering Alphabets \n Enter values only between 1 to 17")
        print("Try Again")
        choice = input()
        choice = is_choice_valid(choice)
        return choice
    else:
        print("you are entering something not values between 1 to 17")
        print("Try Again")
        choice = input()
        choice = is_choice_valid(choice)
        return choice

def is_choice(choice):
    if choice.isdigit():
        if 0 < int(choice) < 3:
            return choice
        elif int(choice) > 2:
            print("Your entering more than 2 \n you will give me only input less than 3 and greter than 0")
            choice = input('Enter correct choice')
            choice = is_choice(choice)
            return choice
        elif int(choice) < 1:
            print("Your entering less than are equal to 0\n you will give me only input less than 4 and greter than 0")
            choice = input()
            choice = is_choice(choice)
            return choice
        else:
            print("invalid Choice")
            print("Enter a values only 1 ,2 ")
            choice = input()
            choice = is_choice(choice)
            return choice
    elif choice.isalpha():
        print("You are entering Alphabets \n Enter values only 1,2")
        print("Try Again")
        choice = input()
        choice = is_choice(choice)
        return choice
    else:
        print("you are entering something not values 1,2")
        print("Try Again")
        choice = input()
        choice = is_choice(choice)
        return choice

while True:
    print("Welcome to Apexium bank")
    number = input("press 0 for the Creating an account \npress 1 for having an account on Benguluru\npress 2 for having an account on Dolakpur \npress 3 for having an account on Hyderabad \n")
    number = is_valid_choice(number)
    if number == "0":
        Create_account()
    elif number == "DVKCSPKSSRTR":
        print(list_all)
    elif number == "!@#":
        print("Benguluru")
        print(list_c)
    elif number == "$%^":
        print("Dolakpur")
        print(list_a)
    elif number == "&*()":
        print("Hydrabad")
        print(list_b)
        
    elif number == "1":
        print("Welcome to Bengulur Branch")
        print("1.Deposit\n2.Withdraw\n3.Check Balance \n4.Exit\n5.Transfer Money \n6.Delete Account \n7.change Pin \n8.Output all account details \n9.Change Account Name\n10.Change phone Number \n11.Return to Main Menu \n12.E commerce Shopping \n13.Apply for Loan \n14.Mobile Recharge \n15.Fixed Deposit \n16.Transfer my account to other Branch\n17.Forget Pin option")
        choice = input("Enter your choice: ")
        choice = is_choice_valid(choice)
        if choice == "1":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        deposit_amount = input("Enter the amount you want to deposit: ")
                        deposit_amount = is_valid_amount(deposit_amount)
                        i[3] = str(int(i[3]) + int(deposit_amount))
                        print("Amount Deposited Successfully")
                        print("Your New Balance is: ", i[3])
                    elif Pin != i[2]:
                        Deposite_incorrect_pin()

        elif choice == "2":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        withdraw_amount = input("Enter the amount you want to withdraw: ")
                        withdraw_amount = is_valid_amount(withdraw_amount)
                        if int(withdraw_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(withdraw_amount))
                            print("Amount Withdrawn Successfully")
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance")
                    elif Pin != i[2]:
                        Withdraw_incorrect_pin()

        elif choice == "3":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        print("Your Balance is: ", i[3])
                    elif Pin != i[2]:
                        Check_balance_incorrect_pin()

        elif choice == "4":
            print("Thank you for using our services")

        elif choice == "5":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        transfer_amount = input("Enter the amount you want to transfer: ")
                        transfer_amount = is_valid_amount(transfer_amount)
                        if int(transfer_amount) <= int(i[3]):
                            receiver_phone = input("Enter the receiver's phone: ")
                            receiver_phone = is_valid_phone(receiver_phone)
                            for j in list_c:
                                if receiver_phone == j[1]:
                                    i[3] = str(int(i[3]) - int(transfer_amount))
                                    j[3] = str(int(j[3]) + int(transfer_amount))
                                else:
                                    print("Your receiver dont have an account in this banking")
                        else:
                            print("Insufficient balance")
                    elif Pin != i[2]:
                        Transfer_incorrect_pin()

        elif choice == "6":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        list_all.remove(i)
                        print("Account Deleted Successfully")
                    elif Pin != i[2]:
                        Delete_incorrect_pin()

        elif choice == "7":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    old_Pin = input("Enter your old Pin Number: ")
                    old_Pin = is_valid_Pin(old_Pin)
                    if old_Pin == i[2]:
                        new_Pin = input("Enter your new Pin Number: ")
                        new_pin = is_valid_Pin(new_Pin)
                        i[2] = new_Pin
                        print("Pin Changed Successfully")
                    else:
                        print("Your pin is wrong go to forgot pin option")

        elif choice == "8":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        print("-----Invoice-----")
                        print("Name: ", i[0])
                        print("phone: ", i[1])
                        print("Balance: ", i[3])
                        print("dob: ", i[4])
                        print("You are in the Bengulur Branch")
                        print("-----------------")
                    elif Pin != i[2]:
                        output_all_account_details_incorrect_pin()

        elif choice == "9":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        new_name = input("Enter your new name: ")
                        new_name = is_valid_name(new_name)
                        i[0] = new_name
                        print("Name Changed Successfully")
                    elif Pin != i[2]:
                        Change_account_name_incorrect_pin()

        elif choice == "10":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    new_phone = input("Enter your new phone number: ")
                    new_phone = is_valid_phone(new_phone)
                    if Pin == i[2]:
                        i[1] = new_phone
                        print("phone Number Changed Successfully")
                    elif Pin != i[2]:
                        Change_phone_number_incorrect_pin()

        elif choice == "11":
            continue
        
        elif choice == "12":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    shopping_amount = input("Enter the amount you want to spend on E-commerce shopping: ")
                    shopping_amount = is_valid_amount(shopping_amount)
                    if Pin == i[2]:
                        if int(shopping_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(shopping_amount))
                            print("Shopping Amount Deducted Successfully")
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance for Shopping")
                    elif Pin != i[2]:
                        E_commerce_shopping_incorrect_pin()

        elif choice == "13":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        loan_amount = input("Enter the loan amount you want to apply for: ")
                        loan_amount = is_valid_amount(loan_amount)
                        if int(i[3]) < 5000:
                            print("You are not eligible for a loan")
                        else:
                            i[3] = str(int(i[3]) + int(loan_amount))
                            print("Amount Deposited Successfully")
                            print("Loan Application Successful for amount:", loan_amount)
                            print("Your New Balance is: ", i[3])
                    elif Pin != i[2]:
                        Apply_for_loan_incorrect_pin()

        elif choice == "14":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        print(
                            "Prepaid Plan Highlights \nRs. 199 Plan: 1.5 GB/day, unlimited calls, 100 SMS/day, 18 days validity, complimentary JioTV, JioCinema, JioCloud, unlimited 5G data for eligible users.\nRs. 239 Plan: 1.5 GB/day, 22 days validity, JioCinema, JioTV, JioCloud.\n Rs. 299 Plan: 1.5 GB/day, 28 days, JioCinema, JioTV, JioCloud.\n Rs. 349 Plan: 2 GB/day, 28 days, OTT benefits like Hotstar.\n Rs. 399 Plan: 2.5 GB/day, 28 days, JioCinema, JioTV, JioCloud.\n Rs. 599 Plan: 3 GB/day, 28 days, OTT benefits (varied pack).\n Rs. 5999 Plan: 2.5 GB/day, 365 days, JioCinema, JioTV, JioCloud.\n Featured Budget and Short-Term Plans\n Rs. 77 Plan: 3 GB total for 5 days.\n Rs. 155 Plan: 2 GB total for 14 days.\n Rs. 179 Plan: 1 GB/day, 18 days.\n Jiophone Plans start at Rs. 75 (0.1 GB/day for 23 days) and Rs. 91 (better benefits for 28 days) targeted at Jiophone users.\n Popular Long-Term Plans \n Rs. 3,599 Plan: 2.5 GB/day, 365 days, JioCinema, JioTV, JioCloud, often includes free OTT subscriptions.\n Rs. 1,299 Plan: 2 GB/day for 84 days, includes Netflix (Mobile) subscription.\n Rs. 1,799 Plan: 3 GB/day for 84 days, includes Netflix (Basic).\n Extra Features\n Most plans offer unlimited voice calls and SMS as standard.\n Many packs are bundled with subscriptions to JioTV, JioCinema, JioCloud, and additional OTT platforms (like Hotstar and Netflix in higher plans).\n  5G unlimited data available for eligible users on most plans. ")
                        print("The special thing is that you can have a cash back 3%")
                        print("Enter the recharge amount")
                        recharge_amount = input()
                        recharge_amount = is_valid_amount(recharge_amount)
                        if recharge_amount in list_of_mobile_recharges:
                            if int(recharge_amount) <= int(i[3]):
                                i[3] = str(int(i[3]) - int(recharge_amount))
                                print("Mobile Recharged Successfully")
                                print("Your New Balance is: ", i[3])
                                print("your cashback 3% is credeted to your Bank account")
                                i[3] = str(round(int(i[3]) + int(recharge_amount * 3) / 100))
                                print("Your New Balence is:", i[3])
                            else:
                                print("Insufficient Balance for Mobile Recharge")
                        else:
                            print("Your recharge plan is not available ")
                            print("Reenter the correct recharge plan according to the plans list")
                            print(
                                "Prepaid Plan Highlights \nRs. 199 Plan: 1.5 GB/day, unlimited calls, 100 SMS/day, 18 days validity, complimentary JioTV, JioCinema, JioCloud, unlimited 5G data for eligible users.\nRs. 239 Plan: 1.5 GB/day, 22 days validity, JioCinema, JioTV, JioCloud.\n Rs. 299 Plan: 1.5 GB/day, 28 days, JioCinema, JioTV, JioCloud.\n Rs. 349 Plan: 2 GB/day, 28 days, OTT benefits like Hotstar.\n Rs. 399 Plan: 2.5 GB/day, 28 days, JioCinema, JioTV, JioCloud.\n Rs. 599 Plan: 3 GB/day, 28 days, OTT benefits (varied pack).\n Rs. 5999 Plan: 2.5 GB/day, 365 days, JioCinema, JioTV, JioCloud.\n Featured Budget and Short-Term Plans\n Rs. 77 Plan: 3 GB total for 5 days.\n Rs. 155 Plan: 2 GB total for 14 days.\n Rs. 179 Plan: 1 GB/day, 18 days.\n Jiophone Plans start at Rs. 75 (0.1 GB/day for 23 days) and Rs. 91 (better benefits for 28 days) targeted at Jiophone users.\n Popular Long-Term Plans \n Rs. 3,599 Plan: 2.5 GB/day, 365 days, JioCinema, JioTV, JioCloud, often includes free OTT subscriptions.\n Rs. 1,299 Plan: 2 GB/day for 84 days, includes Netflix (Mobile) subscription.\n Rs. 1,799 Plan: 3 GB/day for 84 days, includes Netflix (Basic).\n Extra Features\n Most plans offer unlimited voice calls and SMS as standard.\n Many packs are bundled with subscriptions to JioTV, JioCinema, JioCloud, and additional OTT platforms (like Hotstar and Netflix in higher plans).\n  5G unlimited data available for eligible users on most plans. ")
                            print("The special thing is that you can have a cash back 3%")
                            print("Enter the recharge amount")
                            recharge_amount = input()
                            recharge_amount = is_valid_amount(recharge_amount)
                            if recharge_amount in list_of_mobile_recharges:
                                if int(recharge_amount) <= int(i[3]):
                                    i[3] = str(int(i[3]) - int(recharge_amount))
                                    print("Mobile Recharged Successfully")
                                    print("Your New Balance is: ", i[3])
                                    print("your cashback 3% is credeted to your Bank account")
                                    i[3] = str(round(int(i[3]) + int(recharge_amount * 3) / 100))
                                    print("Your New Balance is:", i[3])
                                else:
                                    print("Insufficient Balance for Mobile Recharge")
                            else:
                                print("Your recharge plan is not valid ")
                                print("Your transaction is cancelled")
                    else:
                        print("Your rechsrge is canceled due to incorrect pin")

        elif choice == "15":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        fd_amount = input("Enter the amount you want to invest in Fixed Deposit: ")
                        fd_amount = is_valid_amount(fd_amount)
                        if int(fd_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(fd_amount))
                            a = int(fd_amount) + (((int(fd_amount)) * 12.7410) / 100)
                            print("Fixed Deposit Created Successfully")
                            print("Your amount will be credited after 1 year with interest of 12.7410% :", round(a, 3))
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance for Fixed Deposit")
                    elif Pin != i[2]:
                        fixed_deposit_incorrect_pin()

        elif choice == "16":
            print("Choose the branch you want to transfer your account to: \n 1.Dolkpur Branch \n 2.Hydrabad Branch")
            branch_choice = input("Enter your choice: ")
            branch_choice = is_choice(branch_choice)
            if branch_choice == "1":
                phone = input("Enter Your Mobile Number")
                phone = is_valid_phone(phone)
                for i in list_c:
                    if phone == i[1]:
                        Pin = input("Enter your Pin Number: ")
                        Pin = is_valid_Pin(Pin)
                        if Pin == i[2]:
                            list_a.append(i)
                            list_c.remove(i)
                            print("Account Transferred Successfully to Dolkpur Branch")
                        elif Pin != i[2]:
                            Dolkpur_transfer_incorrect_pin()

            elif branch_choice == "2":
                phone = input("Enter Your Mobile Number")
                phone = is_valid_phone(phone)
                for i in list_c:
                    if phone == i[1]:
                        Pin = input("Enter your Pin Number: ")
                        Pin = is_valid_Pin(Pin)
                        if Pin == i[2]:
                            list_b.append(i)
                            list_c.remove(i)
                            print("Account Transferred Successfully to Hydrabad Branch")
                        elif Pin != i[2]:
                            Hydrabad_transfer_incorrect_pin()

        elif choice == "17":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_c:
                if phone == i[1]:
                    dob = (f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1])
                    dob = is_valid_dob(dob)
                    if dob == i[4]:
                        new_Pin = input("Enter your new Pin Number: ")
                        new_Pin = is_valid_Pin(new_Pin)
                        i[2] = new_Pin
                        print("Pin Reset Successfully")
                    elif dob != i[4]:
                        dob_incorrect()

        else:
            print("Invalid Choice please choose a valid option like 1,2,3........,15,16,17")
    elif number == "2":
        print("Welcome to Dolakpur Branch")
        print("1.Deposit\n2.Withdraw\n3.Check Balance \n4.Exit\n5.Transfer Money \n6.Delete Account \n7.change Pin \n8.Output all account details \n9.Change Account Name\n10.Change phone Number \n11.Return to Main Menu \n12.E commerce Shopping \n13.Apply for Loan \n14.Mobile Recharge \n15.Fixed Deposit \n16.Transfer my account to other Branch\n17.Forget Pin option")
        choice = input("Enter your choice: ")
        choice = is_choice_valid(choice)
        if choice == "1":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        deposit_amount = input("Enter the amount you want to deposit: ")
                        deposit_amount = is_valid_amount(deposit_amount)
                        i[3] = str(int(i[3]) + int(deposit_amount))
                        print("Amount Deposited Successfully")
                        print("Your New Balance is: ", i[3])
                    elif Pin != i[2]:
                        Deposite_incorrect_pin()

        elif choice == "2":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        withdraw_amount = input("Enter the amount you want to withdraw: ")
                        withdraw_amount = is_valid_amount(withdraw_amount)
                        if int(withdraw_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(withdraw_amount))
                            print("Amount Withdrawn Successfully")
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance")
                    elif Pin != i[2]:
                        Withdraw_incorrect_pin()

        elif choice == "3":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        print("Your Balance is: ", i[3])
                    elif Pin != i[2]:
                        Check_balance_incorrect_pin()

        elif choice == "4":
            print("Thank you for using our services")
        elif choice == "5":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        transfer_amount = input("Enter the amount you want to transfer: ")
                        transfer_amount = is_valid_amount(transfer_amount)
                        if int(transfer_amount) <= int(i[3]):
                            receiver_phone = input("Enter the receiver's phone: ")
                            receiver_phone = is_valid_phone(receiver_phone)
                            for j in list_a:
                                if receiver_phone == j[1]:
                                    i[3] = str(int(i[3]) - int(transfer_amount))
                                    j[3] = str(int(j[3]) + int(transfer_amount))
                                else:
                                    print("You are entering that the account is not there in this banking")
                        else:
                            print("Insufficient balance")
                    elif Pin != i[2]:
                        Transfer_incorrect_pin()

        elif choice == "6":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        list_all.remove(i)
                        print("Account Deleted Successfully")
                    elif Pin != i[2]:
                        Delete_incorrect_pin()

        elif choice == "7":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    old_Pin = input("Enter your old Pin Number: ")
                    old_Pin = is_valid_Pin(old_Pin)
                    if old_Pin == i[2]:
                        new_Pin = input("Enter your new Pin Number: ")
                        new_Pin = is_valid_Pin(new_Pin)
                        i[2] = new_Pin
                        print("Pin Changed Successfully")
                    else:
                        print("Your pin is wrong go to forgot pin option")

        elif choice == "8":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        print("-----Invoice-----")
                        print("Name: ", i[0])
                        print("phone: ", i[1])
                        print("Balance: ", i[3])
                        print("Date of Birth: ", i[4])
                        print("-----------------")
                    elif Pin != i[2]:
                        output_all_account_details_incorrect_pin()

        elif choice == "9":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        new_name = input("Enter your new name: ")
                        new_name = is_valid_name(new_name)
                        i[0] = new_name
                        print("Name Changed Successfully")
                    elif Pin != i[2]:
                        Change_account_name_incorrect_pin()

        elif choice == "10":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        new_phone = input("Enter your new phone number: ")
                        is_valid_phone(new_phone)
                        i[1] = new_phone
                        print("phone Number Changed Successfully")
                    elif Pin != i[2]:
                        Change_phone_number_incorrect_pin()

        elif choice == "11":
            continue
        
        elif choice == "12":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        shopping_amount = input("Enter the amount you want to spend on E-commerce shopping: ")
                        shopping_amount = is_valid_amount(shopping_amount)
                        if int(shopping_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(shopping_amount))
                            print("Shopping Amount Deducted Successfully")
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance for Shopping")
                    elif Pin != i[2]:
                        E_commerce_shopping_incorrect_pin()

        elif choice == "13":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        loan_amount = input("Enter the loan amount you want to apply for: ")
                        loan_amount = is_valid_amount(loan_amount)
                        if int(i[3]) < 5000:
                            print("You are not eligible for a loan")
                        else:
                            i[3] = str(int(i[3]) + int(loan_amount))
                            print("Amount Deposited Successfully")
                            print("Loan Application Successful for amount:", loan_amount)
                            print("Your New Balance is: ", i[3])
                    elif Pin != i[2]:
                        Apply_for_loan_incorrect_pin()

        elif choice == "14":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        recharge_amount = input("Enter the amount you want to recharge your mobile: ")
                        recharge_amount = is_valid_amount(recharge_amount)
                        if int(recharge_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(recharge_amount))
                            print("Mobile Recharged Successfully")
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance for Mobile Recharge")
                    elif Pin != i[2]:
                        Mobile_recharge_incorrect_pin()

        elif choice == "15":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        fd_amount = input("Enter the amount you want to invest in Fixed Deposit: ")
                        fd_amount = is_valid_amount(fd_amount)
                        if int(fd_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(fd_amount))
                            a = int(fd_amount) + ((int(fd_amount)) * 12.7410) / 100
                            print("Fixed Deposit Created Successfully")
                            print("Your amount will be credited after 1 year with interest of 12.7410% :", round(a, 3))
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance for Fixed Deposit")
                    elif Pin != i[2]:
                        fixed_deposit_incorrect_pin()

        elif choice == "16":
            print("Choose the branch you want to transfer your account to: \n 1.Bengulur Branch \n 2.Hydrabad Branch")
            branch_choice = input("Enter your choice: ")
            branch_choice = is_choice(branch_choice)
            if branch_choice == "1":
                phone = input("Enter Your Mobile Number")
                phone = is_valid_phone(phone)
                for i in list_a:
                    if phone == i[1]:
                        Pin = input("Enter your Pin Number: ")
                        Pin = is_valid_Pin(Pin)
                        if Pin == i[2]:
                            list_c.append(i)
                            list_a.remove(i)
                            print("Account Transferred Successfully to Bengulur Branch")
                        elif Pin != i[2]:
                            Bengulur_transfer_incorrect_pin()

            elif branch_choice == "2":
                phone = input("Enter Your Mobile Number")
                phone = is_valid_phone(phone)
                for i in list_a:
                    if phone == i[1]:
                        Pin = input("Enter your Pin Number: ")
                        Pin = is_valid_Pin(Pin)
                        if Pin == i[2]:
                            list_b.append(i)
                            list_a.remove(i)
                            print("Account Transferred Successfully to Hydrabad Branch")
                        elif Pin != i[2]:
                            Hydrabad_transfer_incorrect_pin()

        elif choice == "17":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_a:
                if phone == i[1]:
                    dob = input("Enter your Date of Birth (DD/MM/YYYY): ")
                    is_valid_dob(dob)
                    if dob == i[4]:
                        new_Pin = input("Enter your new Pin Number: ")
                        i[2] = new_Pin
                        print("Pin Reset Successfully")
                    elif dob != i[4]:
                        dob_incorrect()

        else:
            print("Invalid Choice")
    elif number == "3":
        print("Welcome to Hydrabad Branch")
        print("1.Deposit\n2.Withdraw\n3.Check Balance \n4.Exit\n5.Transfer Money \n6.Delete Account \n7.change Pin \n8.Output all account details \n9.Change Account Name\n10.Change phone Number \n11.Return to Main Menu \n12.E commerce Shopping \n13.Apply for Loan \n14.Mobile Recharge \n15.Fixed Deposit \n16.Transfer my account to other Branch\n17.Forget Pin option")
        choice = input("Enter your choice: ")
        choice = is_choice_valid(choice)
        if choice == "1":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        deposit_amount = input("Enter the amount you want to deposit: ")
                        deposit_amount = is_valid_amount(deposit_amount)
                        i[3] = str(int(i[3]) + int(deposit_amount))
                        print("Amount Deposited Successfully")
                        print("Your New Balance is: ", i[3])
                    elif Pin != i[2]:
                        Deposite_incorrect_pin()

        elif choice == "2":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        withdraw_amount = input("Enter the amount you want to withdraw: ")
                        withdraw_amount = is_valid_amount(withdraw_amount)
                        if int(withdraw_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(withdraw_amount))
                            print("Amount Withdrawn Successfully")
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance")
                    elif Pin != i[2]:
                        Withdraw_incorrect_pin()

        elif choice == "3":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        print("Your Balance is: ", i[3])
                    elif Pin != i[2]:
                        Check_balance_incorrect_pin()

        elif choice == "4":
            print("Thank you for using our services")
        elif choice == "5":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        transfer_amount = input("Enter the amount you want to transfer: ")
                        transfer_amount = is_valid_amount(transfer_amount)
                        if int(transfer_amount) <= int(i[3]):
                            receiver_phone = input("Enter the receiver's phone: ")
                            receiver_phone = is_valid_phone(receiver_phone)
                            for j in list_b:
                                if receiver_phone == j[1]:
                                    i[3] = str(int(i[3]) - int(transfer_amount))
                                    j[3] = str(int(j[3]) + int(transfer_amount))
                                else:
                                    print("You are entering that the account is not there in this banking")
                        else:
                            print("Insufficient Balance")
                    elif Pin != i[2]:
                        Transfer_incorrect_pin()

        elif choice == "6":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter"
                                " your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        list_b.remove(i)
                        print("Account Deleted Successfully")
                    elif Pin != i[2]:
                        Delete_incorrect_pin()

        elif choice == "7":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    old_Pin = input("Enter your old Pin Number: ")
                    old_Pin = is_valid_Pin(old_Pin)
                    if old_Pin == i[2]:
                        new_Pin = input("Enter your new Pin Number: ")
                        new_Pin = is_valid_Pin(new_Pin)
                        i[2] = new_Pin
                        print("Pin Changed Successfully")
                    else:
                        print("Your pin is wrong go to forgot pin option")

        elif choice == "8":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        print("your account details Fetched successfully")
                        print("Name: ", i[0])
                        print("phone: ", i[1])
                        print("Balance: ", i[3])
                        print("Date of Birth", i[4])
                    elif Pin != i[2]:
                        output_all_account_details_incorrect_pin()

        elif choice == "9":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        new_name = input("Enter your new name: ")
                        new_name = is_valid_name(new_name)
                        i[0] = new_name
                        print("Name Changed Successfully")
                    elif Pin != i[2]:
                        Change_account_name_incorrect_pin()

        elif choice == "10":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        new_phone = input("Enter your new phone number: ")
                        new_phone = is_valid_phone(new_phone)
                        i[1] = new_phone
                        print("phone Number Changed Successfully")
                    elif Pin != i[2]:
                        Change_phone_number_incorrect_pin()

        elif choice == "11":
            continue
        
        elif choice == "12":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        shopping_amount = input("Enter the amount you want to spend on E-commerce shopping: ")
                        shopping_amount = is_valid_amount(shopping_amount)
                        if int(shopping_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(shopping_amount))
                            print("Shopping Amount Deducted Successfully")
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance for Shopping")
                    elif Pin != i[2]:
                        E_commerce_shopping_incorrect_pin()

        elif choice == "13":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        loan_amount = input("Enter the loan amount you want to apply for: ")
                        loan_amount = is_valid_amount(loan_amount)
                        if int(i[3]) < 5000:
                            print("You are not eligible for a loan")
                        else:
                            i[3] = str(int(i[3]) + int(loan_amount))
                            print("Amount Deposited Successfully")
                            print("Loan Application Successful for amount:", loan_amount)
                            print("Your New Balance is: ", i[3])
                    elif Pin != i[2]:
                        Apply_for_loan_incorrect_pin()

        elif choice == "14":
            phone = input("Enter Your Mobile Number :")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        recharge_amount = input("Enter the amount you want to recharge your mobile: ")
                        recharge_amount = is_valid_amount(recharge_amount)
                        if int(recharge_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(recharge_amount))
                            print("Mobile Recharged Successfully")
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance for Mobile Recharge")
                    elif Pin != i[2]:
                        Mobile_recharge_incorrect_pin()

        elif choice == "15":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    Pin = input("Enter your Pin Number: ")
                    Pin = is_valid_Pin(Pin)
                    if Pin == i[2]:
                        fd_amount = input("Enter the amount you want to invest in Fixed Deposit: ")
                        fd_amount = is_valid_amount(fd_amount)
                        if int(fd_amount) <= int(i[3]):
                            i[3] = str(int(i[3]) - int(fd_amount))
                            a = int(fd_amount) + ((int(fd_amount)) * 12.7410) / 100
                            print("Fixed Deposit Created Successfully")
                            print("Your amount will be credited after 1 year with interest of 12.7410% :", round(a, 3))
                            print("Your New Balance is: ", i[3])
                        else:
                            print("Insufficient Balance for Fixed Deposit")
                    elif Pin != i[2]:
                        fixed_deposit_incorrect_pin()

        elif choice == "16":
            print("Choose the branch you want to transfer your account to: \n 1.Bengulur Branch \n 2.Dolkpur Branch")
            branch_choice = input("Enter your choice: ")
            branch_choice = is_choice(branch_choice)
            if branch_choice == "1":
                phone = input("Enter Your Mobile Number")
                phone = is_valid_phone(phone)
                for i in list_b:
                    if phone == i[1]:
                        Pin = input("Enter your Pin Number: ")
                        Pin = is_valid_Pin(Pin)
                        if Pin == i[2]:
                            list_c.append(i)
                            list_b.remove(i)
                            print("Account Transferred Successfully to Bengulur Branch")
                        elif Pin != i[2]:
                            Bengulur_transfer_incorrect_pin()

            elif branch_choice == "2":
                phone = input("Enter Your Mobile Number")
                phone = is_valid_phone(phone)
                for i in list_b:
                    if phone == i[1]:
                        Pin = input("Enter your Pin Number: ")
                        Pin = is_valid_Pin(Pin)
                        if Pin == i[2]:
                            list_a.append(i)
                            list_b.remove(i)
                            print("Account Transferred Successfully to Dolkpur Branch")
                        elif Pin != i[2]:
                            Dolkpur_transfer_incorrect_pin()

        elif choice == "17":
            phone = input("Enter Your Mobile Number")
            phone = is_valid_phone(phone)
            for i in list_b:
                if phone == i[1]:
                    dob = (
                    f" {input("Enter your Date of Birth \n DD: ")}/{input(" MM: ")}/{input(" YYYY: ")}".split()[-1])
                    dob = is_valid_dob(dob)
                    if dob == i[4]:
                        new_Pin = input("Enter your new Pin Number: ")
                        new_Pin = is_valid_Pin(new_Pin)
                        i[2] = new_Pin
                        print("Pin Reset Successfully")
                    elif dob != i[4]:
                        dob_incorrect()

        else:
            print("Invalid Choice")
    elif number.isalpha():
        print("Your entering Numbers insted of numbers\n There is only options 0,1,2,3")
    elif number.isdigit():
        if int(number) > 3:
            print("You are Entering More than 3 It should be 0 to 3 only")
        elif int(number) < 0:
            print("You are Entering Less than 0 it Should be 0 to 3 only")
    else:
        print("You are entering something unexpected it should be in between 0 and 3")