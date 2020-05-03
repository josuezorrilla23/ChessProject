from Piece import Piece
class Pawn(Piece):

    def __init__(self,name,color,positionX,positionY,image):
        Piece.__init__(self,name,color,positionX,positionY,image)
        self.moved = False

    def update_position(self,positionX,positionY):
        self.positionX = positionX
        self.positionY = positionY
        self.moved = True

    def move(self,new_position_x,new_position_y):
        distanceX = new_position_x - self.positionX
        distanceY = new_position_y - self.positionY
        #Check the color of the piece
        if self.color == "white":
            ##If move is a vertical
            if (distanceY == 0):
                #If is the firts move and decide two move two steps and must be positive
                if(distanceX == 2 and self.moved == False):
                    self.update_position(new_position_x,new_position_y)
                #If just move just move one cell and must be positive
                elif distanceX == 1:
                    self.update_position(new_position_x,new_position_y)
            #This move kill the other piece enemy
            elif (distanceX == 1 and distanceY == 1):
                    self.update_position(new_position_x,new_position_y)
            else:
                return False
        if self.color == "Black":
            ##If move is a vertical
            if (distanceY == 0):
                #If is the firts move and decide two move two steps and must be positive
                if(distanceX == -2 and self.moved == False):
                    self.update_position(new_position_x,new_position_y)
                #If just move just move one cell and must be positive
                elif distanceX == -1:
                    self.update_position(new_position_x,new_position_y)
            #This move kill the other piece enemy
            elif (distanceX == -1 and distanceY == -1):
                    self.update_position(new_position_x,new_position_y)
            else:
                return False            
    