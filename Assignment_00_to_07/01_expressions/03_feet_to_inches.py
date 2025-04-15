INCHES_PER_FOOT = 12
def main():

    feet : float = float(input("Enter feet measurement: "))

    inches : float = feet * INCHES_PER_FOOT

    print(f"{feet} feet is equal to {inches} inches.")
    


if __name__ == '__main__':
    main()