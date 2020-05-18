class Player:
    
    def __init__(self,name,color,pieces):
        self.name = name
        self.color = color
        self.pieces = pieces

    def str__pieces(self):
        strp = ""
        for p in self.pieces:
            strp += p.__str__()
        return strp
    
    def __str__(self):
        return "Name: " + self.name + ", Color: " + self.color + " , Piezas: \n" + self.str__pieces()
