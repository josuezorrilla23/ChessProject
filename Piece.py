import math 
class Piece:
    
    def __init__(self,name,color,posLine,posColumn,image):
        self.name = name
        self.color = color
        self.posLine = posLine
        self.posColumn = posColumn
        self.image = image
    
    def __str__(self):
        return "Name: "+ self.name +", Color: " + self.color + ", Line: " + str(self.posLine) + ", Column: " + str(self.posColumn)+"\n"
    
    def is_enemy(self,piece):
        if self.color != piece.color:
            return True
        else:
            return False

        #move_in_range("A8")
    
    def update_position(self,new_position):
        self.posLine = new_position["line"]    
        self.posColumn = new_position["column"]
        self.moved = True
    
    def calculate_distance(self,new_position):
        distanceLine = math.fabs(self.posLine - new_position["line"] )
        distanceColumn = math.fabs(self.posColumn - new_position["column"])
        return distanceLine, distanceColumn 

    def piece_in_path(self,board,new_position):
        
        dist_line, dist_column = self.calculate_distance(new_position)
        
        if self.posLine < new_position["line"]:
            from_position = self.posLine + 1
            to_position = new_position["line"]
        elif self.posLine > new_position["line"]:
            from_position = new_position["line"]
            to_position = self.posLine

        if dist_line > 1 and dist_column == 0:
            for line in range(from_position,to_position):
                if issubclass(type(board[line][new_position["column"]]),Piece):
                    return True
        elif dist_line == 1 and dist_column == 0:
            if issubclass(type(board[new_position["line"]][new_position["column"]]),Piece):
                    return True        
        return False
