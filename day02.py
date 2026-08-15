num = {}

for key in range(1):

    expense=input("enter money")
    category=input("enter category")        
    date=input("enter date")

    # num[expense] = category 
    # num[expense] = date 
    # here i am over writing my value turns out i am doing it 
    # wrong

    num[expense] = {
        "category" : category,
        "date" : date 
    }
    # this helps create dict inside dict 
    # it is helpfull so remember
# enter money12
# enter categoryfood
# enter date13/8
# {'12': {'category': 'food', 'date': '13/8'}}

print(num)
