
def main():

    int1 : int = int(input("Please enter an integer to be divided: "))
    int2 : int = int(input("Please enter an integer to divide by: ") )  

    quotient : int = int1 // int2
    remainder : int = int1 % int2

    print(f"The result of this division is {quotient} with the remainder of {remainder}")

if __name__ == "__main__":
    main()    