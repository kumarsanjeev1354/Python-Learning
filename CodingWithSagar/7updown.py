import random
#Generating Random Number
choice=random.randint(1,13)
#Asked the user to enter his/her choice
user_choice=(input("Enter the user choice="))
#User choice is compared with random number generated
if(user_choice=='above')and choice>7:
    print(f"You Won and your choice is {user_choice} and number choosed is {choice}")
elif(user_choice=='below') and choice<7:
    print(f"You Won and your choice is {user_choice} and number choosed is {choice}")
else:
    #In case of Random value entered
    print(f"You have entered invalid userchoice {user_choice} and number choosed is {choice}")