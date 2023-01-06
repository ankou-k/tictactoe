from tkinter import *

WINDOW_SIZE = 300
GRID_LINE_SIZE = 2
GRID_SIZE = WINDOW_SIZE / 3
GRID_COLOR = 'black'
EMPTY = 0
X = 1
O = 2
X_PLAYER = input("What is the name of the first player? ")
O_PLAYER = input("What is the name of the second player? ")
GAME_OVER = 3

class Game(Tk):
  def __init__(self):
    Tk.__init__(self)
    self.title("              Tic Tac Toe")

    self.tictactoe = Canvas(height=WINDOW_SIZE, width=WINDOW_SIZE)
    self.tictactoe.pack()

    self.new_board()

    self.turn = X
    self.game_state = self.turn #3 possible values

    self.tictactoe.bind('<Button-1>', self.click)

    self.board = [
      [EMPTY, EMPTY, EMPTY],
      [EMPTY, EMPTY, EMPTY],
      [EMPTY, EMPTY, EMPTY]
    ]

  
  def new_board(self):
    for item in range(1,3):
      #VERTICAL
      self.tictactoe.create_line(GRID_SIZE*item, 0, GRID_SIZE*item, WINDOW_SIZE, width=GRID_LINE_SIZE, fill=GRID_COLOR)
      #HORIZONTAL
      self.tictactoe.create_line(0, GRID_SIZE*item, WINDOW_SIZE, GRID_SIZE*item, width=GRID_LINE_SIZE, fill=GRID_COLOR)

  def click(self, event):
    x = self.ptg(event.x)
    y = self.ptg(event.y)

    if (self.game_state == X and self.board[x][y] == EMPTY):
      self.tictactoe.create_text(self.center(event.x), self.center(event.y), text="X", font=('Arial','50','bold'))
      self.board[x][y] = X
      self.hasWon()
      self.turn = O
      self.game_state = self.turn
    
    elif (self.game_state == O and self.board[x][y] == EMPTY):
      self.tictactoe.create_text(self.center(event.x), self.center(event.y), text="O", font=('Arial','50','bold'))
      self.board[x][y] = O
      self.hasWon()
      self.turn = X
      self.game_state = self.turn
  
  def ptg(self, pixel_value):
    if pixel_value >= WINDOW_SIZE:
      pixel_value = WINDOW_SIZE - 1
    
    grid_value = int(pixel_value/GRID_SIZE)
    return grid_value
  
  def center(self, pixel_value):
    co = self.ptg(pixel_value)
    grid = (co)*GRID_SIZE + GRID_SIZE/2
    return grid

  def hasWon(self):
    winner = -1
    for i in range(3):
      if self.board[i][0] == self.board[i][1] and self.board[i][2] == self.board[i][1] and self.board[i][0] != EMPTY:
        winner = self.turn
    for i in range(3):
      if self.board[0][i] == self.board[1][i] and self.board[2][i] == self.board[1][i] and self.board[0][i] != EMPTY:
        winner = self.turn
    
    if self.board[0][0] != EMPTY and self.board[1][1] == self.board[0][0] and self.board[2][2] == self.board[0][0]:
      winner = self.turn

    
    
    boardEmpty = False
    for a in self.board:
      if EMPTY in a:
        boardEmpty = True

    if boardEmpty == False:
      print("It's a tie!")
    elif winner == X:
      print("The winner is..." + X_PLAYER + "!")
    elif winner == O:
      print("The winner is..." + O_PLAYER + "!")
      


def printHello():
  print("hello")

printHello()

ourGame = Game()
ourGame.mainloop()