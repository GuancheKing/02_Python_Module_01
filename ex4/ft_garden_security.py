class SecurePlant:
    """
    Represents a plant securily validating height and age before updating
    their attributes

    name: (str) the name of the new plant
    height: (int) the height of the plant in cm (validated)
    age: (int) the age of the plant in days (validated)
    """
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.__height = 0
        self.__age = 0
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def get_height(self) -> int:
        """
        Returns the height of the plant in cm
        """
        return self.__height

    def set_height(self, new_height: int) -> None:
        """
        Sets the new height of the plant after validating. Error if invalid

        new_height: (int) the new height to be assigned
        """
        if new_height >= 0:
            self.__height = new_height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print("Invalid operation attempted:"
                  f" height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected\n")

    def get_age(self) -> int:
        """
        Returns the age of the plant in days
        """
        return self.__age

    def set_age(self, new_age: int) -> None:
        """
        Sets the new age of the plant after validating. Error if invalid

        new_age: (int) the new age to be assigned
        """
        if new_age >= 0:
            self.__age = new_age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print("Invalid operation attempted: age"
                  f" {new_age} days [REJECTED]")
            print("Security: Negative age rejected\n")

    def current_info(self) -> None:
        """
        Shows plant info as expected
        """
        print(f"Current plant : {self.name} ({self.__height}cm,"
              f" {self.__age} days)")


if __name__ == "__main__":
    print("=== Garden Security System ===")
    plant1 = SecurePlant("Rose", 25, 30)
    print()
    plant1.set_height(-5)
    plant1.current_info()
