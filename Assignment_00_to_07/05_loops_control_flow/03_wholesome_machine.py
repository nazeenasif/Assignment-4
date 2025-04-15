AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main ():

    print("Please type the following affirmation: " + AFFIRMATION)

    user_input = input()

    while user_input != AFFIRMATION:
        print("Incorrect. Please try again.")

        print("Please type the following affirmation: " + AFFIRMATION)
        user_input = input()

    print("That's right! :)")    

if __name__ == "__main__":
    main()