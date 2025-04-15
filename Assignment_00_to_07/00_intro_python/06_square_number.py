def main():
    num : float= float(input("\033[1;3mEnter a number to see its square: "))
    print (str(num) + "\033[0m squared is " + str(num**2))

if __name__ == "__main__":
    main()    