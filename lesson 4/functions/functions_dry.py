# Defining the "Machine" once
def build_car(color, engine_size, top_speed):
    # The function creates and returns a dictionary (the car object)
    return {
        "color": color,
        "engine": engine_size,
        "speed": top_speed
    }

# Using the machine to build multiple cars quickly
car_1 = build_car("Black", "V6", 240)
car_2 = build_car("White", "Electric", 200)

print(f"Car 1 built: {car_1}")
print(f"Car 2 built: {car_2}")