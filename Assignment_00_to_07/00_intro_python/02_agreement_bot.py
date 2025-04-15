def main():
    print("Hey there! I have a question for you.")

    animal = input("\033[1;3m \nWhat's your favorite animal _____ ? \033[0m")
    print(f"\n My favorite animal is also {animal}! \n")


if __name__ == '__main__':
    main()