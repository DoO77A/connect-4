# checks if the user's input is correct if not it recurses until it gets right input
def user_input():

    print("please enter a number from 1 to 7")
    player = input().replace(" ", "")

    # if the input isn't a number it will recurse
    if not player.isdigit():

        print("not a valid number please try again")
        return user_input()

    player = int(player)

    # if the input is out of bounds it will recurse
    if player not in range(1, 8):

        print("number out of range please try again")
        return user_input()

    if player in full_columns:

        print("this column is full please try another one")
        return user_input()

    return player


# replaces the number in the table with the symbol of the user (X if player 1 and O if player 2)
def play(table, player_1, symbol):

    player = user_input()

    # while the spot in this row is full it'll check the next row
    for x in range(5, -1, -1):

        if table[x][player * 2 - 1] == " ":

            table[x] = table[x][:player * 2 - 1] + symbol + table[x][player * 2:]
            player_1.append(player + x * 7)
            player_1 = sorted(player_1)

            # if the column is full it'll add it to a full_columns of full columns
            if x == 0:
                full_columns.append(player)

            break

    return table, player_1


# checks if one of the two players won and prints who is it or a draw if there's none and there's no more plays
def check_winner(player_1, player_2, full_columns, table, winner):

    # checks in the whole table if there's 4 in a row vertical, horizontal or diagonal
    for i in player_1:

        h = 1
        v = 1
        d = 1
        _d = 1

        for k in player_1:

            if k - i == 1 * h:
                h += 1

            if k - i == 7 * v:
                v += 1

            if k - i == 6 * d and (k % 7) - (i % 7) == d:
                d += 1

            if k - i == 8 * _d:
                _d += 1

        if h == 4 or v == 4 or d == 4 or _d == 4:

            break

    # if a user won then it prints that he won then asks if he wants to continue or quit
    if h == 4 or v == 4 or d == 4 or _d == 4:

        print("player " + winner + " wins")
        print("type 1 to continue and 0 to quit")
        player = input().replace(" ", "")

        # while the input is wrong it will keep asking for new input
        while player != "1" and player != "0":

            print("invalid input please try again")
            print("type 1 to continue and 0 to quit")
            player = input().replace(" ", "")

        # if the player wants to continue it resets all the variables to their original value
        if player == "1":

            table = ["| | | | | | | |",
                     "| | | | | | | |",
                     "| | | | | | | |",
                     "| | | | | | | |",
                     "| | | | | | | |",
                     "| | | | | | | |"]
            full_columns = []
            player_1 = []
            player_2 = []
            return table, full_columns, player_1, player_2
        
        # if the user doesn't want to play again it will reset only one variable which will make the game loop end
        else:

            return table, full_columns, player_1, []
    
    # checks if full_columns is empty then it returns so the program doesn't crash
    if full_columns == []:

        return table, full_columns, player_1, player_2
    
    # if the full_columns has 7 elements that means that there is no available play and it prints draw
    if len(full_columns) == 7:

        print("\tDraw")
        print("type 1 to continue and 0 to quit")
        player = input().replace(" ", "")

        while player != "1" and player != "0":

            print("invalid input please try again")
            print("type 1 to continue and 0 to quit")
            player = input().replace(" ", "")

        if player == "1":

            table = ["| | | | | | | |",
                     "| | | | | | | |",
                     "| | | | | | | |",
                     "| | | | | | | |",
                     "| | | | | | | |",
                     "| | | | | | | |"]
            full_columns = []
            player_1 = []
            player_2 = []
            return table, full_columns, player_1, player_2

        else:

            return table, full_columns, player_1, []


# the game table, the numbers to access each column, the full columns, player 1 and player 2's score
table = ["| | | | | | | |",
         "| | | | | | | |",
         "| | | | | | | |",
         "| | | | | | | |",
         "| | | | | | | |",
         "| | | | | | | |"]
last = "|1|2|3|4|5|6|7|"
full_columns = []
player_1 = []
player_2 = []

# game loop
while True:
    
    # prints the game table
    for i in table:

        print(i)

    print(last+"\n")
    print("first player's turn")
    table, player_1 = play(table, player_1, "X")
    table, full_columns, player_1, player_2 = check_winner(player_1, player_2, full_columns, table, "1")
    
    # if player_1 is reset that means that player 1 won and he wants to play again
    if player_1 == []:

        continue
    
    # if player_2 is reset that means that player 1 won and he wants to quit
    elif player_2 == [] and len(player_1) > 1:

        break

    for i in table:

        print(i)

    print(last+"\n")
    print("second player's turn")
    table, player_2 = play(table, player_2, "O")
    table, full_columns, player_2, player_1 = check_winner(player_2, player_1, full_columns, table, "2")

    # if player_1 is reset that means that player 2 won and he wants to quit
    if player_1 == [] and player_2 != []:

        break