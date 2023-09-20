import random
computer_num=random.randrange(1,101)
while True:
    user_num=int(input("Enter the number between 1 to 100"))
    if user_num == computer_num:
        print("Congrats YOU WIN")
        break
    elif user_num < computer_num:
        print("Too small")
    else:
            print("Too large")
            
