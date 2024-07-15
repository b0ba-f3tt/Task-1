def predict_temperature(time):
    a = 0.1  
    b = 0.5  
    c = 10   
    temperature = a * (time ** 2) + b * time + c
    return temperature
input_time = 5 
predicted_temperature = predict_temperature(input_time)
print(f"Predicted temperature after {input_time} hours: {predicted_temperature}°C")
