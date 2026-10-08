# celcius to fahrenheit
# Given a temperature in Celsius, convert it to Fahrenheit and return the converted temperature.

# Use the following formula:

# F = (C × 9/5) + 32

# Where:

# C is the temperature in Celsius.

# F is the temperature in Fahrenheit.

def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9//5)+32
    return fahrenheit
print(celsius_to_fahrenheit(0))