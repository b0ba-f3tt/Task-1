def predict_temperature_multiple_sets(time_values):
    a = 0.1 
    b = 0.5
    c = 10   
    print("Predicted temperatures for multiple time values:")
    for input_time in time_values:
        temperature = a * (input_time ** 2) + b * input_time + c
        print(f"Time: {input_time} hours, Predicted temperature: {temperature}°C")
multiple_time_values = [3, 6, 9, 12, 15]
predict_temperature_multiple_sets(multiple_time_values)
