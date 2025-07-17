import math
import time

# Display Header Info
def show_header():
    print("=" * 50)
    print("        SmartMath-CLI-Calculator")
    print("               by RedMark")
    print("=" * 50)
    time.sleep(1)

def show_menu():
    print("\nSelect Operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (x^y)")
    print("6. Integer Division (//)")
    print("7. Modulus (%)")
    print("8. Square Root (√x)")
    print("9. Logarithm (log base 10)")
    print("10. Exponential (e^x)")
    print("11. Factorial (x!)")
    print("12. Trigonometry (sin, cos, tan)")
    print("13. Show Scientific Constants")
    print("14. Solve Equation (Linear/Quadratic)")
    print("15. Unit Converter")
    print("0. Exit")

def show_constants():
    print("\nScientific Constants:")
    print(f"π (pi)        = {math.pi}")
    print(f"e             = {math.e}")
    print(f"φ (phi)       = {(1 + math.sqrt(5)) / 2:.10f}")
    print(f"Tau (τ = 2π)  = {2 * math.pi}")

def solve_equation():
    print("\nEquation Solver")
    eq_type = input("Linear (L) or Quadratic (Q)? ").lower()

    if eq_type == 'l':
        print("Equation format: ax + b = c")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        if a == 0:
            print("Not a valid linear equation.")
        else:
            x = (c - b) / a
            print(f"Solution: x = {x}")

    elif eq_type == 'q':
        print("Equation format: ax² + bx + c = 0")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        discriminant = b**2 - 4*a*c
        if discriminant > 0:
            x1 = (-b + math.sqrt(discriminant)) / (2*a)
            x2 = (-b - math.sqrt(discriminant)) / (2*a)
            print(f"Real Roots: x₁ = {x1}, x₂ = {x2}")
        elif discriminant == 0:
            x = -b / (2*a)
            print(f"One Real Root: x = {x}")
        else:
            real = -b / (2*a)
            imag = math.sqrt(-discriminant) / (2*a)
            print(f"Complex Roots: x₁ = {real}+{imag}i, x₂ = {real}-{imag}i")
    else:
        print("Invalid choice.")

def unit_converter():
    print("\nUnit Converter")
    print("1. Length")
    print("2. Temperature")
    print("3. Weight")
    choice = input("Choose category (1-3): ")

    if choice == "1":
        val = float(input("Enter length: "))
        unit = input("From unit (m/km/mi/in/ft): ").lower()
        to = input("To unit (m/km/mi/in/ft): ").lower()
        conversions = {
            "m": 1,
            "km": 1000,
            "mi": 1609.34,
            "in": 0.0254,
            "ft": 0.3048
        }
        if unit in conversions and to in conversions:
            result = val * conversions[unit] / conversions[to]
            print(f"{val} {unit} = {result:.4f} {to}")
        else:
            print("Invalid unit")

    elif choice == "2":
        temp = float(input("Enter temperature: "))
        unit = input("From (C/F/K): ").upper()
        to = input("To (C/F/K): ").upper()
        if unit == "C":
            if to == "F":
                print(f"Result: {(temp * 9/5) + 32} °F")
            elif to == "K":
                print(f"Result: {temp + 273.15} K")
        elif unit == "F":
            if to == "C":
                print(f"Result: {(temp - 32) * 5/9} °C")
            elif to == "K":
                print(f"Result: {(temp - 32) * 5/9 + 273.15} K")
        elif unit == "K":
            if to == "C":
                print(f"Result: {temp - 273.15} °C")
            elif to == "F":
                print(f"Result: {(temp - 273.15) * 9/5 + 32} °F")
        else:
            print("Invalid temperature unit")

    elif choice == "3":
        val = float(input("Enter weight: "))
        unit = input("From unit (kg/g/lb): ").lower()
        to = input("To unit (kg/g/lb): ").lower()
        conversions = {
            "kg": 1,
            "g": 0.001,
            "lb": 0.453592
        }
        if unit in conversions and to in conversions:
            result = val * conversions[unit] / conversions[to]
            print(f"{val} {unit} = {result:.4f} {to}")
        else:
            print("Invalid weight unit")

def calculator():
    show_header()  # Show title and author at startup
    while True:
        show_menu()
        choice = input("\nEnter your choice (0-15): ")

        if choice == "0":
            print("Exiting calculator. Goodbye!")
            break

        try:
            if choice in ["1", "2", "3", "4", "5", "6", "7"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
                if choice == "1":
                    print("Result:", a + b)
                elif choice == "2":
                    print("Result:", a - b)
                elif choice == "3":
                    print("Result:", a * b)
                elif choice == "4":
                    print("Result:", a / b)
                elif choice == "5":
                    print("Result:", a ** b)
                elif choice == "6":
                    print("Result:", a // b)
                elif choice == "7":
                    print("Result:", a % b)

            elif choice == "8":
                x = float(input("Enter number: "))
                print("Result:", math.sqrt(x))

            elif choice == "9":
                x = float(input("Enter number: "))
                print("Result:", math.log10(x))

            elif choice == "10":
                x = float(input("Enter number: "))
                print("Result:", math.exp(x))

            elif choice == "11":
                x = int(input("Enter integer: "))
                print("Result:", math.factorial(x))

            elif choice == "12":
                angle = float(input("Enter angle in degrees: "))
                rad = math.radians(angle)
                print("sin:", round(math.sin(rad), 4))
                print("cos:", round(math.cos(rad), 4))
                print("tan:", round(math.tan(rad), 4))

            elif choice == "13":
                show_constants()

            elif choice == "14":
                solve_equation()

            elif choice == "15":
                unit_converter()

            else:
                print("Invalid choice. Please try again.")

        except ValueError:
            print("Please enter valid numbers.")
        except ZeroDivisionError:
            print("Division by zero is not allowed.")
        except Exception as e:
            print("Error:", e)

# Run the calculator
calculator()
