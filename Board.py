from Player import Player
from Pawn import Pawn
from Piece import Piece
from Queen import Queen
from Knight import Knight

class GameBoard:
    def __init__(self):
        self.pieces = []
        self.players = []
        self.board =  [["",3*" "+"A", 5*" "+"B", 5*" "+"C", 5*" "+"D",5*" "+"E",5*" "+"F",5*" "+"G",5*" "+"H"],
         ["8","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["7","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["6","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["5","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["4","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["3","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["2","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["1","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"]]
         
    def draw_board(self):
        lineToPrint = ""
        for line in self.board:
            for cell in line:
                if issubclass(type(cell),Piece):
                    lineToPrint = lineToPrint + " " + cell.image
                else:
                    lineToPrint = lineToPrint + " " + cell
            print(lineToPrint)
            lineToPrint = ""
    
    def set_player(self):
        name1 = input("Name of the first player: ")
        self.players.append(Player(name1,"Black",[]))
        name2 = input("Name of the Second player: ")
        self.players.append(Player(name2,"White",[]))
    
    def draw_piece(self,piece:Piece):
        self.board[piece.posLine][piece.posColumn] = piece.image

    def get_piece(self,position):
        if self.is_piece(position):
            return self.board[position["line"]][position["column"]]
    
    def is_piece(self,position):
        return issubclass(type(self.board[position["line"]][position["column"]]),Piece)

    def set_pieces(self):
        
        self.board[1][4] = Queen("Queen","Black",1,4,"[ \u265B  ]")
        self.board[8][4] = Queen("Queen","White",8,4,"[ \u2655  ]")
        self.board[8][2] = Knight("Knight","White",8,2,"[ \u265E  ]")
        for i in range(1,9):
            self.board[2][i] = Pawn("Pawn","Black",2,i,"[ \u265F  ]")
            self.board[7][i] = Pawn("Pawn","White",7,i,"[ \u2659  ]")

        # self.pieces.append(Queen("Queen","Black",1,4,"[ \u265B  ]"))
        # self.pieces.append(Queen("Queen","White",8,4,"[ \u2655  ]"))
        # for i in range(1,9):
        #     self.pieces.append(Pawn("Pawn","Black",2,i,"[ \u265F  ]"))
        #     self.pieces.append(Pawn("Pawn","White",7,i,"[ \u2659  ]"))
        #return self.pieces
    
    def set_pieces_player(self):
        for player in self.players:
            for line in self.board:
                for piece in line:
                    if isinstance(piece,(Queen,Pawn)):
                        if piece.color == player.color:
                            player.pieces.append(piece)
    
    def is_empty(self,cordinate):
        if self.board[cordinate["line"]][cordinate["column"]]== "[    ]":
            return True
        else:
            return False
    
    def decode_cordinate(self,cord_str):
        cordinate = dict()
        cordinate["line"] = 9 - int(cord_str[1:])
        cordinate["column"] = ord(cord_str[0:1]) - 64
        return cordinate
    
    def move_in_range(self,cordinate):
        #tengo que mejorar
        if (cordinate["line"] >= 1 and cordinate["line"] <= 8) and (cordinate["column"]) >= 1 and cordinate["column"] <= 8:
            return True
        else:
            return False
    
    def ask_play(self):
        i = 0
        while True:
            pieceGet = self.ask_piece(self.players[i%2])
            if pieceGet == None:
                break
            self.ask_new_position(pieceGet)
            # else:
            #     print("Invalid move")
            #self.ask_play()
            i += 1

    def quit_game(self):
        decission = input("Are you sure you wanna quit?\n press N to continue or Y to quit: ")
        if decission == "Y":
            return True
        elif decission == "N":
            return False
        else:
            print("You must press 'Y' or 'N'")
            self.quit_game()

    def start_game(self):
        self.set_pieces()
        self.draw_board()
        self.set_player()
        self.set_pieces_player()
        position = dict()
        position["line"] = 2
        position["column"] = 1
        print(self.get_piece(position))
        # print(self.players[0])
        # print(self.players[1])
        self.ask_play()
    
    def ask_piece(self,player:Player):
        position_str = input(player.name +" "+"Wich piece do you want to move: ")
        if position_str == "Q":
            if(self.quit_game() == True):
                return None
        position = self.decode_cordinate(position_str)
        piece_get = self.get_piece(position)
        if self.move_in_range(position):
            if player.color == piece_get.color:
                return self.get_piece(position)
            else:
                print("That piece dont belong to you.")
                return self.ask_piece(player)
        else:
            print("Move is out of range.")
            return self.ask_piece(player)

    def ask_new_position(self,piece):
        new_position = self.decode_cordinate(input("Where you want to locate your piece: "))
        if piece.piece_in_path(self.board,new_position) and type(piece) != Knight:
            print("There is a piece in the midle, you cant move")
            self.ask_new_position(piece)
        else:
            self.board[piece.posLine][piece.posColumn] = "[    ]"
            piece.move(new_position,self.board)
            self.board[piece.posLine][piece.posColumn] = piece
            self.draw_board()

juego = GameBoard()

#juego.draw_board()

# pcs = juego.set_pieces()
# for p in pcs:
#     juego.draw_piece(p)
#juego.draw_board()

juego.start_game()
print(juego.players[0])
print(juego.players[1])
print(juego.pieces)
