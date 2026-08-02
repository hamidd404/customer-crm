import json

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
        with open("customers.json", 'r') as file:
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


def add_customer():
    with open("customers.json", "r") as file:
        customers = json.load(file)

        customer = {
        "name": get_customer_name(),
        "phone": repetitive_phone_check(),
        "email": get_customer_email_check(),
        "city": get_customer_city()
        }

        customers.append(customer)

        with open("customers.json", "w") as file:
            json.dump(customers, file, indent=4, ensure_ascii=False)

        print("Customer added.")

def show_customers():
    with open("customers.json") as file:
        return file.read()


def search_customer():
    search_name = input("give me the name you are looking for: ")

    with open("customers.json", "r") as file:
        search_result_list = []
        data = json.load(file)
        for i in data:
            if i["name"] == search_name:
                search_result = f"name : {i["name"]}\nphone : {i["phone"]}\nemail : {i["email"]}\ncity : {i["city"]}\n"
                search_result_list.append(search_result)
                return search_result
        if search_result_list == []:
            return "Nothing"

def edit_customer():
    search = search_customer_with_number()
    if search == []:
        return "there is nothing as you searched"
    edit_item = input("what item do you want to edit: \n 1-name \n 2-phone \n 3-email \n 4-city \n choose the number: ")
    with open("customers.json", 'r') as file:
        data = json.load(file)
        for item in data:
            if item == search[0]:
                new_search = item
    if edit_item == "1":
        old_value = new_search["name"]
        edit_name = get_customer_name()
        new_search["name"] = new_search["name"].replace(old_value, edit_name)
    elif edit_item == "2":
        old_value = new_search["phone"]
        while True:
            edit_phone = get_customer_phone()
            if edit_phone.isdigit() and len(edit_phone) == 11:
                new_search["phone"] = new_search["phone"].replace(old_value, edit_phone)
                break
            print(f"Wrong format phone. Try again.")
    elif edit_item == "3":
        old_value = new_search["email"]
        while True:
            edit_email = get_customer_email()
            if "@" in edit_email:
                if "." in edit_email:
                    new_search["email"] = new_search["email"].replace(old_value, edit_email)
                    break
                print("Wrong email. Try again.")
            print("Wrong email. Try again.")
    elif edit_item == "4":
        old_value = new_search["city"]
        edit_city = get_customer_city()
        new_search["city"] = new_search["city"].replace(old_value, edit_city)
    else:
        return ("you entered wrong number please try again")
    with open("customers.json", 'w') as file:
        json.dump(data, file, indent=4)
    return "Customer updated successfully."


def search_customer_with_number():
    search_number = input("give me the customer's number you are looking for: ")

    with open("customers.json", "r") as file:   
        search_result_list = []
        data = json.load(file)
        for line in data:
            if line["phone"] == search_number:
                search_result = line
                search_result_list.append(search_result)
                return search_result_list
                break
        else:
            return []

def delete_customer():
    info_to_delete = search_customer_with_number()
    if info_to_delete == []:
        return "number has not found"
    else:
        with open("customers.json", "r") as file:
            data = json.load(file)
            item = info_to_delete[0]
            data.remove(item)
    with open("customers.json", "w") as file:
        json.dump(data, file, indent=4)
        return f"customer has removed successfully"



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
        print(add_customer())
    elif choice == "2":
        print(show_customers())
    elif choice == "3":
        print(delete_customer())
    elif choice == "4":
        print(search_customer())
    elif choice == "5":
        print(edit_customer())
    elif choice == "6":
        exit()
    else:
        print(wrong_choice())

