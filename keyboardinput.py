import matplotlib.pyplot as plt
temperature = float(input("Enter temperature: "))
humidity = float(input("Enter humidity: "))
pressure = float(input("Enter pressure: "))
a = 0.01
b = -0.5
c = 25
precipitation = a * temperature**2 + b * humidity + c
print(f"Precipitation: {precipitation}")
temperature_range = range(0, 31)
precipitation_values = [a * temp**2 + b * humidity + c for temp in temperature_range]
plt.figure(figsize=(8, 6))
plt.plot(temperature_range, precipitation_values, marker='', linestyle='-')
plt.xlabel('Temperature')
plt.ylabel('Precipitation')
plt.title('Temperature and Precipitation')
plt.show()
