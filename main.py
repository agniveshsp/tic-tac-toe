import random
import sys

from game_display import GameDisplay
from logic import VsPlayer, VsAi, Logic
import os

# Game Over?
def is_game_over(mode, player_id):
    """
    Checks if the current game has ended.

    Args:
        mode (Logic):A subclass which inherits from ``Logic``.(``VsPlayer , VsAi``)
sphin        player_id (str):A string representing the id of the player.("P1","P2")

    Returns:
        ``True`` if the game is won or ended in draw.
    """

    game_status = mode.game_status_check(player_id=player_id)
    game_display.display_board(mode.board_dict, scoretuple=mode.score_update(mark=game_status))
    if game_status != None:  # gamestatus != mark
        game_display.game_result(marker=game_status)
        return True
    else:
        return False




#########--Player vs Player--###################
def player_vs_player():

    """
    Function that handles the player vs player gameplay.

    Returns:
        ``None``

    """

    global turns
    global p1_moves_first
    # Resets dictionary and list.
    vs_player.reset_board()
    game_display.display_board(vs_player.board_dict, scoretuple=(vs_player.p1_score, vs_player.p2_score))

    while ingame:
        if p1_moves_first == True:  # Alternate first play.
            vs_player.player_turn(player1_id)
            if is_game_over(mode=vs_player, player_id=player1_id):
                break

        vs_player.player_turn(player2_id)
        if is_game_over(mode=vs_player, player_id=player2_id):
            break
        p1_moves_first = True

    resume = input("Rematch?(y/n)").lower()
    if resume == "y":
        turns += 1
        if turns % 2 != 0:
            p1_moves_first = True
        else:
            p1_moves_first = False
        return player_vs_player()
    else:
        return


######## Player VS Ai ##########################
def player_vs_ai():
    """
    Function that handles the player vs ai gameplay.

    Returns:
        ``None``

    """
    global turns
    global ai_moves_first
    vs_ai.reset_board()

    while ingame:
        if ai_moves_first == True:
            vs_ai.ai_turn()
            if is_game_over(mode=vs_ai, player_id=vs_ai.ai_id):
                break
        else:
            game_display.display_board(vs_ai.board_dict, scoretuple=(vs_ai.p1_score, vs_ai.p2_score))

        vs_ai.player_turn(vs_ai.player_id)
        if is_game_over(mode=vs_ai, player_id=vs_ai.player_id):
            break
        ai_moves_first = True

    resume = input("Rematch?(y/n)").lower()
    if resume == "y":
        turns += 1
        if vs_ai.ai_id == 'P1':
            if turns % 2 == 0:
                ai_moves_first = False
            elif turns % 2 != 0:
                ai_moves_first = True

        elif vs_ai.ai_id == 'P2':
            if turns % 2 == 0:
                ai_moves_first = True
            elif turns % 2 != 0:
                ai_moves_first = False

        return player_vs_ai()
    else:
        return


################################################


ai_corner_probability = .9

#####probabilty of the ai making a wrong move. all should add upto 1
ai_defence_probability = .90
ai_offense_probability = .05
ai_random_probability = .05
###################################


player1_id = "P1"
player2_id = "P2"
ingame = True
turns = 1
p1_moves_first = True
ai_moves_first = True



GameDisplay.welcome_screen()

vs = input("play against computer? (y/n)?").lower()
if vs == 'n':  # Constructs a player v player game display and a vs_Player game logic.
    game_display = GameDisplay(vs_mode="pvp")
    vs_player = VsPlayer()
    player_vs_player()

elif vs=='y':  # Constructs a player v Ai game display and a vs_ai game logic.
    player_id_list = ["P1", "P2"]
    player_id = random.choice(player_id_list)
    ai_id = [id for id in player_id_list if id != player_id][0]
    if ai_id == "P2":
        ai_moves_first = False
        game_display = GameDisplay(vs_mode="ai", ai_is_p2=True)
    else:
        game_display = GameDisplay("ai", ai_is_p2=False)

    vs_ai = VsAi(ai_id=ai_id, player_id=player_id,
                 corner_prob=ai_corner_probability, defence_prob=ai_defence_probability,
                 offense_prob=ai_offense_probability, random_prob=ai_random_probability)
    player_vs_ai()
else:
    sys.exit()