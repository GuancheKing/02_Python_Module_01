class Plant:
    """
    Represents a plant with name, height and age as attributes
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


def print_plant_creation(plant: Plant) -> None:
    """
    Displays plants info in an organised format
    """
    print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")


if __name__ == "__main__":
    plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
        # Plant("Bamboo", 300, 300)
    ]
    print("=== Plant Factory Output ===")
    for plant_obj in plants:
        print_plant_creation(plant_obj)
    print()
    plants_len = len(plants)
    print(f"Total plants created: {plants_len}")
