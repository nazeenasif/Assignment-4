import math
def main():

    ab : float = float(input("\033[1;3mEnter the length of AB: ")) 
    ac : float = float(input("Enter the length of AC: "))

    bc : float = math.sqrt(ab ** 2 + ac ** 2)
    print(f"\033[0mThe Lenth of the BC (hypotenuse) is: {bc}")

if __name__ == "__main__":
    main()    