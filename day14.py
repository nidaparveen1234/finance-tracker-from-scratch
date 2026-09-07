
import json
num_list = {} 
def load_data(num_list):
    with open("data.json","r")as file:
        loaded_dict = json.load(file)
        return loaded_dict
        
print("Welcome to Finance Tracker") 
num_list = load_data(num_list)

category_dict = {}


def add_item_to_dict():
    serial_no = int(input("Enter the serial number"))
    expense = int(input("Enter the expense"))
    category =input("Enter the category")
    date= input("Enter the date")

    num_list[serial_no] = {
        "Expense": expense,
        "Category": category,
        "Date": date
    }


def categories_each():
    for items in num_list:
        cat = num_list[items]["Category"]
        exp = num_list[items]["Expense"] 

        if cat in category_dict:
            category_dict[cat] += exp
        else:
            category_dict[cat] = exp

def printing_category(total):
    count = 0
    print("Expense Summary")
    print("_______________")
    print("the total of expense = ",total)
    for i,j in category_dict.items(): #     #pprint(category_dict, indent=4)
        count += 1
        print(f"{count}, {i} - {j}")

def add_the_expense(num_list):
    total = 0
    for items in num_list:
        single_expense = num_list[items]["Expense"]
        total += single_expense
    return total

def printing_total_expense(num_list):
    print(f"All Expense\n_____________")
    for items in num_list:
        ser = items
        exp = num_list[items]["Expense"]
        cat = num_list[items]["Category"]
        dt = num_list[items]["Date"]
        
        print(f"{ser}. Expense:{exp}\n  Category:{cat}\n  Date:{dt}")

def ask_user_categ():
    ask_user = input("Enter the category to search")
    print(f"Expenses in {ask_user} \n ------------------")
    for i in num_list:
        cat = num_list[i]["Category"]

        if ask_user == cat:
            cat = num_list[i]["Category"]
            exp = num_list[i]["Expense"]
            dat = num_list[i]["Date"]

            print(f"{i}. Expense:{exp}\n   Date:{dat}")

def edit_option():
    choice = input("Enter serial number to edit: ")
    for items in nu

def json_saving(num_list):
   with open("data.json","w")as file:
      json.dump(num_list, file, indent=4)    


while(True): 
     
    choices = input("Menu \ndo you want to continue : say yes  \nif you want to edit :say 1 \n if you want to finishes or close:say 2 ")
    match choices:
        case"yes": 
            add_item_to_dict()
            num_list.update(num_list)

        case"1":
            edit_option()
        case"2":
            #total = add_the_expense(num_list) 
            print(num_list) 
            #add_the_expense(num_list)
            json_saving(num_list)
            # categories_each()
            #ask_user_categ()
            #printing_category(total)
                    
            #printing_total_expense(num_list)

        case"exit":
            print("Thank you for using this") 
            break;



