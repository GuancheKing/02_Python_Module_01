class Plant:
    """
    Represents a Plant with name and height
    """
    def __init__(self, name: str, height: int) -> None:
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
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def info(self) -> str:
        """
        Returns the PrizeFlower info as a string
        """
        return (f"{super().info()}, Prize Points: {self.prize_points}")
