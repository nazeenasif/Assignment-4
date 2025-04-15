def main():
    print("\nHey! Now you can convert Fahrenheit to Celsius.\n")

    fahrenheit = float(input("\033[1;3m Enter temperature in fahrenheit: \033[0m"))
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    print(f"\nTemperature: {fahrenheit}F = {celsius}C\n")


if __name__ == '__main__':
    main()