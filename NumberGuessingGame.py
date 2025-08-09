import random
from colorama import Fore, Style, init
init(autoreset=True)
min=int(input("Enter the minimum number: "))
max=int(input("Enter the maximum number: "))
correctno=random.randint(min,max)
N=0
while N<5:
    a=int(input(f"Guess the number between {min} to {max}: "))
    if a>correctno:
        print("Too high! Try again.")
        N+=1
    elif correctno>a:
        print("Too low!Try again.")
        N+=1
    elif correctno==a:
        print(Fore.GREEN + f"Congratulations! You guessed the number in {N} attempts.")
        break
    else:
        print("Please enter a valid number")
        N+=1
else:
    print(f"Game end! The correct number is {correctno}")
    
