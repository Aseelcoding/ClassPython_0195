class Rectangle:
    def __init__(self, length, width):
        if length == 0 or width == 0:
            raise ValueError("Length and width cannot be 0")
        self.length = length
        self.width = width

    def circumference(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"rectangle, {self.length} cm long, and {self.width} cm wide"


if __name__ == "__main__":
    rect = Rectangle(3, 2)
    print(rect)
    print("Circumference:", rect.circumference())
    print("Area:", rect.area())
