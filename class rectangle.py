class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def compute_area(self):
        return self.length * self.width


# Example usage:
rectangle1 = Rectangle(5, 4)
print("Area of rectangle1:", rectangle1.compute_area())  # Output: 20

rectangle2 = Rectangle(7, 3)
print("Area of rectangle2:", rectangle2.compute_area())  # Output: 21
