class Figure:
    def __init__(self, color,movment, row ,col):
        self.row = row
        self.col = col
        self.color = color
        self.movment = movment

    def make_king(self):
        self.movment = "KING"
    def Demote(self):
        if self.color == "RED":
            self.movment = "Dawn"
        else:
            self.movment = "UP"
    def __str__(self):
        return f"{self.color} {self.movment} at ({self.row},{self.col})"
    