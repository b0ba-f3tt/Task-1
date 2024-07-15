# Quadratic equation: temperature = a * time^2 + b * time + c

def predict_temperature_multiple_sets(time_values):
    a = 0.1  # Coefficient for time^2
    b = 0.5  # Coefficient for time
    c = 10   # Constant term

    print("Predicted temperatures for multiple time values:")
    for input_time in time_values:
        temperature = a * (input_time ** 2) + b * input_time + c
        print(f"Time: {input_time} hours, Predicted temperature: {temperature}°C")

# Example multiple sets of input time values (you can modify this list accordingly)
multiple_time_values = [3, 6, 9, 12, 15]

# Predict temperature for multiple sets of input values
predict_temperature_multiple_sets(multiple_time_values)
