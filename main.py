#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
dupilcated = []
password_result = []
password = ""
for letter in range(nr_letters):
  
  while True:
    check= random.choice(letters)
    if check in password_result:
        check= random.choice(letters)
    else:
      password_result.append(check)
      break

for symbol in range(nr_symbols):
  while True:
    check2= random.choice(symbols)
    if check2 in password_result:
        check2= random.choice(symbols)
    else:
      password_result.append(check2)
      break
  
for number in range(nr_numbers):
  while True:
    check3= random.choice(numbers)
    if check3 in password_result:
        check3= random.choice(numbers)
    else:
      password_result.append(check3)
      break
  
random.shuffle(password_result)
#final_pass = random.sample(password_result, len(password_result))# the Random sample reutrns a shuffled values from the list
for x in password_result:
  password += x
print(f"Your password is: {password}")


