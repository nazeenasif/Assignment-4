def main():

    numbers : list[int] = [1, 2, 4, 6, 8]
    print("Original list: ", numbers)
    for i in range(len(numbers)):
        numbers[i] *= 2
     
    print("Doubled list: ", numbers) 


if __name__ == "__main__":
    main()    