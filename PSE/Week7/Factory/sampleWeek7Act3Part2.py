#In the first (Activity 3, Part 1), the factory must be modified 
#when a new shape is added. This one (Activity, part 2) does not require
#changing the factory. A concrete product class and include a it in the 
#register (or register it) is all we need to do.

from abc import ABC, abstractmethod

# 1) Abstract Product
class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        """Render the shape and return a description."""
        pass


# 2) Concrete Products
class Circle(Shape):
    def draw(self) -> str:
        return "Drawing a Circle"

class Square(Shape):
    def draw(self) -> str:
        return "Drawing a Square"

class Triangle(Shape):
    def draw(self) -> str:
        return "Drawing a Triangle"

class Octagon(Shape):
    def draw(self) -> str:
        return "Drawing an Octagon"

# 3) Factory
class ShapeFactory:
    _registry = {
        "circle": Circle,
        "square": Square,
        "triangle": Triangle,
        #"octagon": Octagon,
    }

    @classmethod
    def register(cls, name: str, shape_cls: type[Shape]) -> None:
        """Optionally register new shapes without modifying factory code."""
        if not issubclass(shape_cls, Shape):
            raise TypeError("Registered class must inherit from Shape")
        cls._registry[name.lower()] = shape_cls

    @classmethod
    def create(cls, shape_type: str) -> Shape:
        shape_cls = cls._registry.get(shape_type.lower())
        if shape_cls is None:
            raise ValueError(f"Unknown shape type: {shape_type!r}. "
                             f"Available: {', '.join(cls._registry)}")
        return shape_cls()


# 4) Client code (examples)
if __name__ == "__main__":
    factory = ShapeFactory

    circle = factory.create("circle")
    print(circle.draw())  

    square = factory.create("square")
    print(square.draw())  

    triangle = factory.create("triangle") #Triangle is already in _registry
    print(triangle.draw())  

    ShapeFactory.register("octagon", Octagon) #registered at runtime
    octagon = factory.create("octagon")       #Octagon not in _register
    print(octagon.draw())                     



