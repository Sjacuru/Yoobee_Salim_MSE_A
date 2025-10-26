import cmath
import math

def cartesian_to_polar():
    print("\n--- Cartesian → Polar ---")
    a = float(input("Enter the real part: "))
    b = float(input("Enter the imaginary part: "))
    z = complex(a, b)

    r, theta = cmath.polar(z)  # theta in radians
    print(f"Polar form: r = {r:.4f}, θ = {theta:.4f} radians ({math.degrees(theta):.2f}°)")

def polar_to_cartesian():
    print("\n--- Polar → Cartesian ---")
    r = float(input("Enter the magnitude r: "))
    theta_deg = float(input("Enter the angle θ in degrees: "))
    theta = math.radians(theta_deg)  # convert to radians

    z = cmath.rect(r, theta)  # returns complex number from polar coords
    print(f"Cartesian form: {z.real:.4f} + {z.imag:.4f}j")

def main():
    while True:
        print("\nChoose conversion type:")
        print("1 - Cartesian → Polar")
        print("2 - Polar → Cartesian")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            cartesian_to_polar()
        elif choice == "2":
            polar_to_cartesian()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
