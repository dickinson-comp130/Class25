import random

"""
A program that plays a 2-player version of the dice game Pig.
"""

def get_choice():
    """ Read and return the player's choice to roll or stand.
        If the input is other than R or S, ask again.
    """
    choice = input('[R]oll or [S]tand: ')
    
    while (choice != 'R') and (choice != 'S'):
        print(choice + ' is not an option.')
        choice = input('[R]oll or [S]tand: ')
        
    return choice
    
def roll_die():
    """ Roll a six sided die and return the result. This function may not
        strictly be necessary, but it helps with readability in the 
        turn function.
    """
    return random.randint(1,6)

def turn(player, cur_total):
    """ Run one turn for the indicated player '1' or '2' who has cur_total points
        when starting the turn.  This function returns the number of points accumulated
        on this turn.
    """
    turn_total = 0
    roll = 0
    choice = 'R'
    
    while (choice == 'R') and (roll != 1) and (turn_total + cur_total < 100):

        roll = roll_die()
        
        if (roll != 1):
            print('Player ' + player + ' rolls a ' + str(roll))
            turn_total = turn_total + roll
            print('Player ' + player + ' turn score ' + str(turn_total) + 
                  ', total score ' + str(cur_total))
            
            if (turn_total + cur_total < 100):
                choice = get_choice()
                
        else:
            print('Player ' + player + ' rolls a 1 - Bust!')
            turn_total = 0
            
    return turn_total

def print_winner(p1_score, p2_score):
    """ Print the winner of the game based on the scores. """
    if p1_score > p2_score:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
        
#        
# Main Program Below
#

print("Let's play Pig!")

player1_score = 0
player2_score = 0

while (player1_score < 100) and (player2_score < 100):
    
    # Run player 1's turn
    print('')
    player1_turn_score = turn('1', player1_score)        
    player1_score = player1_score + player1_turn_score
    print('Player 1 total score: ' + str(player1_score))
    
    if (player1_score < 100):
        # Run player 2's turn
        print('')
        player2_turn_score = turn('2', player2_score)        
        player2_score = player2_score + player2_turn_score
        print('Player 2 total score: ' + str(player2_score))
    
print('')
print("Game over!")

# Print the winner.
print_winner(player1_score, player2_score)