def categories_each(num_list):
    category_dict={}
    for items in num_list:
        cat = num_list[items]["Category"]
        exp = num_list[items]["Expense"] 

        if cat in category_dict:
            category_dict[cat] += exp
        else:
            category_dict[cat] = exp
    return category_dict

def how_many_category(cat):
    count = 0
    print("Expense Summary")
    print("_______________")
    for i,j in cat.items(): #     #pprint(category_dict, indent=4)
        count += 1
        print(f"{count}, {i} - {j}")


def add_the_expense(num_list):
    total = 0
    for items in num_list:
        single_expense = num_list[items]["Expense"]
        total += single_expense
    print(total)


def printing_total_expense(num_list):
    print(f"All Expense\n_____________")
    for items in num_list:
        ser = items
        exp = num_list[items]["Expense"]
        cat = num_list[items]["Category"]
        dt = num_list[items]["Date"]
        
        print(f"{ser}. Expense:{exp}\n  Category:{cat}\n  Date:{dt}")

def ask_user_categ(num_list):
    ask_user = input("Enter the category to search")
    print(f"Expenses in {ask_user} \n ------------------")
    for i in num_list:
        cat = num_list[i]["Category"]

        if ask_user == cat:
            cat = num_list[i]["Category"]
            exp = num_list[i]["Expense"]
            dat = num_list[i]["Date"]

            print(f"{i}. Expense:{exp}\n   Date:{dat}")


def add_item_to_dict(num_list):
    try:
        serial_no = int(input("Enter the serial number"))
    except ValueError:
        print("this is not a valid number !!!")
        return 
    

    try:
        expense = abs(int(input("Enter the expense")))
    except ValueError:
        print("this is not a valid number !!!")
        return 0

    if expense == 0:
        print("zero cannot be added")
        return 0
    else:
        category =input("Enter the category")
        date= input("Enter the date")
        num_list[serial_no] = {
            "Expense": expense,
            "Category": category,
            "Date": date
            }

def edit_option(num_list):
    print(num_list)
    try:
        choice = int(input("Enter serial number to edit: "))
    except ValueError:
        print("it is not a number !!!!")
        return 
    if choice in num_list:
         option = input("what do you want to edit-- enter 1 to edit category -- enter 2 to edit expense -- enter 3 to edit date ")
         match option:
            case"1":
                 user_edit = input("enter the category to edit")
                 num_list[choice]["Category"]=user_edit
                 #get_value = num_list[choice]["Category"]
                 #final_category = num_list[choice][user_edit
                 print(num_list)
            case"2":
                 try:
                     user_edit = abs(int(input("enter the expense")))
                 except ValueError:
                         print("it is not a number !!!!")
                         return 
                 if user_edit == 0:
                         print("zero cannot be added")
                         return 0
                 num_list[choice]["Expense"]=user_edit
                 print (num_list)
            case"3":
                 user_edit = input("enter the Date")
                 num_list[choice]["Date"]=user_edit
                 print (num_list)
            case _:  # <--- This is your DEFAULT case
                 print("it doesnt exit ")
    
    else:
        print("it doesn't exist")


def delete_fn(num_list): 
    try:
        deleted_value = int(input("enter the serial number to delete"))
    except ValueError:
        print("it is not a number !!!!")
        return 
    if deleted_value in num_list:
            num_list.pop(deleted_value)
    else:
        print("Serial number not found")
        print(num_list)              
