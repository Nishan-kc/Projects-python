import string
import random


chars = " " + string.punctuation + string.digits +  string.ascii_letters 
chars = list(chars)
key = chars.copy()
random.shuffle(key)



#encryption 

plain_text = input("Enter text: ")
cipher_text = " "

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"before = {plain_text}")
print(f"before = {cipher_text}")