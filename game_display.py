import os

title_art="""
████████╗░██╗░█████╗░░░████████╗░█████╗░░█████╗░░░████████╗░█████╗░███████╗
╚══██╔══╝░██║██╔══██╗░░╚══██╔══╝██╔══██╗██╔══██╗░░╚══██╔══╝██╔══██╗██╔════╝
░░░██║░░░░██║██║░░╚═╝░░░░░██║░░░███████║██║░░╚═╝░░░░░██║░░░██║░░██║█████╗░░
░░░██║░░░░██║██║░░██╗░░░░░██║░░░██╔══██║██║░░██╗░░░░░██║░░░██║░░██║██╔══╝░░
░░░██║░░░░██║╚█████╔╝░░░░░██║░░░██║░░██║╚█████╔╝░░░░░██║░░░╚█████╔╝███████╗
░░░╚═╝░░░░╚═╝░╚════╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░░░░░╚═╝░░░░╚════╝░╚══════╝                                                                                                       
"""
player_art="""                                            
                         █▀▀▀▀▄          ▄▀█▀▀█
                         ▐███▄ ▀▄      ▄▀ ▄███▀
                           ▀█▓█▄ ▀▄  ▄▀ ▄█▓█▀
                             ▀█▓█▄ ▄▀  ▄█▓█▀
                                ██▓█▄ ▀█▀
                          ▄▄  ▄█▓███▓█▄ ▀▄  ▄▄
                           ██████▓█▀▀█▓██▓███▀
                           ▄█████▀    ▀█████▄
                         ▄████▀▀██    ██▀▀████▄
                      ▐█████                ▀████▌
                       ███▀                  ▀███▀
"""


class GameDisplay():
    def __init__(self,vs_mode,ai_is_p2=False):
        """
        Instantiates a GameDisplay object.

        Args:
            mode(str):Current gamemode. 'pvp' for player vs player and 'ai' for player vs ai.
            ai_is_p2(bool):``True`` if Ai is playing 'O'. Default is ``False``
        """

        self.mode=vs_mode
        self.p1_score=0  #X
        self.p2_score=0  #O
        self.ai_is_p2 = ai_is_p2

    @staticmethod
    def welcome_screen():
        """
        Welcome screen displayed once when the program starts.Is a static method.
        Returns:
            ``None``

        """
        GameDisplay.console_clear()
        print(player_art)
        
    @staticmethod
    def console_clear():
        """
        Static method that clears the console and adds the title art.
        Returns:
            ``None``

        """
        os.system('cls' if os.name == 'nt' else 'clear')
        print(title_art)

    def display_board(self,board_dict,scoretuple=(0,0)):
        """
        Configures and Displays the game board on the console.

        Args:
            board_dict(dict): Dictionary representing the game board.
            scoretuple(tuple):Tuple with 0th element being player 1 score and 1st element being player 2 score.


        Returns:
            ``None``

        """

        self.console_clear()
        bp=board_dict
        # scoretuple=kwargs.get("scoretuple",(0,0))
        if self.mode=="pvp":
            self.p1_score=scoretuple[0]
            self.p2_score=scoretuple[1]
            board = f"""
                          Player1:{self.p1_score} | Player2:{self.p2_score} 
                           *-----------------*
                           |  {bp[1]}  |  {bp[2]}  |  {bp[3]}  |
                           -------------------
                           |  {bp[4]}  |  {bp[5]}  |  {bp[6]}  |
                           -------------------
                           |  {bp[7]}  |  {bp[8]}  |  {bp[9]}  |
                           *-----------------*
                """
        else:
            if self.ai_is_p2:
                self.p1_score=scoretuple[0]
                self.p2_score=scoretuple[1]
            else:#Flip the scoreboard
                self.p1_score = scoretuple[1]
                self.p2_score = scoretuple[0]

            board = f"""
                             Player:{self.p1_score} | Ai:{self.p2_score} 
                           +-----------------+
                           |  {bp[1]}  |  {bp[2]}  |  {bp[3]}  |
                           -------------------
                           |  {bp[4]}  |  {bp[5]}  |  {bp[6]}  |
                           -------------------
                           |  {bp[7]}  |  {bp[8]}  |  {bp[9]}  |
                           +-----------------+
                       """

        print(board)
        return None

    def game_result(self,marker):
        """
        Prints the game result on to the console.

        Args:
            marker(str): "X","O" or "Draw".

        Returns:
            ``None``

        """
        if marker == "Draw":
            print("Game Draw!")
        else:
            print(f"{marker} WINS!")

