import random
import sys



class Logic():


    def __init__(self):
        """
          Instantiates a Logic object.
        """
        self.p1_score = 0
        self.p2_score = 0

    def player_turn(self, player_id):
        """
        Takes user inputs and assigns them to an empty plot on the game board.
        Args:
            player_id(str): A string representing the id of the player.("P1","P2")

        Returns:
            None

        """
        if player_id == "P1":
            marker = 'X'
        elif player_id == "P2":
            marker = 'O'
        entry = input(f"Enter a number to mark your {marker}:")
        if entry.isnumeric():
            entry=int(entry)
            if entry in self.p_list:
                self.p_list.remove(entry)
                self.board_dict[entry] = marker
                return None
            else:

                print("Enter a valid square.")
                return self.player_turn(player_id)
        else:
            print("Enter a valid square.")
            return self.player_turn(player_id)

    def game_status_check(self, player_id):
        """
        Checks if the markers on the board satisfy the condition for a win or draw.
        If three of the markers match horizontally,vertically or diagonally then condition is met.
        If there are no more empty plots left on the board then game ends in a draw.

        Args:
            player_id(str): A string representing the id of the player.("P1","P2")

        Returns:
            Returns the winning marker, 'X' or 'O'.If the game ends in a draw, return 'Draw'.

        """
        self.update_dictionary_array()
        if player_id == "P1":
            marker = 'X'
        elif player_id == "P2":
            marker = 'O'
        for array in self.horizontal:
            if self._array_count_is_three(array, marker) == True:
                return marker

        for array in self.vertical:
            if self._array_count_is_three(array, marker) == True:
                return marker
        # for diagonal
        if self._array_count_is_three(self.diagonal_one, marker) == True:
            return marker
        elif self._array_count_is_three(self.diagonal_two, marker) == True:
            return marker

        elif not self.p_list:
            return "Draw"

        return None

    def update_dictionary_array(self):
        """
        Updates horizontal,vertical and diagonal arrays with updated values from the board.

        Returns:
            ``None``

        """

        self.horizontal=[[self.board_dict[1], self.board_dict[2], self.board_dict[3]],
                         [self.board_dict[4], self.board_dict[5], self.board_dict[6]],
                         [self.board_dict[7], self.board_dict[8], self.board_dict[9]]]

        self.vertical = [[self.board_dict[1], self.board_dict[4], self.board_dict[7]],
                         [self.board_dict[2], self.board_dict[5], self.board_dict[8]],
                         [self.board_dict[3], self.board_dict[6], self.board_dict[9]]]

        self.diagonal_one = [self.board_dict[1], self.board_dict[5], self.board_dict[9]]
        self.diagonal_two = [self.board_dict[3], self.board_dict[5], self.board_dict[7]]

    def _array_count_is_three(self, array, marker):
        """
        Simply checks if  the number of occurrence in a given list is three.

        Args:
            array(list):A list than consists of three elements.
            marker(str):The marker to check for three occurrence.  "X" or "O".

        Returns:
            ``True`` if the array has three markers of the same type.

        """
        if array.count(marker) == 3:
            return True
        else:
            return False

    def score_update(self,mark):
        """
        Updates the score of the first player to match three markers.

        Args:
            mark: either "X", "O" or ``None``. Default is ``None``

        Returns:
            A tuple consisting of player 1 score and player 2 score.


        """

        if mark == 'X':
            self.p1_score += 1
        elif mark == "O":
            self.p2_score += 1
        else:#no change in current score.
            return (self.p1_score, self.p2_score)

        return (self.p1_score, self.p2_score)

    def reset_board(self):
        """
        Resets the Tic Tac Toe board (``board.dict``) to its default stateand resets the ``p_list``.
        Returns:
           ``None``

        """

        self.board_dict = {1:" ", 2:" ", 3:" ",
                           4:" ", 5:" ", 6:" ",
                           7:" ", 8:" ", 9:" ", }

        self.p_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class VsPlayer(Logic):
    """
    Instantiates a subclass of Logic class.
    """
    pass


class VsAi(Logic):
    def __init__(self, ai_id,player_id,corner_prob,defence_prob,offense_prob,random_prob):
        """
        Instantiates a subclass of the Logic class.
        Args:
            ai_id(str): Ai id , "P1" or "P2".
            player_id(str): Player id , "P1" or "P2".
            corner_prob(float): Probability that Ai marks a corner after player marks the center plot. Min-0, Max-1.
            defence_prob(float):Probability that Ai prioritizes a defensive move. Min-0, Max-1.
            offense_prob(float):Probability that Ai prioritizes a offensive move. Min-0, Max-1.
            random_prob(float):Probability that Ai prioritizes a random move. Min-0, Max-1.
        Raises:
            COUNTERROR :defence_prob,offense_prob and random_prob values should add upto 1.

        """
        super().__init__()
        self.ai_id=ai_id
        self.player_id=player_id
        # probabilty of the ai making a corner move.
        self.ai_corner_probability = corner_prob
        #####probabilty of the ai making a wrong move. all should add upto 1##
        self.ai_defence_probability = defence_prob
        self.ai_offense_probability = offense_prob
        self.ai_random_probability = random_prob
        ###################################
        if self.ai_defence_probability+self.ai_offense_probability+self.ai_random_probability!=1:
            print(self.ai_defence_probability+self.ai_offense_probability+self.ai_random_probability)
            sys.exit('COUNTERROR:defence_prob,offense_prob and random_prob values should add upto 1.')


        if ai_id=="P1":
            self.ai_marker="X"
            self.player_marker="O"
        else:
            self.ai_marker="O"
            self.player_marker = "X"

    def get_ai_moves(self):
        """
        Compares and checks various arrays extracted from the game board and returns a list of possible moves the ai can make along with the type of move.
        Returns:
            A tuple which consists of a list of possible moves and the type of move.

        """
        self.ai_win_boxes = []
        self.ai_defence_boxes = []
        self.ai_offense_boxes = []
        self.ai_random_boxes=[]

        
        self.update_dictionary_array()

        self.linear_check(linear_list=self.horizontal, start_key=1, iteration_increment=1)
        self.linear_check(linear_list=self.vertical, start_key=1, iteration_increment=3, row_start=-1, row_increment=1)
        self.diagonal_check(diagonal_list=self.diagonal_one, start_key=1, iteration_increment=4)
        self.diagonal_check(diagonal_list=self.diagonal_two, start_key=3, iteration_increment=2)

        print(f"defence boxes={self.ai_defence_boxes},"
              f"offense boxes={self.ai_offense_boxes}"
              f"win boxes= {self.ai_win_boxes}",
              f"random_box={self.ai_random_boxes}")

        if self.ai_win_boxes:
            return (self.ai_win_boxes,"win")
        elif self.ai_defence_boxes:
            if (self.ai_offense_boxes or self.ai_random_boxes) : #Returns a defensive move with a .25% chance of move being random.
                move_list= random.choices([self.ai_defence_boxes,self.ai_offense_boxes,self.ai_random_boxes],[self.ai_defence_probability,self.ai_offense_probability,self.ai_random_probability])[0]
                if not move_list: #check if move_list is empty
                    return (self.ai_defence_boxes, "defence")
                print(f"ai defencee= {move_list}")
                return (move_list,"defence")

        elif self.ai_offense_boxes:
            return (self.ai_offense_boxes,"offense")
        else:
            return (self.ai_random_boxes,"random")


    def ai_turn(self):
        """
        Method responsible for ai moves on the board.
        Returns:
            ``None``

        """

        ai_possible_moves=self.get_ai_moves()   #returns possible AI moves. with label
        print(ai_possible_moves)


        if ai_possible_moves[1] == "random":
            if 5 in ai_possible_moves[0] and len(ai_possible_moves[0])>1: #Already plotted
                corner_list=[corner for corner in ai_possible_moves[0] if corner in [1,3,7,9]] #If not corner then game already lost.
                non_corner_list=[non_corner for non_corner in ai_possible_moves[0] if non_corner in [2,4,6,8]]

                #Initial loosing, if player marks center and ai marks a non-corner then AI lost.
                if corner_list and non_corner_list:
                    selected=random.choices([corner_list,non_corner_list],[self.ai_corner_probability,1-self.ai_corner_probability])[0]
                elif non_corner_list:
                    selected=non_corner_list
                elif corner_list:
                    selected=corner_list

                ai_move = random.choice(selected)

            elif 5 not in ai_possible_moves[0]:
                selected = ai_possible_moves[0]
                ai_move = random.choice(selected)

        else:
            ai_move = random.choice(ai_possible_moves[0])


        #Remove plotted number from p_list
        self.p_list.remove(ai_move)
        #Plot Marker to selected plot.
        self.board_dict[ai_move] = self.ai_marker
        return None

    def linear_check(self,linear_list, start_key, iteration_increment, row_start=0, row_increment=0):
        """
        Checks horizontal or vertical arrays and appends the moves that Ai can make to suitable lists.

        Args:
            linear_list(list): A horizontally or vertically sliced list from the game board.
            start_key(int): The number in which the iteration starts.
            iteration_increment(int): Increment after each loop.
            row(int,    optional)=Row starting number to process vertical arrays.Default is 0.
            row_increment(int, optional):Number in which rows are incremented. Default is 0.

        Returns:
            ``None``


        """

        row = row_start
        row_increment = row_increment
        key = start_key

        for array in linear_list:
            row += row_increment
            ai_count = 0
            player_count = 0
            null_count = 0

            for mark in array:
                if mark == self.ai_marker:
                    ai_count += 1
                elif mark == self.player_marker:
                    player_count += 1
                else:
                    null_count += 1

            # win for 0 a
            if ai_count == 2 and null_count == 1:
                for mark in array:
                    if mark == " ":
                        dict_key = row + key
                        if dict_key not in self.ai_win_boxes and dict_key in self.p_list:
                            self.ai_win_boxes.append(dict_key)
                    key += iteration_increment

            elif ai_count == 1 and null_count == 2:
                for mark in array:
                    if mark == " ":
                        dict_key = row + key
                        if dict_key not in self.ai_offense_boxes and dict_key in self.p_list:
                            self.ai_offense_boxes.append(dict_key)
                    key += iteration_increment

            elif player_count == 2 and null_count == 1:
                for mark in array:
                    if mark == " ":
                        dict_key = row + key
                        if dict_key not in self.ai_defence_boxes and dict_key in self.p_list:
                            self.ai_defence_boxes.append(dict_key)
                    key += iteration_increment

            else:  # Assign empty boxes to random box list
                for mark in array:
                    if mark == " ":
                        dict_key = row + key
                        if dict_key not in self.ai_random_boxes and dict_key in self.p_list:
                            self.ai_random_boxes.append(dict_key)
                    key += iteration_increment

            if row_increment != 0:  # Vertical list has row increment of 1, horizontal does not.
                key = start_key

    def diagonal_check(self,diagonal_list, start_key, iteration_increment):
        """
        Checks diagonal arrays and appends the moves that Ai can make to suitable lists.

        Args:
            diagonal_list(list): A diagonally sliced list from the game board.
            start_key(int): The number in which the iteration starts.
            iteration_increment(int): Increment after each loop.

        Returns:
            ``None``

        """
        ai_count = 0
        player_count = 0
        null_count = 0
        key = start_key

        for mark in diagonal_list:
            if mark == self.ai_marker:
                ai_count += 1
            elif mark == self.player_marker:
                player_count += 1
            else:
                null_count += 1

        if ai_count == 2 and null_count == 1:
            for mark in diagonal_list:
                if mark == " ":
                    if key not in self.ai_win_boxes and key in self.p_list:
                        self.ai_win_boxes.append(key)
                key += iteration_increment

        elif ai_count == 1 and null_count == 2:
            for mark in diagonal_list:
                if mark == " ":
                    if key not in self.ai_offense_boxes and key in self.p_list:
                        self.ai_offense_boxes.append(key)
                key += iteration_increment

        elif player_count == 2 and null_count == 1:
            for mark in diagonal_list:
                if mark == " ":
                    if key not in self.ai_defence_boxes and key in self.p_list:
                        self.ai_defence_boxes.append(key)
                key += iteration_increment

        else:
            for mark in diagonal_list:
                if mark == " ":
                    if key not in self.ai_random_boxes and key in self.p_list:
                        self.ai_random_boxes.append(key)
                key += iteration_increment