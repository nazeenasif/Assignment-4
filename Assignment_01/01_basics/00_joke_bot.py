
JOKE : str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12.Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies:'because they had eggs'"
def main():

    user_input = input("what do you want?").lower()

    if user_input == "joke":
        print(JOKE)
    else:
        print("Sorry I only tell jokes")    

if __name__ == "__main__":
    main()        
