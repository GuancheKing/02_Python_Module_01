class Plant:
    """
    Represents a plant with name, height and age as attributes
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cpd: int, days: int) -> int:
        """
        Increases the plant's height for a number of days

        cpd: centimeters per day
        return: growth in cm
        """
        old_height = self.height
        self.height += cpd * days
        return self.height - old_height

    def aging(self, days: int) -> None:
        """
        Increases the plant's age for a number of days

        days: nº of days
        """
        self.age += days


def get_info(plant: Plant, cpd: int, days: int) -> None:
    """
    Displays info of the plant after growing and aging
    """
    growth = plant.grow(cpd, days)
    plant.aging(days)
    print(f"{plant.name}: {plant.height}cm, {plant.age} days old")
    if growth > 0:
        print(f"Growth this week :+{growth}cm")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    # plant2 = Plant("Cucumber", 21, 7)
    print("=== Day 1 ===")
    get_info(plant1, 1, 0)
    # get_info(plant2, 3, 0)
    print("=== Day 7 ===")
    get_info(plant1, 1, 6)
    # get_info(plant2, 3, 6)
