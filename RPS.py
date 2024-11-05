import random

#this is the list of opponent plays
opponent_play = []

def player(prev_play):

    # the strategy is to find repetitive patterns on 2, 3, 4 and 5 moves
    # and predict the next move based on these patterns
    global opponent_play
    opponent_play.append(prev_play)
    guess = random.choice(('R', 'P', 'S'))

    # for each repetitive pattern, we reward the last opponent play in the following dict
    most_moves = {'R': 0, 'P': 0, 'S': 0}

    # check for repetitive 2 moves
    if len(opponent_play)>2:
        last_two = opponent_play[-2:]
        for i in range(len(opponent_play)-2):
            if opponent_play[i:i+2] == last_two:
                most_moves[opponent_play[i+2]] += 1

    # check for repetitive 3 moves
    if len(opponent_play)>3:
        last_three = opponent_play[-3:]
        for i in range(len(opponent_play)-3):
            if opponent_play[i:i+3] == last_three:
                most_moves[opponent_play[i+3]] += 1

    # check for repetitive 4 moves
    if len(opponent_play)>4:
        last_four = opponent_play[-4:]
        for i in range(len(opponent_play)-4):
            if opponent_play[i:i+4] == last_four:
                most_moves[opponent_play[i+4]] += 1

    # check for repetitive 5 moves
    if len(opponent_play)>5:
        last_five = opponent_play[-5:]
        for i in range(len(opponent_play)-5):
            if opponent_play[i:i+4] == last_five:
                most_moves[opponent_play[i+5]] += 1

    # the move with the most rewards is our closest predict
    predict = max(most_moves, key=lambda k: int(most_moves[k]))

    # we play the beater in front of our predict
    if predict == 'R':
        guess = 'P'
    if predict == 'P':
        guess = 'S'
    if predict == 'S':
        guess = 'R'

    # simply reset the history of the player after each 1000 times, because that's the test counter
    if len(opponent_play)%1000 == 0:
        opponent_play = []

    return guess
