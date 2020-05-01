class Piece:
    
    def __init__(self,name,color,positionX,positionY,image):
        self.name = name
        self.color = color
        self.positionX = positionX
        self.positionY = positionY
        self.image = image
    def move_in_range(self,cord_str):
        if ord(cord_str[0:1]) > 72 or int(cord_str[1:]) > 8:
            return False
        else:
            return True

    def decode_move(self,cord_str):
        cordinate = dict()
        if self.move_in_range(cord_str):
            cordinate["x"] = ord(cord_str[0:1]) - 64
            cordinate["y"] = int(cord_str[1:]) - 8
            return cordinate
        else:
            cordinate["x"] = self.positionX
            cordinate["y"] = self.positionY
    