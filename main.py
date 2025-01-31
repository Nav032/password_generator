#Password Generator Project - #Order of characters randomised:

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password= ""
for letter in range(1,nr_letters+1):
  random_index_letters=random.randint(0,len(letters)-1)
  password+=letters[random_index_letters]

for symbol in range(1,nr_symbols+1):
  random_index_symbols=random.randint(0,len(symbols)-1)
  password+=symbols[random_index_symbols]

for number in range(1,nr_numbers+1):
  random_index_numbers=random.randint(0,len(numbers)-1)
  password+=numbers[random_index_numbers]

password_list=list(password)

random.shuffle(password_list)

randomized_password="".join(password_list)

print(f"Here is your password: {randomized_password}")
  
# instead of using random module to fetch random values from the lists, we can use random.choice() to do the same task.
