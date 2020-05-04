from Player import Player
from Pawn import Pawn
from Piece import Piece
class GameBoard:
    def __init__(self):
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
                lineToPrint = lineToPrint + " " + cell
            print(lineToPrint)
            lineToPrint = ""
    
    def set_player(self,player):
        name1 = input("Name of the first player: ")

        self.player1 = Player(name1,"black",[])
        name2 = input("Name of the Second player: ")
        self.player2 = Player(name2,"white",[])
    
    def draw_piece(self,piece:Piece):
        self.board[piece.positionX][piece.positionY] = piece.image

    def set_pieces(self):
        pieces = []
        for i in range(1,9):
            pawn = Pawn("Pawn","Black",2,i,"[ \u265F  ]")
            pieces.append(pawn)
        for i in range(1,9):
            pawn = Pawn("Pawn","White",7,i,"[ \u2659  ]")
            pieces.append(pawn)
        return pieces

        


    

juego = GameBoard()

juego.draw_board()

#fila,columna = getCordinate("A8")
juego.draw_board()
#p = Pawn("Black","Peon",3,5)
#juego.draw_piece(p)
juego.set_pieces()
pcs = juego.set_pieces()
for p in pcs:
    juego.draw_piece(p)

juego.draw_board()




# printBoard(MovePawn("B2",board))