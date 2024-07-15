# Quadratic equation: temperature = a * time^2 + b * time + c

def predict_temperature():
    try:
        a = float(input("Enter the coefficient for time^2 (a): "))
        b = float(input("Enter the coefficient for time (b): "))
        c = float(input("Enter the constant term (c): "))

        input_time = float(input("Enter time in hours: "))

        temperature = a * (input_time ** 2) + b * input_time + c
        print(f"Predicted temperature: {temperature}°C")
    except ValueError:
        print("Please enter valid numerical values.")

predict_temperature()
