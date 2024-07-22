import matplotlib.pyplot as plt
a = 0.1
b = -0.8
c = 20
temperature = 50.0
pressure = 900.0
humidity = 30.0
precipitation = a * temperature**2 + b * humidity + c
print(f"Precipitation: {precipitation}")
precipitation_values = [a * temp**2 + b * humidity + c for temp in temperature_range]
plt.plot(temperature_range, precipitation_values, marker='', linestyle='-')
plt.xlabel('Temperature')
plt.ylabel('Precipitation')
plt.title('Temperature and Precipitation')
plt.show()
