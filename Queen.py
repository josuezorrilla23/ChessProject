from Piece import Piece
import math

class Queen(Piece):

    def __init__(self,name,color,posLine,posColumn,image):
        Piece.__init__(self,name,color,posLine,posColumn,image)

    def move(self,new_position,board=[]):
        distanceLine = math.fabs(self.posLine - new_position["line"]) 
        distanceColumn = math.fabs(self.posColumn - new_position["column"]) 
        
        if (distanceLine == distanceColumn):
            self.update_position(new_position)
        elif (distanceLine > 0 and distanceColumn ==0):
            self.update_position(new_position)
        elif (distanceLine == 0 and distanceColumn >0):
            self.update_position(new_position)
        else:
            return False
