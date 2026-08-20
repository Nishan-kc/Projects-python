import random
num = range(*(1,101))
is_running = True
number = random.choice(num)
while is_running:
 
    guess = int(input("Guess the number(1-100): "))

    if guess == number:
        print("correct guess !!")
        conti = input("Wanna play agian(y/n): ").lower()
        if(conti!="y"):
           is_running = False

       
    else:
        print("Incorrect ")
        if(number > guess):
            print(f"number is greater than {guess}")
        else:
             print(f"number is smaller than {guess}")



            