 # Tic Tac Toe 
 
A simple console based 'tic tac toe' game that has a player vs player mode as well as a player vs Ai mode.

---

# [Quick Play](https://replit.com/@AgniveshSp/tic-tac-toe)

## Instructions
*How to run the program and play the game.*

1. Run **main.py**
1. Press 'y' to play against computer, 'n' to play against another player.
1. Enter a number ranging from 1-9 to mark your marker.
1. When the game ends press 'y' for a rematch or 'n' to exit.
---

## Game Mechanics

When the program starts, it asks the user whether they want to play against a computer or another player. If the user chooses to play with another player, the program assigns the 'X' mark to player 1 and 'O' mark to player 2. By convention, 'X' moves first in the first round. Each box on the game board is denoted by a number from 1 to 9. These numbers are keys in a dictionary where 'X' and 'O' are assigned.

After each player's move, the program checks if any three markers in a horizontal row, vertical row, or diagonal row match. If they do, the program announces the game is over and prompts for a rematch. If it's the second round, then 'O' plays first. If any of the plots a player chooses have already been used, the program asks them to pick another plot.

If the player chooses to play against the computer, both the user and computer are assigned a random player_id, which can be 'P1' or 'P2'. By convention, 'P1' moves first. If it's the AI's turn, a random box is marked with an 'X' and prompts the user for their move. If the user marks the center plot and the AI does not mark one of the corner plots, it means victory is guaranteed for the user. So, using randomization, the AI chooses a corner plot to mark its next move. The AI prioritizes its moves as follows: first, it checks for a winning move where two plots are marked with the AI's marker and one plot is empty. Next, it looks for defensive moves where two plots are marked with the user's marker and one plot is empty. The AI will occupy this plot to prevent the user from winning. Then, it checks for offensive moves, where the AI scans all possible directions for any plots with two empty boxes to mark its next move. Finally, if none of the conditions are met, the AI randomly chooses an empty plot and marks it. To make the AI more human-like, it is given a random error chance. This means that instead of defending and preventing the user from winning, the AI may make a plot randomly chosen between offense and random boxes. Each move is followed by checking arrays to see if any of the three markers match. If the game is over and all plots are filled with a marker, the game ends in a draw.

---

## Documentation

###  Modules

<details><summary>main</summary>
 
#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main.is\_game\_over(_mode_, _player\_id_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/main.py#L9)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Checks if the current game has ended.*
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Args:**<br>
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode (Logic): A subclass which inherits from `Logic`. (`VsPlayer , VsAi`)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;player\_id (str): A string representing the id of the player.(“P1”,”P2”)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`True` if the game is won or ended in draw.



#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main.player\_vs\_player()[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/main.py#L33C17-L33C17)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Function that handles the player vs player gameplay.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: ``None``

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;main.player\_vs\_ai()[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/main.py#L73)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Function that handles the player vs ai gameplay.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: ``None``

</details>


<details><summary>logic</summary>

### &nbsp;&nbsp;&nbsp;&nbsp;class logic.Logic[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L6)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: `object`


#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;player\_turn(_player\_id_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L16)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Takes user inputs and assigns them to an empty plot on the game board.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**player\_id** (str): A string representing the id of the player.(“P1”,”P2”) :type player\_id: str

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: ``None``

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;game\_status\_check(_player\_id_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L45)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Checks if the markers on the board satisfy the condition for a win or draw.* <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*If three of the markers match horizontally,vertically or diagonally then condition is met.*<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*If there are no more empty plots left on the board then game ends in a draw.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**player\_id** (_str_) – A string representing the id of the player.(“P1”,”P2”)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns the winning marker, ‘X’ or ‘O’. If the game ends in a draw, return ‘Draw’.

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update\_dictionary\_array()[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L81)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Updates horizontal,vertical and diagonal arrays with updated values from the board.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: `None`


#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reset\_board()[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L140)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Resets the Tic Tac Toe board (`board.dict`) to its default stateand resets the `p_list`.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: `None`

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;score\_update(_mark_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L118)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Updates the score of the first player to match three markers.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**mark** – either “X”, “O” or `None`. Default is `None`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A tuple consisting of player 1 score and player 2 score.


### &nbsp;&nbsp;&nbsp;&nbsp;_class_ logic.VsAi(_ai\_id_, _player\_id_, _corner\_prob_, _defence\_prob_, _offense\_prob_, _random\_prob_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L162)


> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: [`Logic`](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L6 "logic.Logic")

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Instantiates a subclass object of Logic class.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Args:**<br>


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ai_id(str): Ai id , "P1" or "P2".


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;player_id(str): Player id , "P1" or "P2".


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;corner_prob(float): Probability that Ai marks a corner after player marks the center plot. Min-0, Max-1.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;defence_prob(float): Probability that Ai prioritizes a defensive move. Min-0, Max-1.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offense_prob(float): Probability that Ai prioritizes a offensive move. Min-0, Max-1.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_prob(float): Probability that Ai prioritizes a random move. Min-0, Max-1.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Raises**:


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;COUNTERROR : defence_prob,offense_prob and random_prob values should add upto 1.





#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ai\_turn()[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L240)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Method responsible for ai moves on the board.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: `None`



#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;linear\_check(_linear\_list_, _start\_key_, _iteration\_increment_, _row\_start\=0_, _row\_increment\=0_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L281)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Checks horizontal or vertical arrays and appends the moves that Ai can make to suitable lists.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**linear\_list** (_list_) – A horizontally or vertically sliced list from the game board.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**start\_key** (_int_) – The number in which the iteration starts.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**iteration\_increment** (_int_) – Increment after each loop.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**row** (_int__,_ _optional_) –Starting number of the row. Default is 0.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**row\_increment** (_int__,_ _optional_) – Number in which rows are incremented. Default is 0.
    

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: `None`

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;diagonal\_check(_diagonal\_list_, _start\_key_, _iteration\_increment_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L352)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Checks diagonal arrays and appends the moves that Ai can make to suitable lists.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**diagonal\_list** (_list_) – A diagonally sliced list from the game board.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**start\_key** (_int_) – The number in which the iteration starts.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**iteration\_increment** (_int_) – Increment after each loop.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: `None`


### &nbsp;&nbsp;&nbsp;&nbsp;_class_ logic.VsPlayer[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L155)
> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: [`Logic`](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/logic.py#L6 "logic.Logic")

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Instantiates a subclass object of Logic class.*

</details>
<details><summary >game_display</summary>

### &nbsp;&nbsp;&nbsp;&nbsp;class game\_display.GameDisplay(_vs\_mode_, _ai\_is\_p2\=False_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/game_display.py#L26)

> #### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bases: `object`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Instantiates a GameDisplay object.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Args:**<br>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode(str):Current gamemode. 'pvp' for player vs player and 'ai' for player vs ai.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ai_is_p2(bool):``True`` if Ai is playing 'O'. Default is ``False``

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_static_ console\_clear()[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/game_display.py#L53)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Static method that clears the console and adds the title art.* 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns: `None`





#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;_static_ welcome\_screen()[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/game_display.py#L42)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Welcome screen displayed once when the program starts.Is a static method.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:`None`

#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;display\_board(_board\_dict_, _scoretuple\=(0, 0)_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/game_display.py#L63)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Configures and Displays the game board on the console.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**board\_dict** (_dict_) – Dictionary representing the game board.
    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**scoretuple** (_tuple_) – Tuple with 0th element being player 1 score and 1st element being player 2 score.
    

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:`None`



#### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;game\_result(_marker_)[\[source\]](https://github.com/agniveshsp/tic-tac-toe/blob/4e6909977e19aba44b6de52f4b0c79028daccbf6/game_display.py#L115)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Prints the game result on to the console.*

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Parameters:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**marker** (_str_) – “X”,”O” or “Draw”.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Returns:`None`

</details>

--- 

## Flowchart 
<details><summary>Class Diagrams</summary>
<br><br>



![classdiagarram](https://github.com/agniveshsp/tic-tac-toe/assets/67277625/2e952476-22f2-4bc7-8d4d-6b69daef0ec4)<?xml version="1.0" encoding="UTF-8"?>

</details>

 
<details><summary>main</summary>
 
<details><summary>&nbsp;&nbsp;&nbsp;&nbsp;start</summary>
 

![mainrun](https://github.com/agniveshsp/tic-tac-toe/assets/67277625/de9bbac5-d9a7-4b6c-b283-07fb93ee6d38)<?xml version="1.0" encoding="UTF-8"?>


</details>

<details><summary>&nbsp;&nbsp;&nbsp;&nbsp;functions</summary>
 
![mainfunc](https://github.com/agniveshsp/tic-tac-toe/assets/67277625/ba10c58b-d166-4767-9df2-049e7f9a265b)<?xml version="1.0" encoding="UTF-8"?>

</details>

</details>


<details><summary>logic</summary>
 
![logicclass](https://github.com/agniveshsp/tic-tac-toe/assets/67277625/c63da9c9-79f6-4b3c-a033-ebb25023244d)<?xml version="1.0" encoding="UTF-8"?>
 
 
</details>



<details><summary>gamedisplay</summary>
 
![gamedisplay](https://github.com/agniveshsp/tic-tac-toe/assets/67277625/44a559f2-6683-439c-9352-47519b9c0b5d)

 
</details>

 
 
 
