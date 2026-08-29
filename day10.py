#from pprint import pprint
num_list = {} 
print("Welcome to Finance Tracker") 
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
    

while(True): 
 
    choices = input("do you want to continue") 
    if choices == "yes": 
        add_item_to_dict() 
    else: 
        
        total = add_the_expense(num_list)  
        categories_each()
        ask_user_categ()
        #printing_category(total)
        #printing_total_expense(num_list)
        break; 
print("Thank you for using this") 

# output
#Welcome to Finance Tracker
# do you want to continueyes
# Enter the serial number1
# Enter the expense20
# Enter the categoryfood
# Enter the date12-3
# do you want to continueyes
# Enter the serial number2
# Enter the expense30
# Enter the categorycloth
# Enter the date3-3  
# do you want to continueno
# Enter the category to searchfood
# Expenses in food 
#  ------------------
# 1. Expense:20
#    Date:12-3
# Thank you for using this
