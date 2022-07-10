class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        w = self.width
        h = self.height
        if w > 50 or h > 50:
            return "Too big for picture."
        string = (int(w) * "*" + "\n") * int(h)
        return string

    def get_amount_inside(self, other):
        return int(self.get_area()) // int(other.get_area())


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"