car_classes = ['AM General Hummer SUV 2000', 'Acura RL Sedan 2012', 'Acura TL Sedan 2012', 'Acura TL Type-S 2008', 'Acura TSX Sedan 2012', ...]  # Truncated for brevity

def map_car_to_category(car_name):
    lower_car_name = car_name.lower()
    if any(x in lower_car_name for x in ['suv', 'crossover', 'wagon']):
        return 'SUV'
    elif 'truck' in lower_car_name or 'pickup' in lower_car_name:
        return 'Truck'
    elif any(x in lower_car_name for x in ['sport', 'coupe', 'convertible', 'roadster', 'spyder', 'vantage']):
        return 'Sportscar'
    elif 'van' in lower_car_name or 'minivan' in lower_car_name:
        return 'Van'
    else:
        return 'Car'  # Default category if no other category fits

# Example of mapping each class
category_map = {car: map_car_to_category(car) for car in car_classes}

# Print the mapping
for car, category in category_map.items():
    print(f"{car}: {category}")
