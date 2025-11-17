import random 

def guessing_game():
    answer = random.randint(0,100)
    
    while True:
        user_guess = input('what is your guess..!')

        if not user_guess.isdigit():
            print(f'Enter input number as a digit not decimal')
            break

        user_guess = int(user_guess)
        if user_guess == answer:
            print(f'Right the answer is {answer}')
            break

        elif user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        
        else:
            print(f'Your guess of {user_guess} is too High!')

#guessing_game()


def guessing_game_2():
    answer = random.randint(0,100)
    counter = 3 
    while counter > 0:
        user_guess = input(f'what is your guess..your have only {counter} chances left!')
        counter -= 1

        if not user_guess.isdigit():
            print(f'Enter input number as a digit not decimal')
            break

        user_guess = int(user_guess)
        if user_guess == answer:
            print(f'Right the answer is {answer}')
            break

        elif user_guess < answer:
            print(f'Your guess of {user_guess} is too low!')
        
        else:
            print(f'Your guess of {user_guess} is too High!')

guessing_game_2()