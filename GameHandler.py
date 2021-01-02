from board import Board

class GameHandler:
    def __init__(self):
        self.current_player = True
        self.selected = None
        self.white_count = 0
        self.black_count = 0

    def select(self, event, board):

        board_arr = board.get_board()
        y, x = self.get_cell(event.x, event.y, board)
        
        if self.selected != None and x == self.selected[0][0] and y == self.selected[0][1]:
            self.selected = None
            board.delete_selected()
            board.draw_board()
            return

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

        
        beatable = False
        
        if board_arr[y][x] != 0:
            
            if board_arr[y][x].get_d():
                try:
                    if x> 0 and y > 0 and board_arr[y-1][x-1] != 0 and board_arr[y][x].get_player1() == True and self.current_player == True:
                        if board_arr[y-2][x-2] == 0 and board_arr[y-1][x-1].get_player1() == False:
                            self.selected.append([x-2,y-2])
                            beatable = True
                except: pass
                try:
                    if x> 0 and y < 7 and board_arr[y+1][x-1] != 0 and board_arr[y][x].get_player1() == True and self.current_player == True:
                        if board_arr[y+2][x-2] == 0 and board_arr[y+1][x-1].get_player1() == False:
                            self.selected.append([x-2,y+2])
                            beatable = True
                except: pass
                try:
                    if x < 7 and y > 0 and board_arr[y-1][x+1] != 0 and board_arr[y][x].get_player1() == True and self.current_player == True:
                        if board_arr[y-2][x+2] == 0 and board_arr[y-1][x+1].get_player1() == False:
                            self.selected.append([x+2,y-2])
                            beatable = True
                except: pass
                try:
                    if x < 7 and y < 7 and board_arr[y+1][x+1] != 0 and board_arr[y][x].get_player1() == True and self.current_player == True:
                        if board_arr[y+2][x+2] == 0 and board_arr[y+1][x+1].get_player1() == False:
                            self.selected.append([x+2,y+2])
                            beatable = True
                except: pass
                try:
                    if board_arr[y][x].get_player1() == True and self.current_player == True and beatable == False:
                        temp = self.check_piece(x + 1,y + 1, board_arr, [], +1, +1)
                        for l in temp:
                            self.selected.append(l)
                        temp = self.check_piece(x + 1,y - 1, board_arr, [], +1, -1)
                        for l in temp:
                            self.selected.append(l)
                        temp = self.check_piece(x - 1,y + 1, board_arr, [], -1, +1)
                        for l in temp:
                            self.selected.append(l)
                        temp = self.check_piece(x - 1,y - 1, board_arr, [], -1, -1)
                        for l in temp:
                            self.selected.append(l)
                        
                except Exception as e: print(e)

                try:
                    
                    if x> 0 and y > 0 and board_arr[y-1][x-1] != 0 and board_arr[y][x].get_player1() == False and self.current_player == False:
                        if board_arr[y-2][x-2] == 0 and board_arr[y-1][x-1].get_player1() == True:
                            self.selected.append([x-2,y-2])
                            beatable = True
                    
                except: pass
                try:

                    if x> 0 and y < 7 and board_arr[y+1][x-1] != 0 and board_arr[y][x].get_player1() == False and self.current_player == False:
                        if board_arr[y+2][x-2] == 0 and board_arr[y+1][x-1].get_player1() == True:
                            self.selected.append([x-2,y+2])
                            beatable = True
                except: pass
                try:
                    if x < 7 and y > 0 and board_arr[y-1][x+1] != 0 and board_arr[y][x].get_player1() == False and self.current_player == False:
                        if board_arr[y-2][x+2] == 0 and board_arr[y-1][x+1].get_player1() == True:
                            self.selected.append([x+2,y-2])
                            beatable = True
                except: pass
                try:    
                    if x < 7 and y < 7 and board_arr[y+1][x+1] != 0 and board_arr[y][x].get_player1() == False and self.current_player == False:
                        if board_arr[y+2][x+2] == 0 and board_arr[y+1][x+1].get_player1() == True:
                            self.selected.append([x+2,y+2])
                            beatable = True
                except: pass
                try:
                    if  board_arr[y][x].get_player1() == False and self.current_player == False and beatable == False:
                        temp = self.check_piece(x + 1,y + 1, board_arr, [], +1, +1)
                        for l in temp:
                            self.selected.append(l)
                        temp = self.check_piece(x + 1,y - 1, board_arr, [], +1, -1)
                        for l in temp:
                            self.selected.append(l)
                        temp = self.check_piece(x - 1,y + 1, board_arr, [], -1, +1)
                        for l in temp:
                            self.selected.append(l)
                        temp = self.check_piece(x - 1,y - 1, board_arr, [], -1, -1)
                        for l in temp:
                            self.selected.append(l)
                    
                except Exception as e: print(e)

            else:    

                try:        
                    if board_arr[y-1][x-1] == 0 and board_arr[y][x].get_player1() == True and self.current_player == True and beatable == False:       #ist frei links oben und ist spieler 1
                        self.selected.append([x-1, y-1])
                    elif board_arr[y-1][x-1] != 0 and board_arr[y][x].get_player1() == True and self.current_player == True:
                        if board_arr[y-2][x-2] == 0 and board_arr[y-1][x-1].get_player1() == False:
                            self.selected = [[x,y],[x-2,y-2]]
                            beatable = True
                except: pass

                try:
                    if board_arr[y+1][x-1] == 0 and board_arr[y][x].get_player1() == False and self.current_player == False and beatable == False:       #frei spieler 2
                        self.selected.append([x-1,y+1])
                    elif board_arr[y+1][x-1] != 0 and board_arr[y][x].get_player1() == False and self.current_player == False:
                        if board_arr[y+2][x-2] == 0 and board_arr[y+1][x-1].get_player1() == True:
                            self.selected = [[x,y],[x-2, y+2]]
                            beatable = True
                except: pass

                try:
                    if board_arr[y-1][x+1] == 0 and board_arr[y][x].get_player1() == True and self.current_player == True and beatable == False:       #ist frei rechts oben und ist spieler 1
                        self.selected.append([x+1, y-1])
                    elif board_arr[y-1][x+1] != 0 and board_arr[y][x].get_player1() == True and self.current_player == True:
                        if board_arr[y-2][x+2] == 0 and board_arr[y-1][x+1].get_player1() == False:
                            self.selected = [[x,y],[x+2, y-2]]
                            beatable = True
                except: pass

                try:
                    if board_arr[y+1][x+1] == 0 and board_arr[y][x].get_player1() == False and self.current_player == False and beatable == False:       #frei spieler 2
                        self.selected.append([x+1, y+1])
                    elif board_arr[y+1][x+1] != 0 and board_arr[y][x].get_player1() == False and self.current_player == False:
                        if board_arr[y+2][x+2] == 0 and board_arr[y+1][x+1].get_player1() == True:
                            self.selected = [[x,y],[x+2, y+2]]
                            beatable = True
                except: pass
        
        if self.selected != None:
            for coords in self.selected:
                board.draw_selected(coords[0], coords[1])
        
        return
        
        
    def controls(self): return  

    def get_cell(self, x, y, board):
        u = board.get_u()
        return (y-(y//u))//u,(x-(x//u))//u
    
    def draw_diff(self): return

    def move_piece(self, piece, moveAt, board):
        origin = piece.get_coords()

        dx =  moveAt[1] - origin[1]
        dy = moveAt[0] - origin[0]

        if dx <= -2 and dy <= -2:
            board.set_new_coords([origin[0] - 1, origin[1] - 1], 0)
        
        if dx <= -2 and dy >= 2:
            board.set_new_coords([origin[0] + 1, origin[1] - 1], 0)

        if dx >= 2 and dy <= -2:
            board.set_new_coords([origin[0] - 1, origin[1] + 1], 0)
        
        if dx >= 2 and dy >= 2:
            board.set_new_coords([origin[0] + 1, origin[1] + 1], 0)

        newX = origin[1] + dx
        newY = origin[0] + dy
        piece.set_coords([newY, newX])
        
        board.set_new_coords([newY, newX], piece)
        board.set_new_coords([origin[0], origin[1]], 0)
        
        board.draw_board()

        self.selected = None

        if self.check_dame([newX, newY], self.current_player):
            piece.set_d(True)

        self.current_player = not self.current_player
        return
    
    
        

    def check_dame(self, pos, player):
        if player == True and pos[1] == 0:
            return True
        elif player == False and pos[1] == 7:
            return True
        else: return False

    def check_piece(self, x, y, board, arr, dx, dy):
        #if (board[y][x] != 0) or (y >= 8 and x >= 8 or y < 0 and x < 0):
        #    return arr
        #arr.append([y,x])
        #print(arr)
        #self.check_piece(y + 1, x + 1, board, arr)
        
        #return arr

        while y <= 7 and x <= 7 and y >= 0 and x >= 0 and board[y][x] == 0:
            arr.append([x, y])
            y += dy
            x += dx

        return arr