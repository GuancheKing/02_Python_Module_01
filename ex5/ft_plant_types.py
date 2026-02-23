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

        def bloom(self) -> None:
            """
            Shows if the flower has bloomed
            """
            print(f"{self.name} is blooming beautifully!")

    class Tree(Plant):
        """
        A tree is a type of plant with an trunk_diameter and 
        ability to produce shade.
        """
        def __init__(self, name, height, age, trunk_diameter: int) -> None:
            super().__init__(name, height, age)
            self.trunk_diameter = trunk_diameter
        
        def produce_shade(self)
            """
            Estimate and display the tree's shade area.
            """
            shade_area = self.trunk_diameter * self.height * 3.14/100
            round_area = round(shade_area)
            print(f"{self.name} provides {round_area} square meters of shade")    