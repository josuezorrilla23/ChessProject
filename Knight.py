from Piece import Piece
import math

class Knight(Piece):
    
    def __init__(self,name,color,posLine,posColumn,image):
        Piece.__init__(self,name,color,posLine,posColumn,image)

    def move(self,new_position,board=[]):
        distanceLine = math.fabs(self.posLine - new_position["line"]) 
        distanceColumn = math.fabs(self.posColumn - new_position["column"])

        if (distanceLine == 2 or distanceLine == 1) and (distanceColumn == 2 or distanceColumn == 1):
            if distanceColumn + distanceLine == 3:
                self.update_position(new_position)