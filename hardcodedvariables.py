# Quadratic equation: temperature = a * time^2 + b * time + c

def predict_temperature(time):
    a = 0.1  # Coefficient for time^2
    b = 0.5  # Coefficient for time
    c = 10   # Constant term

    temperature = a * (time ** 2) + b * time + c
    return temperature

# Test the function with a specific time
input_time = 5  # Input time in hours
predicted_temperature = predict_temperature(input_time)
print(f"Predicted temperature after {input_time} hours: {predicted_temperature}°C")
