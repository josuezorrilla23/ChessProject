from Piece import Piece
import math
class Pawn(Piece):

    def __init__(self,name,color,posLine,posColumn,image):
        Piece.__init__(self,name,color,posLine,posColumn,image)
        self.moved = False

    def move(self,new_position,board=[]):

        distanceLine = self.posLine - new_position["line"] 
        distanceColumn = self.posColumn - new_position["column"] 

        direction = 0
        if self.color == "White":
            direction = 1
        elif self.color == "Black":
            direction = -1

        if (distanceColumn == 0):
            if(distanceLine == (2 * direction) and self.moved == False):
                self.update_position(new_position)
            elif distanceLine == (1 * direction):
                self.update_position(new_position)
            else:
                return False
        elif (issubclass(type(board[new_position["line"]][new_position["column"]]),Piece) and 
            distanceLine == (1 * direction) and distanceColumn == (1 * direction)):
            if (board[new_position["line"]][new_position["column"]].color != self.color):
                self.update_position(new_position)
            else:
                return False
        else:
            return False
