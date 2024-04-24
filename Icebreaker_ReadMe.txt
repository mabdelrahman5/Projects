ICEBREAKER GAME
----------------------
Game Rules:
Icebreaker is a two player game on a board of 5 by 5 squares of ice.
The players' objective is to trap their opponent so they cannot move, the first player who is unable to move loses the game.

Game starts with a board of solid ice and players in different squares. 
Players have two tasks each turn: to move by clicking  on  nearby square, and then to break a free square of ice.
If a player cannot move any longer, because the nearby squares are broken or occupied by an opponent, that player loses, the winner is declared, and users are prompted to either play again or quit.

Status of the game: displayed on the bottom left of the game window, displaying which player's turn, their coordinates, the player's task (move or break ice), and the outcome of each mouse click.

The game can be terminated or reset at any moment, by clicking the correspondent buttons.

Program Structure and Logic:

BOARD LAYOUT
The main application window consists of a grid of board squares, and a section containing two text
messages and two buttons.
The game board dimensions (number of rows and columns) are chosen by the developer. They are
fixed and can be any size between 5x5 and 10x10. The examples below show a board with 5 rows
and 7 columns.

GAME PLAY
A player’s turn consists of two tasks:
1) move their piece: a piece may be moved to any unoccupied
adjacent white square (up, down, left, right or diagonally).
Your program must detect an attempt to make an invalid
move to a square outside the range of adjacent squares,
and report it NOT VALID in the mouse click status message.

2) break a square of ice: Any unbroken and unoccupied
square may be clicked. Once broken, a square remains
broken for the rest of the game. Clicking on a broken or
occupied square should be reported as NOT VALID. 

How the game ends
The objective of the game is to enclose your opponent so they
cannot move. The first player unable to move loses the game. A
player is unable to move when all squares surrounding it are
either broken or occupied by the other player. 

STATUS DISPLAY
The current state of the game is identified by the current player, their next task, the location of
both players, the state of the board squares (ice or water), and where the mouse has been clicked.
Your game should display at least two status messages:

1) A player status message informing the users whose turn it is, and what their next task is
(move or break ice). If the player’s turn is to move, the message should also display the
player’s current board position (in square brackets in the examples below). This message
should display the winning player when the game ends.

2) A mouse click status message showing the board coordinates of a valid board click, or the
text 'NOT VALID'. When the QUIT or RESET button is clicked, the mouse click message
should display 'BYE BYE !!', or 'RESET', respectively.

Program Logic and Major Decisions:

Icebreaker()
 - in the initialization, I hardcoded a lot of the main window facets, creating a rectangle at the bottom of the screen below the game board so that I could set up my status messages and button objects on that plane. I also hardcoded this part to understand the dimensions needed before i make the board.
 - for the switch_player method, i chose to have a 2 player list comprised of the player objects that I make that are essentially Oval objects that are movable within my icebreaker game and can be checked if they are clicked. They can also be checked for their x and y coordinates (their getP1().getX() and getP1.getY() values) to aid in me using their coordinates for display after they are floor divided by 100, and also to be used in the can_move method that checks all adjacent squares by using the original x and y coordinates given.
 - the play method is controlled fully by clicks that allow various aspects of my game to change certain values and progress the game. I made by play() method loop by utilizing the current player, which is any player between player1 and player2, and a move counter. These variables are always changing based on the current player playing, and the move that they have. player1, with move counter 1 means that player1 will be moving, and player2 with move counter 2 means that player 2 will be breaking ice. From the beginning, the move counter and player are set to 1. The program will remain in the state of the player and move until valid actions are taken corresponding to the move counter value (1 = move 2 = break ice). If an action is taken and the state was for player 1 to move, the move counter will increase by 1, and the player will be tasked to break ice. Once the ice is broken successfully, then the players will be switched and the move counter resets to 1.
 - during all of this, I use the display_ and coord_ variables to either use the x or y value in the window, or the x or y coordinate being shown to the player. the difference between these is a division of 100 to the display_ values, and i separate them to make it more decisive to use when I am trying to show or use a certain integer value.
 - my can_move method uses the display_ x and y values given of a specific player to and modifies them to essentially be centers of each square on the board. These center coordinates are then created new variables, ones that are subtracted by 100, which are the negative values, and ones that are added by 100, which are the positive values. These values are used to generate 8 possible points, created by variables corresponding to the direction, that each player can move towards. I then run through a loop of all the points and then use those points to check if the points are within the ice block list. If they are, I then check if they are not clicking broken ice, or a player object, and if they are not, they return True. Otherwise, at the exit of the loop, I return False, showing no possible options for the player to move.

Board()
 - I initialized the board with all squares being drawn 10 points away from each other, with each square having an x and y of 90 each. I have a board of squares going 5x5, totaling to about 500 points x and y for the entire board itself. The square coordinates are all added to the ice block list in order to check for mouseclicks on them in the future. I also initialize a broken ice list that is empty
 - To break the ice, I use the coordinate of the clicked rectangle and draw another rectangle on top of it, this one representing the same color as the background to make it look like there is nothing there. I then add this rectangle to the broken ice list so that I can check if it has been clicked, and also so I can clear it later on easier.
 - I use the clear_ice method when I reset the game to remove all the broken ice and reset the board to normal. This occurs by me essentially undrawing and popping all the broken ice squares within the broken ice list
 - The in_rectangle method I use is taken from the house_demo1.py file that I examined in class with professor Renwick. This method checks if a certain point (mouseclick for example) fits into the points of a specified rectangle. I use this in both the is_broken_ice methods and in_rect_list methods to check through the broken ice list and ice block lists in the main game.

Button():
 - initialized as a drawn rectangle in the window using the game window, center point, width, height, and label for text. I use the center to create the top left x and y coordinates of the oval, as well as the bottom right by subtracting half of the width and height of each coordinate for the top left by the center, and then adding half the width and height of each coordinate for the bottom right. This is then drawn and labeled with the text given ("QUIT" and "RESET", for example)
 - the is_clicked method is simple and just checks if the object itself was clicked.

Player():
 - initialized as a drawn oval in the window using the game window, the center point of the object, the width, the height, and a color to specify which player it is. I use the center to create the top left x and y coordinates of the oval, as well as the bottom right by subtracting half of the width and height of each coordinate for the top left by the center, and then adding half the width and height of each coordinate for the bottom right. This is then drawn and filled with a specified color.
- the move_player method is made so that it can be given any 2 valid point as an argument so that I can make resetting the board simple. The check for if the square is adjacent is made in the play() method loop where i check the difference between a point and a player coordinate and see if it is within -1 and 1. Here I can use the coordinates of the player, which are gonna be from 5, to 405, in increments of 100, and I set the parameters (which will be numbers from 0-4 each) so that they will match the same coordinates as a player would have on each square. After I set the coordinates, I then move the player within the class as it is still recognized as a _BBox object.
- the is_clicked method is simple and just checks if the object itself was clicked, this includes the invisibile corners of the oval, and I make it so each player is the same size as each square so that the program doesn't get confused if i click an occupied square in the wrong place.
 - check_coordinates simply retrieves the player coordinates as the object is still recognized as a _BBox object.

Splash Screen and Score Board:
 - for the splash screen and scoreboard I create functions that open separate windows that initialize button objects and rectangles. If the button objects are clicked, which will be specified as "Play" and "Quit" in the splash and "Replay" and "Quit" in the scoreboard, they will either play the game, or exit the program. In the case of the "Play again" in the scoreboard, it will only save the player 1 and player 2 scores, which are global variables that are added into as when a player wins a game, the scoreboard function is given the argument 1 or 2, which corresponds to which player won the game. Once a player wins, and the program was clicked to "Replay" the variables will be saved until the entire game is closed again, which resets the scoreboard. 

CLASSES

Icebreaker: This class sets up the game board and implements the game logic.
- __init__: 
	:purpose: initializes all the game objects and attributes, including window size, colours, status messages, players, buttons, and various other aspects that are 	integral to the game mechanics.
        :parameters:
        self - instance - instance of icebreaker object
        width - int - integer representing the width of the window
        height - int - integer representing the height of the window
        title - str - name of the window on the left side of the title bar
        :return: None

- play:
	:purpose: runs game logic by using mouse clicks: awaits for a mouseclick. 
        If the quit button is clicked, displays "BYE BYE !!" and awaits another mouseclick to close the window and terminate the program
        If the reset button is clicked, displays "RESET" and returns to top of the GUI loop
        checks a current player between player_1 and player_2, which is initially set as player_1
	for each player, has a similar loop that ascertains for valid clicks first (valid, adjacent clicks to player location), and then allows players to break any 	unoccuied, unbroken square before switching players and restarting the loop
        :parameters:
        self - instance - instance of icebreaker object
        :return: None

 - switch_players:
        :purpose: switches the player being controlled during the main play method
        :parameters:
        self - instance - instance of icebreaker object
        desired_player - object - player_object that is desired to be switched to
        :return: different player object
 - can_move:
	:purpose: checks if player can move in the 8 squares around them
        :parameters:
        self - instance - instance of icebreaker game
        player - player being checked for if they can move or not
        :return:
        True or False of if they can move or not

Board: This class contains the game board: a two-dimensional list of lists of board squares.
- __init__:
	:purpose: initializes a board of squares (rows and columns) representing ice blocks in the icebreaker game window
        :parameters:
        self - instance - instance of game board to create
        win - window - window in which game board squares are drawn
        :return: None

- break_ice:
	:purpose: breaks an iceblock (drawing a new rectangle) on the clickpoint using specified coordinates, then adds it into the broken_ice stack
        :parameters:
        self - instance - instance of board
        click_point - checkMouse() method return - a coordinate extracted from a mouseclick within the window
        rect - rectangle object that represents iceblock
        :return: None

- clear_ice:
	:purpose: clears all the broken ice blocks and undraws them
        :parameters:
        self - instance of board object
        :return: None

- is_broken_ice:
	:purpose: checks if the clickpoint clicked broken ice.
        :parameters: 
        self - instance - instance of game board
        click_point - checkMouse() method return - point object at which the mouse was clicked
        :return: True if the broken ice piece was clicked, and None if ice list is empty or otherwise

- in_rectangle:
	:credits: I took this function from the house_demo1.py file we were shown in class and did some tweaking to achieve my desired results.
        :purpose: this function determines whether the mouse is clicked inside a rectangle
        :parameters: 
        click_point - point object at which the mouse was clicked
        rect - rectangle object to be checked for mouse click
        return: True if click-point is inside rect, False otherwise

- in_rect_list:
	:purpose: checks through an entire list to see if a rectangle has been clicked. if so, returns the list coordinates of the click
        :parameters:
        self - instance - instance of the object used
        click_point - checkMouse() method return - a coordinate extracted from a mouseclick within the window
        rect_list - list - 2 dimensional list of rectangle objects that have different points represented on the window.
        :return:
        x and y coordinates representing the row and column of the rectangle clicked, or None

Button: A button object (rectangle) that is initialized and drawn into the game. has a method to check if the specified button has been clicked or not
- __init__:
	:purpose: creates a button in the window (rectangle object) that can be accessed and labeled for specific functions
        :parameters:
        self - instance - instance of button object
        win - window - window that the button will be displayed on
        center - int - center point for the button/rectangle
        width - int - width of button
        height - int - height of button
        label - label of button
        :return: None
- is_clicked:
	:purpose: checks if the specified button object is clicked or not
        :parameters:
        self - instance - instance of button object
        click_point - checkMouse() method return - coordinates from checkMouse() that checks the click point of a mouse button within the window
        :return: True or False whether the button object was clicked or not

Player: This class creates a player that is initialized and drawn into the icebreaker game. contains methods that allow it to move to a specific location, check its own coordinates, and check if the player object has been clicked or not.
- __init__:
	:purpose: initializes the player class, the attributes of the circle representing the player, and the location of the player object
        :parameters:
        self - instance - instance of player object
        win - window - window that the player will be displayed on
        center - int - center point for the player/oval
        width - int - width of player
        height - int - height of player
        color - color of player
        :return: None

- move_player:
	:purpose: moves a player object on the window towards the desired end location.
        :parameters:
        self - instance - instance of player
        x_end - x coordinate of the end point of where to move the 
        :return: None

- player_clicked:
	:purpose: checks if a player was clicked
        :parameters:
        self - instance - instance of player
        click_point - checkMouse() method return - coordinates from checkMouse() that checks the click point of a mouse button within the window
        :return: True if the player instance was clicked, False if not.

- check_coordinates:
	:purpose: returns the coordinates of the player object
        :parameters:
        self - instance - instance of player
        :return: x and y coordinates of player

FUNCTIONS:

__main__() function: Creates an Icebreaker object and starts playing the game. Game starts automatically when the code is run, and is played fully without inputs and only with mouse clicks.

 - splash_screen:
	:purpose: creates the splash screen of the icebreaker game, along with the title, creator name, additional info, and a play game and close button.
    	Internally contains the game object and commences it after clicking the play button
    	:parameters: None
    	:return: None

 - score_board:
	:purpose: creates the scoreboard window that appears after the icebreaker game has finished. contains the total game scores of player 1 and player 2,
    	and adds to them based on the argument integer given (1 for player 1, 2 for player 2)
    	:parameters:
   	player_num - int - determines whether a point should be given to player one or player two based on the integer given
    	:return: None