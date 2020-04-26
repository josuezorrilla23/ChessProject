
class GameBoard:
    def __init__(self,player1,player2):
        self.player1 = player1
        self.player2 = player2
        self.board =  [["",3*" "+"A", 5*" "+"B", 5*" "+"C", 5*" "+"D",5*" "+"E",5*" "+"F",5*" "+"G",5*" "+"H"],
         ["8","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["7","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["6","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["5","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["4","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["3","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["2","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"],
         ["1","[    ]", "[    ]", "[    ]", "[    ]","[    ]", "[    ]", "[    ]", "[    ]"]]

    def drawBoard(self):
        lineToPrint = ""
        for line in self.board:
            for cell in line:
                lineToPrint = lineToPrint + " " + cell
            print(lineToPrint)
            lineToPrint = ""

juego = GameBoard("Josue","Mario")

juego.drawBoard()
  
    




    

# #getCordinate("A8")
# def getCordinate(cell):
#     fila = ord(cell[0:1]) - 64
#     columna = 9 - int(cell[1:])
#     return fila,columna

# def MoveCell(fila,columna,board):
#     board[fila][columna] = "[ \u2659  ]"
#     return board

# printBoard(board)    
# fila,columna = getCordinate("A8")
# printBoard(MoveCell(fila,columna,board))
# #print(printCell("H1"))

# def MovePawn(cordinate,board):
#     if ord(cordinate[0:1]) > 72 or int(cordinate[1:]) > 8:
#         print("Movimiento fuera de rango.")
#     else:
#         return MoveCell(9-int(cordinate[1:]),ord(cordinate[0:1])-64,board)

# printBoard(MovePawn("B2",board))