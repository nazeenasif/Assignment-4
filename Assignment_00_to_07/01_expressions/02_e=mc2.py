c : int = 299792458 

def main():
    mass : float = float(input("Enter kilos of mass: "))

    energy : float = mass * (c ** 2)

    print("e = m * C^2...")
    print(f"m = {mass}Kg")
    print(f"C = " + str(c) + "m/s")

    print(f"Energy is {energy} joules")


if __name__ == '__main__':
    main()    