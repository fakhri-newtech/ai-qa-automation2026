# We built a basic car, but forgot to add the 'warranty' data
basic_car = {"color": "Blue", "engine": "V4"} 

try:
    # Attempting to read a key that doesn't exist will crash Python normally
    print(basic_car["warranty_years"])
except KeyError as e:
    # Catching the crash gracefully
    print(f"the key error was in the key {e}")


print("The assembly line is still running! Moving to the next car...")