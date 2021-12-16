# Final-Project-of-Software-Carpentry
Instruction of Eating Snake Game
1.	The instruction of game operation
Key	Function
Up	Snake moves in the direction of up
Down	Snake moves in the direction of down
Left	Snake moves in the direction of left
Right	Snake moves in the direction of right
Space	Stop/continue the game
F1	Accelerate
F2	Slow down
F3	Start/stop difficult mode
Esc	Exit the game

2.	Flow of the game
At the beginning of the game, a randomly-positioned snake with a length of 5 (snake head red and snake body green), a randomly-positioned food (red), and a randomly-positioned wall with a maximum length of 5 (black) will be generated.

When the game is running, you can use the keys to control the movement of the snake to eat the food. Each food is eaten, the length of the snake body increases by 1. After the body length of snake increased to 10 (after eating 10 foods), and the speed of the snake increases by one level, and a wall whose length is up to 5 will also be added to the game to increase the difficulty of the game. If the snake bites itself or hits the wall while moving, it will die, and the game will automatically exit.

3.	Coding part explanation
There would be three parts of the coding: window.py, snake.py and window.py. Each part has different functions and game.py is the running code of the game. 

In the window.py file, I define the functions to provide an entrance to pygame (this package needs to be installed). Clear function is to create the game board (fill the screen with background color). Rect and circle are functions to draw square and circle on the game board. Lastly, the event function is to judge the conditions of the game and stop or continue the game.

In the snake.py file, this module mainly focuses on snake itself, such as defining the body and movement of snakes. Functions of draw and show is to draw the snake and make it appear on the game board. Move function is to define the movement of the snake. 

Game.py is the running file of this game. Firstly, use game_run function to define the pathway of the snake. Then in the main part, a new pathway is created and make changes by detecting the keys pressing events.
![image](https://user-images.githubusercontent.com/90734795/146447479-d3632715-5e86-404d-b3e9-2eeaadf76da4.png)

