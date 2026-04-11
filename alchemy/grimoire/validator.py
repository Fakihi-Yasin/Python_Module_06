def validate_ingredients(ingredients: str) -> str:
    elements = ["fire", "water", "earth", "air"]
    for element in elements:
        if element in ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
