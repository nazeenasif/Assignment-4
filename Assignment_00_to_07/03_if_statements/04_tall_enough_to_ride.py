
MINIMUM_HEIGHT : int = 50

def main():

    user_height = float(input("\033[1;3mHow tall are you? \033[0m"))

    if user_height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()        