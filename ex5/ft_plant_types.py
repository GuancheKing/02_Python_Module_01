class Plant:
    """
    Represents a plant with name, height and age as attributes
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """
    A flower is a type of plant with an additional color attribute and
    capacity to bloom.
    """
    def __init__(self, name, height, age, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        """
        Confirms if the flower has bloomed
        """
        self._is_blooming = True

    def show_info(self) -> None:
        """
        Shows required info for Flower
        """
        print(f"{self.name} (Flower): {self.height}cm, {self.age} days, "
              f"{self.color} color")
        self.bloom()
        if self._is_blooming:
            print(f"{self.name} is blooming beautifully!")
        print()


class Tree(Plant):
    """
    A tree is a type of plant with an trunk_diameter and
    ability to produce shade.
    """
    def __init__(self, name, height, age, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> int:
        """
        Estimate and display the tree's shade area.
        """
        shade_area = self.trunk_diameter * self.height * 3.14/1000
        round_area = round(shade_area)
        return round_area

    def show_info(self) -> None:
        """
        Shows required info for Tree
        """
        print(f"{self.name} (Tree): {self.height}cm, {self.age} days, "
              f"{self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.produce_shade()} square meters of"
              " shade")
        print()


class Vegetable(Plant):
    """
    A vegetable is a plant with a harvest season and nutritional value
    """
    def __init__(self, name, height, age, harvest_season: str,
                 nutritional_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_info(self) -> None:
        """
        Shows required info for Vegetable
        """
        print(f"{self.name} (Vegetable): {self.height}cm, {self.age} days, "
              f"{self.harvest_season} harvest")
        print(f"{self.name} is rich in: {self.nutritional_value}")
        print()


if __name__ == "__main__":
    flower1 = Flower("Rose", 25, 30, "red")
    # flower2 = Flower("Sunflower", 18, 38, "yellow")
    tree1 = Tree("Oak", 500, 1825, 50)
    # tree2 = Tree("Lemon Tree", 220, 2250, 25)
    veg1 = Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    # veg2 = Vegetable("Aubergine", 23, 75, "summer", "potassium")
    print("=== Garden Plant Types ===")
    print()
    # plants = [flower1, flower2, tree1, tree2, veg1, veg2]
    plants = [flower1, tree1, veg1]
    for plant in plants:
        plant.show_info()
