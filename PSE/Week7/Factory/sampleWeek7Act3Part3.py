#Update code in Week7 - activity 3 (part2) with adding one more shape,
# "Triangle" to your code. Then explain the difference between using the
# Factory Design Pattern and not using it, to demonstrate the value of
# the pattern. Include notes on which lines you added to your code and 
# why. Share your GitHub link. 

# The use of Factory Design Pattern allows to add new shapes or modify  
# the existing ones without affecting the client code. Different classes
# can be treated as instances of a parent class. 

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
        "triangle": Triangle, #Added for activity 3 (part 3)
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
def main():
    factory = ShapeFactory

    circle = factory.create("circle")
    print(circle.draw())  

    square = factory.create("square")
    print(square.draw())  

    #ShapeFactory.register("triangle", Triangle) 
    triangle = factory.create("triangle")       #Added for activity 3 (part 3)
    print(triangle.draw())                      #Added for activity 3 (part 3)

    ShapeFactory.register("octagon", Octagon) #registered at runtime
    #octagon = factory.create("octagon")       #Octagon not in _register
    #print(octagon.draw())                     

if __name__ == "__main__":
    main()
