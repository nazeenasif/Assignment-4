import random
def main():

    secret_number = random.randint(1, 99)

    print("I am thinking of a number between 0 and 99...")
    user_input = int(input("Guess a number: "))

    while user_input != secret_number:
        if user_input < secret_number:
            print("Too low!")
        else:
            print("Too high!")

        print()
        user_input = int(input("Enter a new guess: "))

    print("Congrats! The number was: " + str(secret_number))
        
if __name__ == "__main__":
    main()


