class Plant:
    """
    Represents a Plant with name and height
    """
    def __init__(self, name: str, height: int) -> None:
        """
        Initialises a Plant with its name and height
        """
        self.name = name
        self.height = height

    def grow(self) -> int:
        """
        Grows the Plant height by 1 cm at a time and returns growth
        """
        growth = 1
        self.height += growth
        return growth

    def info(self) -> str:
        """
        Returns the Plant info as a string
        """
        return (f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    """
    A Plant with coloured flowers that can bloom
    """
    def __init__(self, name: str, height: int, color: str) -> None:
        """
        Initialises a Flowering Plant with its name, height, color and blooming state
        """
        super().__init__(name, height)
        self.color = color
        self._is_blooming = False

    def bloom(self) -> None:
        """
        Blooms the FloweringPlant
        """
        self._is_blooming = True

    def info(self) -> str:
        """
        Returns the FloweringPlant info as a string
        """
        if self._is_blooming:
            return (f"{super().info()}, {self.color} flowers (blooming)")
        else:
            return (f"{super().info()}, {self.color} flowers"
                    " (not blooming)")


class PrizeFlower(FloweringPlant):
    """
    A FloweringPlant that earns prize points
    """
    def __init__(
            self,
            name: str,
            height: int,
            color: str,
            prize_points: int
    ) -> None:
        """
        Initialises a Prize Flower with its Prize Points
        """
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info(self) -> str:
        """
        Returns the PrizeFlower info as a string
        """
        return (f"{super().info()}, Prize points: {self.prize_points}")

class Garden:
    """
    Represents a garden with different plant types and tracks stats
    """
    def __init__(self, owner: str) -> None:
        """
        Initialises an empty garden
        """
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: Plant) -> None:
        """
        Adds a plant to the Garden instance
        """
        self.plants.append(plant)
    
    def grow_all(self) -> int:
        """
        Grows all plants in the Garden and returns
        the total growth achieved
        """
        total_growth = 0
        for plant in self.plants:
            total_growth += plant.grow()
        return total_growth
    
    def plant_info_lines(self) -> list[str]:
        """
        Generate and return a list of plant information
        strings for all plants currently in the garden.
        """
        lines = []
        for p in self.plants:
            lines.append(p.info())
        return lines

class GardenManager:
    """
    Manages several gardens, shows reports and provides analytics tools
    """
    def __init__(self) -> None:
        """
        Initialises an empty garden manager
        """
        self.gardens = {}
    
    def add_garden(self, garden: Garden) -> None:
        """
        Registers an existing Garden instance in the manager
        """
        self.gardens[garden.owner] = garden

    def add_plant_to_garden(self, owner: str, plant: Plant) -> None:
        """
        Adds a plant to an owner's garden, creating the garden if needed.
        """
        if owner not in self.gardens:
            self.gardens[owner] = Garden(owner)
        self.gardens[owner].add_plant(plant)
        




    class GardenStats:
        """
        Nested helper to calculate garden statistics
        """
        @staticmethod
        def total_growth(plants) -> int:
            """
            Calculates total growth
            """
            for plant in plant