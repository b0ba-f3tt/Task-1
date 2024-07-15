# Quadratic equation: temperature = a * time^2 + b * time + c

def predict_temperature_single_set():
    a = 0.1  # Coefficient for time^2
    b = 0.5  # Coefficient for time
    c = 10   # Constant term

    input_time = 5  # Single input time in hours (example)
    
    temperature = a * (input_time ** 2) + b * input_time + c
    print(f"Predicted temperature after {input_time} hours: {temperature}°C")

# Predict temperature for a single set of input values
predict_temperature_single_set()
