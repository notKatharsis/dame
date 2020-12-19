from board import Board

class GameHandler:
    def __init__(self):
        self.current_player = 1
        self.selected = None
        self.white_count = 0
        self.black_count = 0

    def select(self, event, board):

        board_arr = board.get_board()
        y, x = self.get_cell(event.x, event.y, board)
        select = self.selected
        if self.selected != None:
            for coords in self.selected:
                if  y == coords[1] and x == coords[0]:
                    self.move_piece(board_arr[select[0][1]][select[0][0]], [y,x], board)
                else:
                    self.selected = [[x, y]]
        else:
            self.selected = [[x, y]]

        #for i in range(x, 0, -1):                                               #check for all adjacent positions behind the piece \
        #    if x - i >= 0 and y - i >= 0 or x + i <= 7 and y + i <= 7:
        #        #print(x - i, y - i)
        #        all_selected.append([x-i,y-i])
        #for i in range(8 - x):                                                  #check for all adjacent postions before the piece \
        #    if x - i >= 0 and y - i >= 0 or x + i <= 7 and y + i <= 7:
        #        #print(x + i, y + i)
        #        all_selected.append([x+i, y+i])
        #for i in range(x, -1, -1):
        #    if y + i >= 0 and y + i <= 7:
        #        #print(x - i, y + i)
        #        all_selected.append([x-i,y+i])
        #for i in range(1, y + 1):
        #    if x + i >= 0 and x + i <= 7:
        #        #print(x + i, y - i)
        #        all_selected.append([x+i,y-i])
        #
        #for arr in all_selected:
        #    board.draw_selected(arr[0], arr[1])                #vlt später nützzlich

        
        
        if board_arr[y][x] != 0:

            try:        
                if board_arr[y-1][x-1] == 0 and board_arr[y][x].get_player1() == True:       #ist frei links oben und ist spieler 1
                    self.selected.append([x-1, y-1])
            except: pass

            try:
                if board_arr[y+1][x-1] == 0 and board_arr[y][x].get_player1() == False:
                    self.selected.append([x-1,y+1])
            except: pass

            try:
                if board_arr[y-1][x+1] == 0 and board_arr[y][x].get_player1() == True:       #ist frei rechts oben und ist spieler 1
                    self.selected.append([x+1, y-1])
            except: pass

            try:
                if board_arr[y+1][x+1] == 0 and board_arr[y][x].get_player1() == False:
                    self.selected.append([x+1, y+1])
            except: pass    
        

        for coords in self.selected:
            board.draw_selected(coords[0], coords[1])
        
        
    def controls(self): return  

    def get_cell(self, x, y, board):
        u = board.get_u()
        return (y-(y//u))//u,(x-(x//u))//u
    
    def draw_diff(self): return

    def move_piece(self, piece, moveAt, board):
        origin = piece.get_coords()

        dx =  moveAt[1] - origin[1]
        dy = moveAt[0] - origin[0]
        newX = origin[1] + dx
        newY = origin[0] + dy
        piece.set_coords([newY, newX])
        print(piece.get_coords())
        board.set_new_coords([newY, newX], piece)
        board.set_new_coords([origin[0], origin[1]], 0)

        board.draw_board()

        self.selected = []
        

    def check_moves(self): return
