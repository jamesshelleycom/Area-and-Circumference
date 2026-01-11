while True:
    try:
        radius = float(input("Enter the radius: "))
        break  # Exit loop if conversion succeeds
    except ValueError:
        print("Invalid input! Please enter a number.")

circumference = 2 * 3.14 * radius
area = 3.14 * radius ** 2

print("Circumference:", circumference)
print("Area:", area)
