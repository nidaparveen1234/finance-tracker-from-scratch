num = {}

def enter_money():
            num_value = input("enter the serial no.") 
            expense=input("enter money")
            category=input("enter category")        
            date=input("enter date")
    
            num[num_value] = {
                "expense":expense,
                "category":category,
                "date":date
            }

print("Welcome to Finance Tracker")

while True:
    choice = input("do you want to continue")
    if choice == "yes":
         enter_money()
    else:
         print(num)
         break;

# this code has design flow which is when i am entering expense of 13
# the value is not getting stored cause i took 13 as my key so i need a 
#different key 
# i think it should be a number order so i can add it
# i used to have expense as key so i changed the key to serial no 
# and add expense and everything to dict 

#output
# Welcome to Finance Tracker
# do you want to continueyes
# enter the serial no.1
# enter money13
# enter categoryfood
# enter date13-8
# do you want to continueyes
# enter the serial no.2
# enter money30
# enter categoryfood
# enter date14-8
# do you want to continueno
# {'1': {'expense': '13', 'category': 'food', 'date': '13-8'}, '2': {'expense': '30', 'category': 'food', 'date': '14-8'}}
