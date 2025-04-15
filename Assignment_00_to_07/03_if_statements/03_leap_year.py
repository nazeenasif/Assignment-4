def main():

    leap_year = int(input("Enter a year (To check whether it's a leap year or not): "))

    if leap_year % 4 == 0 :
        if leap_year % 100 == 0 :
            if leap_year % 400 == 0 :
                print("That's a leap year!")
            else:
                print("That's not a leap year!")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year!")
        
if __name__ == "__main__":
    main()                       