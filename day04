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

def add_the_expense():
        for items_0 in num_list:
             if "expense" in items_0:
                  total+= items_0["expense"]

while(True):

    choices = input("do you want to continue")
    if choices == "yes":
        add_item_to_dict()
        add_the_expense()
    else:
        print(num_list)
        break;
print("Thank you for using this")
