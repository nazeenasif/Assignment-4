def main():
     
     side_1 = float(input("\033[1;3m\nWhat is the length of side 1? "))
     side_2 = float(input("\nWhat is the length of side 2? "))
     side_3 = float(input("\nWhat is the length of side 3? "))

     perimeter = side_1 + side_2 + side_3

     print(f"\033[0m\nThe perimeter of the triangle is: {perimeter}\n")

if __name__ == '__main__':
    main()    