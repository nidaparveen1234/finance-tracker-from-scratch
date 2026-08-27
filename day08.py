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
   
while(True): 
 
    choices = input("do you want to continue") 
    if choices == "yes": 
        add_item_to_dict() 
    else: 
        
        total = add_the_expense(num_list)  
        categories_each()
        printing_category(total)
        break; 
print("Thank you for using this") 

#  output
# Welcome to Finance Tracker
# do you want to continueyes
# Enter the serial number1
# Enter the expense23
# Enter the categoryfood
# Enter the date23-4
# do you want to continueyes
# Enter the serial number2
# Enter the expense45
# Enter the categoryfood
# Enter the date23-4
# do you want to continueyes
# Enter the serial number3
# Enter the expense40
# Enter the categorycloths
# Enter the date2304 
# do you want to continueno
# Expense Summary
# _______________
# the total of expense =  108
# 1, food - 68
# 2, cloths - 40
# Thank you for using this
