from Piece import Piece
import math
class Pawn(Piece):

    def __init__(self,name,color,posLine,posColumn,image):
        Piece.__init__(self,name,color,posLine,posColumn,image)
        self.moved = False

    def move(self,new_position,board=[]):
        #new_position = self.decode_cordinate(cord_str)
        distanceLine = self.posLine - new_position["line"] 
        distanceColumn = self.posColumn - new_position["column"] 
        
        #Check the color of the piece
        direction = 0
        if self.color == "White":
            direction = 1
        elif self.color == "Black":
            direction = -1
        
        ##If move is a vertical
        if (distanceColumn == 0):
            #If is the firts move and decide two move two steps and must be positive
            if(distanceLine == (2 * direction) and self.moved == False):
                self.update_position(new_position)
            #If just move just move one cell and must be positive
            elif distanceLine == (1 * direction):
                self.update_position(new_position)
        #This move kill the other piece enemy
        elif (distanceLine == (1 * direction) and distanceColumn == (1 * direction)):
            if board[new_position["line"]][new_position["column"]].color != self.color:
                self.update_position(new_position)
        else:
            return False


        


print(math.fabs(1) == 1)