import json
from functions import categories_each
from functions import how_many_category
from functions import add_the_expense
from functions import printing_total_expense
from functions import ask_user_categ
from functions import add_item_to_dict
from functions import edit_option
from functions import delete_fn

num_list = {} 
def load_data(num_list):
    with open("data.json", "r") as file:
        loaded_dict = json.load(file)

        return {int(key): value for key, value in loaded_dict.items()}       
print("Welcome to Finance Tracker") 
num_list = load_data(num_list)

category_dict = {}



def json_saving(num_list):
   with open("data.json","w")as file:
      json.dump(num_list, file, indent=4)    


while(True): 
     
    choices = input("Menu\n-------\n1.Enter the Finances\n2.Edit Finances\n3.Delete Finances" \
    "\n4.Category\n5.Sum of Expense\n6.how many Category\n 7. the List of Expenses \nExit.To Exit and Save")
    match choices:
        case"1": 
            add_item_to_dict(num_list)
        case"2":
            edit_option(num_list)
        case"3":
            delete_fn(num_list)
        case"4":
            ask_user_categ(num_list)
        case"5":
            add_the_expense(num_list)
            
        case"6":
            cat_total=categories_each(num_list)
            how_many_category(cat_total) 
        case"7":
            printing_total_expense(num_list)
        case"exit":
            num_list.update(num_list)
            json_saving(num_list)
            print("Thank you for using this") 
            break;

# output
# Welcome to Finance Tracker
# Menu
# -------
# 1.Enter the Finances
# 2.Edit Finances
# 3.Delete Finances
# 4.Category
# 5.Sum of Expense
# 6.how many Category
#  7. the List of Expenses 
# Exit.To Exit and Save1
# Enter the serial number1
# Enter the expense0
# zero cannot be added
# Menu
# -------
# 1.Enter the Finances
# 2.Edit Finances
# 3.Delete Finances
# 4.Category
# 5.Sum of Expense
# 6.how many Category
#  7. the List of Expenses 
# Exit.To Exit and Save1
# Enter the serial number
# this is not a valid number !!!
# Menu
# -------
# 1.Enter the Finances
# 2.Edit Finances
# 3.Delete Finances
# 4.Category
# 5.Sum of Expense
# 6.how many Category
#  7. the List of Expenses 
# Exit.To Exit and Save1
# Enter the serial number2
# Enter the expense20
# Enter the categoryfood
# Enter the date1-dh
# Menu
# -------
# 1.Enter the Finances
# 2.Edit Finances
# 3.Delete Finances
# 4.Category
# 5.Sum of Expense
# 6.how many Category
#  7. the List of Expenses 
# Exit.To Exit and Save4
# Enter the category to searchfood
# Expenses in food 
#  ------------------
# 1. Expense:0
#    Date:13-4
# 2. Expense:20
#    Date:1-dh
# Menu
# -------
# 1.Enter the Finances
# 2.Edit Finances
# 3.Delete Finances
# 4.Category
# 5.Sum of Expense
# 6.how many Category
#  7. the List of Expenses 
# Exit.To Exit and Save6
# Expense Summary
# _______________
# 1, food - 20
# Menu
# -------
# 1.Enter the Finances
# 2.Edit Finances
# 3.Delete Finances
# 4.Category
# 5.Sum of Expense
# 6.how many Category
#  7. the List of Expenses 
# Exit.To Exit and Save3
# enter the serial number to delete1
# Menu
# -------
# 1.Enter the Finances
# 2.Edit Finances
# 3.Delete Finances
# 4.Category
# 5.Sum of Expense
# 6.how many Category
#  7. the List of Expenses 
# Exit.To Exit and Save