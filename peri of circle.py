import math

def calculate_perimeter(radius):
    """Calculate the perimeter (circumference) of a circle given its radius."""
    return 2 * math.pi * radius

def main():
    print("Perimeter (Circumference) of a Circle Calculator")
    try:
        radius = float(input("Enter the radius of the circle: "))
        if radius < 0:
            print("Radius cannot be negative.")
            return
        perimeter = calculate_perimeter(radius)
        print(f"The perimeter of the circle with radius {radius} is: {perimeter:.2f}")
    except ValueError:
        print("Please enter a valid number for the radius.")

if __name__ == "__main__":
    main()