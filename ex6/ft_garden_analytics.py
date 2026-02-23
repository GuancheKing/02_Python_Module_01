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
    Represents a garden owned by a single person and stores its plants.
    """
    def __init__(self, owner: str) -> None:
        """
        Initialises an empty garden
        """
        self.owner = owner
        self.plants = []
        self.total_growth = 0

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
            self.total_growth += plant.grow()
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
    total_gardens_created = 0

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
            GardenManager.total_gardens_created += 1
        self.gardens[owner].add_plant(plant)

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """
        Create and return a sample GardenManager instance populated
        with multiple gardens and plants for demonstration/testing.
        """
        manager = cls()
        oak = Plant("Oak Tree", 100)
        rose = FloweringPlant("Rose", 25, "red")
        sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)
        lily = PrizeFlower("Lily", 45, "yellow", 92)
        manager.add_plant_to_garden("Alice", oak)
        manager.add_plant_to_garden("Alice", rose)
        manager.add_plant_to_garden("Alice", sunflower)
        manager.add_plant_to_garden("Bob", lily)
        return manager
    
    def report(self, owner: str) -> None:
        """
        Print a formatted report for a specific owner's garden,
        including the plant list and basic statistics.
        """
        garden = self.gardens[owner]

        print(f"\n=== {garden.owner}'s Garden Report ===")
        print("Plants in garden:")

        for line in garden.plant_info_lines():
            print(line)

        plants_added = len(garden.plants)
        growth = garden.total_growth
        print(f"Plants added: {plants_added}, Total growth: {growth}")
        regular, flowering, prize = (
            self.GardenStats.plant_types(garden)
        )
        print(f"Plant types: {regular} regular, {flowering} flowering"
              f", {prize} prize flowers")

    class GardenStats:
        """
        Nested helper to provide static methods for garden validation and stats
        """
        @staticmethod
        def validate_heights(gardens: dict[str, Garden]) -> bool:
            """
            Return True if all plants across all gardens
            have a non-negative height

            Args:
                gardens (dict[str, Garden]): Mapping of owner 
                names to Garden instances
            """
            for garden in gardens.values():
                for plant in garden.plants:
                    if plant.height < 0:
                        return False
            return True

        @staticmethod
        def plant_types(garden: Garden) -> tuple[int, int, int]:
            """
            Count plants by category in a single garden.

            Categories are mutually exclusive with priority:
            PrizeFlower > FloweringPlant > Plant.

            Args:
                garden (Garden): Garden instance to analyze.

            Returns:
                tuple[int, int, int]: (regular, flowering, prize)
            """
            prize = 0
            flowering = 0
            regular = 0
            for plant in garden.plants:
                if isinstance(plant, PrizeFlower):
                    prize += 1
                elif isinstance(plant, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return (regular, flowering, prize)


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    