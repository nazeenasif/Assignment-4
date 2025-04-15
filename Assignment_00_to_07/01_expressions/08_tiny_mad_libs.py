

def main():
    print("Hey there! You have to answer the following questions to make a fun sentence.")

    adjective :str = input("Enter an adjective: ")
    noun : str = input("Enter a noun: ")
    verb : str = input("Enter a verb: ")

    sentence = f"The {adjective} {noun} {verb} into a job interview wearing sunglasses! "

    print(sentence)

if __name__ == "__main__":
    main()
