class Person:
    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def getAge(self) -> int:
        return self.__age

    def ageUp(self) -> None:
        self.__age += 1

    def getFullname(self) -> str:
        return self.first_name + " " + self.last_name

    def printFullname(self) -> None:
        print(self.getFullname())
