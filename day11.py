import json

# Fix 1: Pass the list into the function so it is defined
def json_saving(num_list):
    with open("data.json", "w") as file:
         # Fix 2: Use json.dump() without the 's' for saving to a file
         json.dump(num_list, file, indent=4) 

# Example data to test the function
my_numbers = [1, 2, 3, 4, 5]

# Call the function to save the data
json_saving(my_numbers)

# Load the data back
with open("data.json", "r") as file:
     loaded_dict = json.load(file)

print(loaded_dict)  # Output: [1, 2, 3, 4, 5]


# mine  
# import json
# >> 
# >> def json_saving():
# >>     with open("data.json","w") as file:
# >>          json.dump(my_numbers, file, indent =4) 
# >> 
# >> 
# >> 
# >> my_numbers = [1, 2, 3, 4, 5]
# >> 
# >> json_saving(my_numbers)
# >> 
# >> with open("data.json","r") as file:
# >>      loaded_dict = json.load(file)
# >> 
# >> print(loaded_dict)
