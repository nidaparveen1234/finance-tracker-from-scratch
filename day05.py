num_list = {}
print("Welcome to Finance Tracker")


def add_item_to_dict():
    serial_no = int(input("Enter the serial number"))
    expense = int(input("Enter the expense"))
    category =input("Enter the category")
    date= input("Enter the date")

    num_list[serial_no] = {
        "Expense":expense,
        "Category":category,
        "Date":date
    }

def add_the_expense(num_list):
        total = 0
        for items in num_list:# here i tried using "i" but turns out i cant do it cause python consider it a actual item in list not index soo here it was finding 
            single_expense = num_list[items]["Expense"]# dict so after turning into items it work
            total += single_expense
        print("The total expense is ",total)
             
while(True):

    choices = input("do you want to continue")
    if choices == "yes":
        add_item_to_dict()
    else:
        add_the_expense(num_list)
        print(num_list)
        break;
print("Thank you for using this")

# the output
# Welcome to Finance Tracker
# do you want to continueyes
# Enter the serial number1
# Enter the expense12
# Enter the categoryfood
# Enter the date13/8
# do you want to continueyes
# Enter the serial number2
# Enter the expense30
# Enter the categoryfood
# Enter the date14/8
# do you want to continueno
# The total expense is  42
# {1: {'Expense': 12, 'Category': 'food', 'Date': '13/8'}, 2: {'Expense': 30, 'Category': 'food', 'Date': '14/8'}}
# Thank you for using this
