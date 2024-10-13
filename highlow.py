import random
score = 0
count = 0
while count < 3:
    computer_number = random.randint(1 , 100)
    player_number = random.randint(1 , 100)
    print('player number is: ' , player_number)
    user_guess = input("Do u think your number is higher or lower than the computer's? higher\lower:")


    if user_guess == 'higher':
            if player_number > computer_number :
                print('u are correct' , computer_number)
                score += 1
            else:
                print('u are wrong' , computer_number)
    elif user_guess == 'lower':
            if  player_number < computer_number :
                print('u are the correct' , computer_number)
                score += 1
            else:
                print('U are wrong' , computer_number)
                
    else:
            print('Invalid synthax : Plz try higher or lower')            

    print(f'your score is now: {score}')
    print(f'\nGame over! your final score is:{score}')    



# player_number = random.randint(1 , 100)
# print(player_number)
# computer_number = random.randint(1 , 100)

# print(f"players number:{player_number}")
# print(f"computer number:{computer_number}")


# print(f"your number is:{player_number}")

# guess = input("do you think your number is higher or lower than the computer's?")
# print(f"your guessed:{guess}")

# welcome()