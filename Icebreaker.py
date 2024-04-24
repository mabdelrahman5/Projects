#--------------------------------------------------------------
# ID#: 3149444
# Icebreaker Game - Milestone 3
#--------------------------------------------------------------
from graphics import *

player_1_score = 0
player_2_score = 0
class Icebreaker:
    def __init__(self, width = 500, height = 700, title = "Mohamed Abdelrahman - Icebreaker: Milestone 3 | 03-24-2024"):
        '''
        :purpose: initializes all the game objects and attributes,
        including window size, colours, status messages, players, buttons, and various other aspects that are integral to the game mechanics.
        :parameters:
        self - instance - instance of icebreaker object
        width - int - integer representing the width of the window
        height - int - integer representing the height of the window
        title - str - name of the window on the left side of the title bar
        :return: None
        '''
        self.win = GraphWin(title, width, height)
        self.win.setBackground("aquamarine")

        self.display_area = Rectangle(Point(0, 500), Point(width,height))
        self.display_area.setFill("light salmon")
        self.display_area.setOutline("light salmon")
        self.display_area.draw(self.win)
        self.game_board = Board(self.win)

        player_1_center = Point(50, 250)
        player_2_center = Point(450, 250)
        self.player_1 = Player(self.win, player_1_center, 90, 90, "cyan")
        self.player_2 = Player(self.win, player_2_center, 90, 90, "orange")
        self.player_list = [self.player_1, self.player_2]
        self.current_player = self.switch_players(self.player_1)

        display_x, display_y = self.current_player.check_coordinates()
        self.player_text = Text(Point(width*0.25, height*0.80), f"PLAYER 1 (BLUE): [{display_x//100:.0f}, {display_y//100:.0f}]\nMOVE PIECE")
        self.player_text.draw(self.win)
        self.game_text = Text(Point(width*0.25, height*0.90), "Mouse")
        self.game_text.draw(self.win)

        quit_center = Point(width*0.75, height*0.80)
        reset_center = Point(width*0.75, height*0.90)
        self.quit_button = Button(self.win, quit_center, 100, 30, "QUIT")
        self.reset_button = Button(self.win, reset_center, 100, 30, "RESET")
        self.move_counter = 1
    
    def switch_players(self, desired_player):
        '''
        :purpose: switches the player being controlled during the main play method
        :parameters:
        self - instance - instance of icebreaker object
        desired_player - object - player_object that is desired to be switched to
        :return: different player object
        '''
        for player in self.player_list:
            if desired_player == player:
                return player

    def play(self):
        '''
        :purpose: runs game logic by using mouse clicks: awaits for a mouseclick. 
        If the quit button is clicked, displays "BYE BYE !!" and awaits another mouseclick to close the window and terminate the program
        If the reset button is clicked, displays "RESET" and returns to top of the GUI loop
        If the Board squares are clicked, displays "{column}, {row}", and returns to the top of the GUI loop
        If any other space is clicked, displays "NOT VALID"
        :parameters:
        self - instance - instance of icebreaker object
        :return: None
        '''
        while True:
            click_point = self.win.checkMouse()
            display_x, display_y = self.current_player.check_coordinates()
            coord_x = display_x // 100
            coord_y = display_y // 100

            if self.current_player == self.player_1 and self.move_counter == 1:
                display_x, display_y = self.current_player.check_coordinates()
                if self.can_move(display_x, display_y) == False:
                        self.player_text.setText(f"GAME OVER !!\n Player 2 (Orange) HAS WON")
                        self.win.getMouse()
                        self.win.close()
                        score_board(2)
                self.player_text.setText(f"PLAYER 1 (BLUE): [{coord_x:.0f} {coord_y:.0f}]\n MOVE PIECE")
                if click_point:
                    x, y = click_point.getX(), click_point.getY()

                    if self.quit_button.is_clicked(click_point):
                        self.game_text.setText("BYE BYE !!")
                        self.win.getMouse()
                        self.win.close()

                    elif self.reset_button.is_clicked(click_point):
                        self.game_text.setText("RESET")
                        self.player_1.move_player(0,2)
                        self.player_2.move_player(4,2)
                        self.game_board.clear_ice()
                        self.current_player = self.switch_players(self.player_1)
                        self.win.getMouse()
                        self.game_text.setText("Mouse")
                    
                    elif self.player_1.player_clicked(click_point) == True:
                        self.game_text.setText(f"NOT VALID")

                    elif self.player_2.player_clicked(click_point) == True:
                        self.game_text.setText(f"NOT VALID")

                    elif self.game_board.is_broken_ice(click_point) == True:                            
                        self.game_text.setText(f"NOT VALID")

                    elif self.game_board.in_rect_list(click_point, self.game_board.ice_block_list) != None:
                        rect_x, rect_y = self.game_board.in_rect_list(click_point, self.game_board.ice_block_list)
                        if (1 >= (rect_x - coord_x) >= -1) and (1 >= (rect_y - coord_y) >= -1):
                            self.current_player.move_player(rect_x, rect_y)
                            self.game_text.setText(f"{self.game_board.in_rect_list(click_point, self.game_board.ice_block_list)}")
                            display_x, display_y = self.current_player.check_coordinates()
                            coord_x = display_x//100
                            coord_y = display_y//100
                            self.player_text.setText(f"PLAYER 1 (BLUE):[{coord_x:.0f} {coord_y:.0f}]\nBREAK ICE")
                            self.move_counter += 1
                        else:
                            self.game_text.setText("NOT VALID")
                    
                    else:
                        self.game_text.setText("NOT VALID")

            elif self.current_player == self.player_1 and self.move_counter == 2:
                display_x, display_y = self.current_player.check_coordinates()
                if click_point:
                    x, y = click_point.getX(), click_point.getY()
                
                    if self.quit_button.is_clicked(click_point):
                        self.game_text.setText("BYE BYE !!")
                        self.win.getMouse()
                        self.win.close()

                    elif self.reset_button.is_clicked(click_point):
                        self.game_text.setText("RESET")
                        self.player_1.move_player(0,2)
                        self.player_2.move_player(4,2)
                        self.game_board.clear_ice()
                        self.current_player = self.switch_players(self.player_1)
                        self.game_text.setText("Mouse")
                        self.move_counter = 1
                            
                    elif self.player_1.player_clicked(click_point) == True:
                        self.game_text.setText(f"NOT VALID")
                            
                    elif self.player_2.player_clicked(click_point) == True:
                        self.game_text.setText(f"NOT VALID")

                    elif self.game_board.is_broken_ice(click_point) == True:
                        self.game_text.setText(f"NOT VALID")
                            
                    elif self.game_board.in_rect_list(click_point, self.game_board.ice_block_list) == None:
                        self.game_text.setText("NOT VALID")
                            
                    elif self.game_board.in_rect_list(click_point, self.game_board.ice_block_list) != None:
                        rect_x, rect_y = self.game_board.in_rect_list(click_point, self.game_board.ice_block_list)
                        self.game_board.break_ice(self.win, rect_x, rect_y)
                        self.game_text.setText(f"{self.game_board.in_rect_list(click_point, self.game_board.ice_block_list)}")
                        self.current_player = self.switch_players(self.player_2)
                        self.move_counter = 1

                    else:
                        self.game_text.setText("NOT VALID")

            elif self.current_player == self.player_2 and self.move_counter == 1:
                display_x, display_y = self.current_player.check_coordinates()
                if self.can_move(display_x, display_y) == False:
                        self.player_text.setText(f"GAME OVER !!\n Player 1 (Blue) HAS WON")
                        self.win.getMouse()
                        self.win.close()
                        score_board(1)

                self.player_text.setText(f"PLAYER 2 (ORANGE): [{coord_x:.0f} {coord_y:.0f}]\n MOVE PIECE")
                if click_point:
                    x, y = click_point.getX(), click_point.getY()

                    if self.can_move(display_x, display_y) == False:
                        self.player_text.setText(f"GAME OVER !!\n Player 1 (Blue) HAS WON")
                        self.player1_score += 1
                        self.win.getMouse()
                        self.win.close()
                        score_board()

                    elif self.quit_button.is_clicked(click_point):
                        self.game_text.setText("BYE BYE !!")
                        self.win.getMouse()
                        self.win.close()

                    elif self.reset_button.is_clicked(click_point):
                        self.game_text.setText("RESET")
                        self.player_1.move_player(0,2)
                        self.player_2.move_player(4,2)
                        self.game_board.clear_ice()
                        self.current_player = self.switch_players(self.player_1)
                        self.win.getMouse()
                        self.game_text.setText("Mouse")
                    
                    elif self.player_1.player_clicked(click_point) == True:
                        self.game_text.setText(f"NOT VALID")

                    elif self.player_2.player_clicked(click_point) == True:
                        self.game_text.setText(f"NOT VALID")

                    elif self.game_board.is_broken_ice(click_point) == True:                            
                        self.game_text.setText(f"NOT VALID")

                    elif self.game_board.in_rect_list(click_point, self.game_board.ice_block_list) != None:
                        rect_x, rect_y = self.game_board.in_rect_list(click_point, self.game_board.ice_block_list)
                        if (1 >= (rect_x - coord_x) >= -1) and (1 >= (rect_y - coord_y) >= -1):
                            self.current_player.move_player(rect_x, rect_y)
                            self.game_text.setText(f"{self.game_board.in_rect_list(click_point, self.game_board.ice_block_list)}")
                            display_x, display_y = self.current_player.check_coordinates()
                            coord_x = display_x//100
                            coord_y = display_y//100
                            self.player_text.setText(f"PLAYER 2 (ORANGE):[{coord_x:.0f} {coord_y:.0f}]\nBREAK ICE")
                            self.move_counter += 1
                        else:
                            self.game_text.setText("NOT VALID")
                    else:
                        self.game_text.setText("NOT VALID")

            elif self.current_player == self.player_2 and self.move_counter == 2:
                display_x, display_y = self.current_player.check_coordinates()
                if click_point:
                    x, y = click_point.getX(), click_point.getY()
                
                    if self.quit_button.is_clicked(click_point):
                        self.game_text.setText("BYE BYE !!")
                        self.win.getMouse()
                        self.win.close()

                    elif self.reset_button.is_clicked(click_point):
                        self.game_text.setText("RESET")
                        self.player_1.move_player(0,2)
                        self.player_2.move_player(4,2)
                        self.game_board.clear_ice()
                        self.current_player = self.switch_players(self.player_1)
                        self.game_text.setText("Mouse")
                        self.move_counter = 1
                            
                    elif self.player_1.player_clicked(click_point) == True:
                        self.game_text.setText(f"NOT VALID")

                    elif self.player_2.player_clicked(click_point) == True:
                        self.game_text.setText(f"NOT VALID")

                    elif self.game_board.is_broken_ice(click_point) == True:
                        self.game_text.setText(f"NOT VALID")
                            
                    elif self.game_board.in_rect_list(click_point, self.game_board.ice_block_list) == None:
                        self.game_text.setText("NOT VALID")
                            
                    elif self.game_board.in_rect_list(click_point, self.game_board.ice_block_list) != None:
                        rect_x, rect_y = self.game_board.in_rect_list(click_point, self.game_board.ice_block_list)
                        self.game_board.break_ice(self.win, rect_x, rect_y)
                        self.game_text.setText(f"{self.game_board.in_rect_list(click_point, self.game_board.ice_block_list)}")
                        self.current_player = self.switch_players(self.player_1)
                        self.move_counter = 1
                    
                    else:
                        self.game_text.setText(F"NOT VALID")

    def can_move(self, player_x, player_y):
        '''
        :purpose: checks if player can move in the 8 squares around them
        :parameters:
        self - instance - instance of icebreaker game
        player - player being checked for if they can move or not
        :return:
        True or False of if they can move or not
        '''
        player_x += 45
        player_y += 45

        negative_x = player_x - 100
        negative_y = player_y - 100

        positive_x = player_x + 100
        positive_y = player_y + 100

        up = Point(player_x, negative_y)
        down = Point(player_x, positive_y)
        left = Point(negative_x, player_y)
        right = Point(positive_x, player_y)
        top_left = Point(negative_x, negative_y)
        top_right = Point(positive_x, negative_y)
        bot_left = Point(negative_x, positive_y)
        bot_right = Point(positive_x, positive_y)

        point_list = [up, down, left, right, top_left, top_right, bot_left, bot_right]
        for point in point_list:
            if self.game_board.in_rect_list(point, self.game_board.ice_block_list) != None:
                if self.game_board.is_broken_ice(point) == None and self.player_1.player_clicked(point) == False and self.player_2.player_clicked(point) == False:
                    return True
        return False
            
class Board:
    def __init__(self, win):
        '''
        :purpose: initializes a board of squares representing ice blocks in the icebreaker game window. also initializes an empty list that contains broken iceblocks
        :parameters:
        self - instance - instance of game board to create
        win - window - window in which game board squares are drawn
        :return: None
        '''
        self.broken_ice = []
        self.ice_block_list = []
        for row in range(5, 406, 100):
            row_list = []
            for col in range(5, 406, 100):
                rect = Rectangle(Point(row,col), Point(row+90,col+90))
                rect.draw(win)
                row_list.append(Rectangle(Point(row,col), Point(row+90,col+90)))
                rect.setFill("white")
            self.ice_block_list.append(row_list)

    def break_ice(self, win, x_coord, y_coord):
        '''
        :purpose: breaks an iceblock (drawing a new rectangle) on the clickpoint using specified coordinates, then adds it into the broken_ice stack
        :parameters:
        self - instance - instance of board
        click_point - checkMouse() method return - a coordinate extracted from a mouseclick within the window
        rect - rectangle object that represents iceblock
        :return: None
        '''
        self.rect = Rectangle(Point((x_coord*100) +5, (y_coord*100) +5), Point((x_coord*100) +95, (y_coord*100) +95))
        self.rect.setFill("aquamarine")
        self.rect.setOutline("aquamarine")
        self.rect.draw(win)
        self.broken_ice.append(self.rect)

    def clear_ice(self):
        '''
        :purpose: clears all the broken ice blocks and undraws them
        :parameters:
        self - instance of board object
        :return: None
        '''
        if len(self.broken_ice) == 0:
            return
        else:
            i = len(self.broken_ice) -1
            while i >= 0:
                self.rect = self.broken_ice[i]
                self.rect.undraw()
                i -= 1
                self.broken_ice.pop()


    def is_broken_ice(self, click_point):
        '''
        :purpose: checks if the clickpoint clicked broken ice.
        :parameters: 
        self - instance - instance of game board
        click_point - checkMouse() method return - point object at which the mouse was clicked
        :return: True if the broken ice piece was clicked, and None if ice list is empty and otherwise False
        '''
        if len(self.broken_ice) == 0:
            return 
        else:
            for i in range(len(self.broken_ice)):
                self.rect = self.broken_ice[i]
                if self.in_rectangle(click_point, self.rect) == True:
                    return True
            return

    
    def in_rectangle(self, click_point, rect: Rectangle) -> bool:
        '''
        :credits: I took this function from the house_demo1.py file we were shown in class and did some tweaking to achieve my desired results.
        :purpose: this function determines whether the mouse is clicked inside a rectangle
        :parameters: 
        click_point - point object at which the mouse was clicked
        rect - rectangle object to be checked for mouse click
        return: True if click-point is inside rect, False otherwise
        '''
        if int(rect.getP1().getX()) < int(rect.getP2().getX()):
            x_check = (
                int(rect.getP1().getX()) < click_point.getX() < int(rect.getP2().getX())
            )
        else:
            x_check = (
                int(rect.getP2().getX()) < click_point.getX() < int(rect.getP1().getX())
            )

        if int(rect.getP1().getY()) < int(rect.getP2().getY()):
            y_check = (
                int(rect.getP1().getY()) < click_point.getY() < int(rect.getP2().getY())
            )
        else:
            y_check = (
                int(rect.getP2().getY()) < click_point.getY() < int(rect.getP1().getY())
            )

        return x_check and y_check
    
    def in_rect_list(self, click_point, rect_list):
        '''
        :purpose: checks through an entire list to see if a rectangle has been clicked. if so, returns the list coordinates of the click
        :parameters:
        self - instance - instance of the object used
        click_point - checkMouse() method return - a coordinate extracted from a mouseclick within the window
        rect_list - list - 2 dimensional list of rectangle objects that have different points represented on the window.
        :return:
        x and y coordinates representing the row and column of the rectangle clicked, or None
        '''
        for x in range(len(rect_list)):
            for y in range(len(rect_list[x])):
                if self.in_rectangle(click_point, rect_list[x][y]) == True:
                    return (x, y)

class Button:
    def __init__(self, win, center, width, height, label):
        '''
        :purpose: creates a button in the window (rectangle object) that can be accessed and labeled for specific functions
        :parameters:
        self - instance - instance of button object
        win - window - window that the button will be displayed on
        center - int - center point for the button/rectangle
        width - int - width of button
        height - int - height of button
        label - label of button
        :return: None
        '''
        self.rect = Rectangle(Point(center.getX() - width/2, center.getY() - height/2), Point(center.getX() + width/2, center.getY() + height/2))
        self.label = Text(center, label)
        self.rect.draw(win)
        self.label.draw(win)
    
    def is_clicked(self, click_point):
        '''
        :purpose: checks if the specified button object is clicked or not
        :parameters:
        self - instance - instance of button object
        click_point - checkMouse() method return - coordinates from checkMouse() that checks the click point of a mouse button within the window
        :return: True or False whether the button object was clicked or not
        '''
        x, y = click_point.getX(), click_point.getY()
        return (self.rect.getP1().getX() <= x <= self.rect.getP2().getX() and self.rect.getP1().getY() <= y <= self.rect.getP2().getY())
    
class Player:
    def __init__(self, win, center, width, height, color):
        '''
        :purpose: initializes the player class, the attributes of the circle representing the player, and the location of the player object
        :parameters:
        self - instance - instance of player object
        win - window - window that the player will be displayed on
        center - int - center point for the player/oval
        width - int - width of player
        height - int - height of player
        color - color of player
        :return: None
        '''
        self.player = Oval(Point(center.getX() - width/2, center.getY() - height/2), Point(center.getX() + width/2, center.getY() + height/2))
        self.player.setFill(color)
        self.player.draw(win)
    
    def move_player(self, x_end, y_end):
        '''
        :purpose: moves a player object on the window towards the desired end location.
        :parameters:
        self - instance - instance of player
        x_end - x coordinate of the end point of where to move the 
        :return: None
        '''
        x_start, y_start = self.check_coordinates()

        x_end = (x_end * 100) +5
        y_end = (y_end * 100) +5

        x_change = x_end - x_start
        y_change = y_end - y_start
        self.player.move(x_change, y_change)

    def player_clicked(self, click_point):
        '''
        :purpose: checks if a player was clicked
        :parameters:
        self - instance - instance of player
        click_point - checkMouse() method return - coordinates from checkMouse() that checks the click point of a mouse button within the window
        :return: True if the player instance was clicked, False if not.
        '''
        x, y = click_point.getX(), click_point.getY()
        return (self.player.getP1().getX() <= x <= self.player.getP2().getX() and self.player.getP1().getY() <= y <= self.player.getP2().getY())
    
    def check_coordinates(self):
        '''
        :purpose: returns the coordinates of the player object
        :parameters:
        self - instance - instance of player
        :return: x and y coordinates of player
        '''
        return self.player.getP1().getX(), self.player.getP1().getY()
        

def splash_screen():
    '''
    :purpose: creates the splash screen of the icebreaker game, along with the title, creator name, additional info, and a play game and close button.
    Internally contains the game object and commences it after clicking the play button
    :parameters: None
    :return: None
    '''
    splash_win = GraphWin("Mohamed Abdelrahman - Icebreaker: Milestone 3 | 03-24-2024", 500, 500)
    splash_win.setBackground("cyan")

    welcome_text = Text(Point(250, 100), "Welcome to the Icebreaker Game\nThis game was written in part by Mohamed A.\nfor CMPT 103, Winter 2024")
    welcome_text.setSize(15)
    welcome_text.draw(splash_win)
    
    play_text = Text(Point(250,250), "Would you like to play?")
    play_text.setSize(25)
    play_text.setTextColor("white")
    play_text.draw(splash_win)
    
    

    play_button = Button(splash_win, Point(250, 300), 150, 40, "Play")
    close_button = Button(splash_win, Point(250, 350), 150, 40, "Quit")

    while True:
        click_point = splash_win.getMouse()

        if close_button.is_clicked(click_point):
            splash_win.getMouse()
            splash_win.close()

        elif play_button.is_clicked(click_point):
            splash_win.close()
            icebreaker = Icebreaker()
            icebreaker.play()

def score_board(player_num:int):
    '''
    :purpose: creates the scoreboard window that appears after the icebreaker game has finished. contains the total game scores of player 1 and player 2,
    and adds to them based on the argument integer given (1 for player 1, 2 for player 2)
    :parameters:
    player_num - int - determines whether a point should be given to player one or player two based on the integer given
    :return: None
    '''
    global player_1_score, player_2_score
    if player_num == 1:
        player_1_score += 1
    if player_num == 2:
        player_2_score += 1
    score_win = GraphWin("Mohamed Abdelrahman - Icebreaker: Milestone 3 | 03-24-2024", 500, 500)
    score_win.setBackground("light pink")

    game_score = Text(Point(250, 75), "Game Score:")
    game_score.setSize(20)
    game_score.setStyle("bold")
    game_score.draw(score_win)

    score_board = Rectangle(Point(175,100), Point(325, 250))
    score_board.setFill("white")
    score_board.draw(score_win)

    score_text = Text(Point(250, 175), f"Player 1: {player_1_score}\n Player 2: {player_2_score}")
    score_text.setSize(20)
    score_text.draw(score_win)

    play_button = Button(score_win, Point(250, 300), 150, 40, "Replay")
    close_button = Button(score_win, Point(250, 350), 150, 40, "Quit")

    while True:
        click_point = score_win.getMouse()

        if close_button.is_clicked(click_point):
            score_win.getMouse()
            score_win.close()

        elif play_button.is_clicked(click_point):
            score_win.close()
            icebreaker = Icebreaker()
            icebreaker.play()

if __name__ == '__main__':
    splash_screen()
