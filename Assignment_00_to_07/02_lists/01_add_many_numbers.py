def adding_numbers(numbers):
    total: int = 0
    for num in numbers:
        total += num
    return total

def main():
    numbers_list: list[int] = [1, 2, 3, 4, 5]
    result = adding_numbers(numbers_list)
    print("list: ", numbers_list)
    print("Sum of numbers: ", result)

if __name__ == "__main__":
    main()
