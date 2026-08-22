num_list = {}
print("Welcome to Finance Tracker")
category_dict = {}

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

def categories_each():
     for items in num_list:
        cat = num_list[items]["Category"]
        expense = num_list[items]["Expense"]
        if cat in category_dict:
             category_dict[cat] += expense
        else:
             category_dict[cat] = expense
     print("the category expense are", category_dict)
     
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
        #add_the_expense(num_list)
        categories_each()
        break;
print("Thank you for using this")

# output 
# Welcome to Finance Tracker
# do you want to continueyes
# Enter the serial number1
# Enter the expense20
# Enter the categoryfood
# Enter the date13-4
# do you want to continueyes
# Enter the serial number2
# Enter the expense20
# Enter the categoryfood
# Enter the date234
# do you want to continueyes
# Enter the serial number3
# Enter the expense40
# Enter the categorycloths
# Enter the date123
# do you want to continueno
# the category expense are {'food': 40, 'cloths': 40}
# Thank you for using this
