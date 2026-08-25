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
def printing_category():
    count = 0
    print("Expense Summary")
    print("_______________")
    for i,j in category_dict.items(): #     #pprint(category_dict, indent=4)
        count += 1
        print(f"{count}, {i} - {j}")

def add_the_expense(num_list):
    total = 0
    for items in num_list:
        single_expense = num_list[items]["Expense"]
        total += single_expense
    print(total)
   
while(True): 
 
    choices = input("do you want to continue") 
    if choices == "yes": 
        add_item_to_dict() 
    else: 
        #add_the_expense(num_list) 
        #print(num_list) 
        categories_each()
        printing_category()
        break; 
print("Thank you for using this") 
 
# the output 
# Welcome to Finance Tracker
# do you want to continueyes
# Enter the serial number1
# Enter the expense12
# Enter the categoryfood
# Enter the date12-9
# do you want to continueyes
# Enter the serial number2 
# Enter the expense12
# Enter the categoryfood
# Enter the date12-8
# do you want to continueyes
# Enter the serial number3   
# Enter the expense1000
# Enter the categorycloths
# Enter the date5-8
# do you want to continueno
# Expense Summary
# _______________
# 1, food - 24
# 2, cloths - 1000
# Thank you for using this
