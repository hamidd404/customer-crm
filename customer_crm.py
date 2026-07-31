def get_user_choice():
    print("=============")
    choose_menu_number = input("choose: ")
    print("=============")
    return choose_menu_number

def wrong_choice():
    wrong = "You entered wrong number please try agian"
    return "wrong"

def get_customer_name():
    name = input("what is the customer name: ")
    return name

def get_customer_phone():
    phone = input("what is the customer's phone number: ")
    return phone

def get_customer_email():
    email = input("What is the customer's email: ")
    return email

def get_customer_city():
    city = input("What is the customer's city: ")
    return city

def get_customer_phone_check():
    while True:
        phone = get_customer_phone()
        if phone.isdigit() and len(phone) == 11:
            return phone
        print("Wrong format phone. Try again.")

def repetitive_phone_check():
    while True:
        phone = get_customer_phone_check()
        with open("customers.txt", 'r') as file:
            content = file.read()
            if phone in content:
                print("This phone number already exist.")
            else:
                return phone

def get_customer_email_check():
    while True:
        email = get_customer_email()
        if "@" in email:
            if "." in email:
                return email
        print("Wrong format email. Try again.")


def add_customer_info():
    with open("customers.txt", "a") as customer_file:
        name = get_customer_name()
        phone = repetitive_phone_check()
        email = get_customer_email_check()
        city = get_customer_city()
        information = f"name: {name}\nphone: {phone}\nemail: {email}\ncity: {city}\n--------------\n"
        customer_file.write(information)
        return "Customer added successfully"

def show_customers():
    with open("customers.txt") as customer_file:
        return customer_file.read()


def search_customers():
    search_name = input("give me the name you are looking for: ")
    new_search_list = []
    skip = False
    with open("customers.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith(f"name: {search_name}"):
            skip = True
            new_search_list.append(line)
            continue

        if skip:
            if line.strip() == "--------------":
                new_search_list.append(line)
                skip = False
                continue

            new_search_list.append(line)

    return new_search_list

def show_search_result():
    search_result_list = []
    search_result = search_customers()
    if search_result == []:
        return "THERE IS NOTHING"
    for i in search_result:
        new_search_customer = i.strip()
        search_result_list.append(new_search_customer)
        show_result = "\n".join(search_result_list)
    return (show_result)


def edit_customer():
    search = search_customers()
    if search == []:
        return "there is nothing as you searched"
    edit_item = input("what item do you want to edit: \n 1-name \n 2-phone \n 3-email \n 4-city \n choose the number: ")
    if edit_item == "1":
        old_value = search[0]
        edit_name = get_customer_name()
        new_value = f"name: {edit_name}\n"
    elif edit_item == "2":
        old_value = search[1]
        while True:
            edit_phone = get_customer_phone()
            if edit_phone.isdigit() and len(edit_phone) == 11:
                new_value = f"phone: {edit_phone}\n"
                break
            print(f"Wrong format phone. Try again.")
    elif edit_item == "3":
        old_value = search[2]
        while True:
            edit_email = get_customer_email()
            if "@" in edit_email:
                if "." in edit_email:
                    new_value = f"email: {edit_email}\n"
                    break
                print("Wrong email. Try again.")
            print("Wrong email. Try again.")
    elif edit_item == "4":
        old_value = search[3]
        edit_city = get_customer_city()
        new_value = f"city: {edit_city}\n"
    else:
        return ("you entered wrong number please try again")
    with open("customers.txt", 'r') as file:
        data = file.read()
        data = data.replace(old_value, new_value)
    with open('customers.txt', 'w') as file:
        file.write(data)

    return "Customer updated successfully."


def delete_customer():
    phone = input("Enter phone number to delete: ")
    with open("customers.txt", "r") as file:
        lines = file.readlines()
    new_lines = []
    skip = False
    for line in lines:
        if line.startswith(f"phone: {phone}"):
            if len(new_lines) > 0:
                new_lines.pop()
            skip = True
            continue
        if skip:
            if line.strip() == "--------------":
                skip = False
            continue
        new_lines.append(line)
    with open("customers.txt", "w") as file:
        file.writelines(new_lines)
    print("Customer removed successfully.")


def menu():
    menu_crm = """    =============
    menu
    =============
    1- New customer
    2- Customer list
    3- Delete customer
    4- Search and find
    5- edit customer
    6- Exit"""
    return menu_crm

while True:
    print(menu())
    choice = get_user_choice()
    if choice == "1":
        print(add_customer_info())
    elif choice == "2":
        print(show_customers())
    elif choice == "3":
        print(delete_customer())
    elif choice == "4":
        print(show_search_result())
    elif choice == "5":
        print(edit_customer())
    elif choice == "6":
        exit()
    else:
        print(wrong_choice())

