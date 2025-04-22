import random
def main():

    secret_num = random.randint(0,99)

    user_input = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

    while user_input != secret_num:
        if user_input < secret_num:
          print("Too low! Try again.")
        elif user_input > secret_num:
          print("Too high! Try again.")
          
        print()
        user_input = int(input("Enter a new guess: "))

    print("Congratulations! You've guessed the number!")

if __name__ == "__main__":
   main()       