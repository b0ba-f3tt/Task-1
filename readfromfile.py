# Quadratic equation: temperature = a * time^2 + b * time + c

def predict_temperature_from_file(filename):
    try:
        with open(filename, 'r') as file:
            coefficients = file.readline().strip().split()  # Read coefficients from the first line
            a, b, c = map(float, coefficients)  # Convert coefficients to floats

            print(f"Coefficients: a = {a}, b = {b}, c = {c}")

            print("Predicted temperatures:")
            for line in file:
                time = float(line.strip())
                temperature = a * (time ** 2) + b * time + c
                print(f"Time: {time} hours, Predicted temperature: {temperature}°C")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Invalid data in the file.")

# Read data from the input file and predict temperatures
predict_temperature_from_file('input_data.txt')

#inputs
#0.1 0.5 10
#3
#6
#9
