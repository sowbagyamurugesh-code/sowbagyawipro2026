from abc import ABC, abstractmethod
class shape(ABC):
    def display(self):
        print("normal method implemented")
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def area(self):
        print("area method implemented")

obj=Rectangle()
obj.display()
obj.area()

