from Piece import Piece
import math

class Rook(Piece):

    def __init__(self,name,color,posLine,posColumn,image):
        Piece.__init__(self,name,color,posLine,posColumn,image)

    def move(self,new_position,board=[]):
        # if piece.piece_in_path(self.board,new_position):
        distanceLine = math.fabs(self.posLine - new_position["line"]) 
        distanceColumn = math.fabs(self.posColumn - new_position["column"]) 
        
        
        if (distanceLine > 0 and distanceColumn ==0):
            self.update_position(new_position)
        if (distanceLine == 0 and distanceColumn >0):
            self.update_position(new_position)
