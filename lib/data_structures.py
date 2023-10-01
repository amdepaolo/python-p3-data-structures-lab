spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    spicy_names = [food.get("name") for food in spicy_foods]
    return spicy_names

def get_spiciest_foods(spicy_foods):
    spiciest = [food for food in spicy_foods if food.get("heat_level") > 5]
    return spiciest


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        name = food.get('name')
        cuisine = food.get('cuisine')
        peppers = "🌶" * food.get('heat_level')
        print(f"{name} ({cuisine}) | Heat Level: {peppers}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food.get("cuisine") == cuisine:
            return food
        

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)

def get_average_heat_level(spicy_foods):
    heat_list = [food.get("heat_level") for food in spicy_foods]
    heat_sum = 0
    for heat_int in heat_list:
        heat_sum += heat_int
    return heat_sum / len(heat_list)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
