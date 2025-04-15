import random


NumSides : int = 6
def main():

    die1 : int = random.randint(1, NumSides)
    die2 : int = random.randint(1, NumSides)

    total : int = die1 + die2

    print(f"Dice have {NumSides} sides each.")
    print(f"First die : {die1}")
    print(f"Second die : {die2}")
    print(f"Total of two dice : {total}")


if __name__ == "__main__":
    main()    