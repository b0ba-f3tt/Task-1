def predict_temperature_single_set():
    a = 0.1 
    b = 0.5 
    c = 10  
    input_time = 5 
    temperature = a * (input_time ** 2) + b * input_time + c
    print(f"Predicted temperature after {input_time} hours: {temperature}°C")
predict_temperature_single_set()
