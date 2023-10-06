#Michael Williamson
#Tic Tac Toe practice
#7/17/2020

player1Score: int = 0
player2Score: int = 0
firstMove: int = 1

person = input("Are you Misa? ")
if person == "yes":
    while True:
        print("1|N|3")
        print("-+-+-")
        print("W|5|E")
        print("-+-+-")
        print("7|S|9")
        print("Here are your options for Tic Tac Toe. Be careful of the wind. Please select the number for the "
              "location you wish to move.")
        print("SCORES   Player 1 - " + str(player1Score) + "    Player 2 - " + str(player2Score))
        currentTurn = "X"
        currentBoard = {'1': ' ', 'N': ' ', '3': ' ',
                        'W': ' ', '5': ' ', 'E': ' ',
                        '7': ' ', 'S': ' ', '9': ' '}


        def printBoard(board):
            print(board['1'] + "|" + board['N'] + "|" + board['3'])
            print("-+-+-")
            print(board['W'] + "|" + board['5'] + "|" + board['E'])
            print("-+-+-")
            print(board['7'] + "|" + board['S'] + "|" + board['9'])


        i: int = 0
        while True:
            printBoard(currentBoard)
            if i >= 9:
                break
            if i == 0:
                move = input("Player " + str(firstMove) + " you are " + currentTurn + ", where would you like to go? ")
            else:
                move = input(currentTurn + ", where would you like to go? ")
            if currentBoard[move] == ' ':
                currentBoard[move] = currentTurn
                if currentTurn == "X":
                    currentTurn = "O"
                else:
                    currentTurn = "X"
            else:
                print("Spot already taken")
                i -= 1
            if currentBoard['1'] == currentBoard['N'] == currentBoard['3'] != ' ':
                print(currentBoard['1'] + " is the Winner!!!")
                if currentBoard['1'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['1'] == currentBoard['5'] == currentBoard['9'] != ' ':
                print(currentBoard['1'] + " is the Winner!!!")
                if currentBoard['1'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['1'] == currentBoard['W'] == currentBoard['7'] != ' ':
                print(currentBoard['1'] + " is the Winner!!!")
                if currentBoard['1'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['N'] == currentBoard['5'] == currentBoard['S'] != ' ':
                print(currentBoard['N'] + " is the Winner!!!")
                if currentBoard['N'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['3'] == currentBoard['5'] == currentBoard['7'] != ' ':
                print(currentBoard['3'] + " is the Winner!!!")
                if currentBoard['3'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['3'] == currentBoard['E'] == currentBoard['9'] != ' ':
                print(currentBoard['3'] + " is the Winner!!!")
                if currentBoard['3'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['W'] == currentBoard['5'] == currentBoard['E'] != ' ':
                print(currentBoard['W'] + " is the Winner!!!")
                if currentBoard['W'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['7'] == currentBoard['S'] == currentBoard['9'] != ' ':
                print(currentBoard['7'] + " is the Winner!!!")
                if currentBoard['7'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif i >= 9:
                print("Cats game.")
            i += 1

        print("Good game!!!")
        replay: str = input("Type \'yes\' or \'Y\' to play again?")
        if replay != 'yes' and replay != 'Y':
            break
        if firstMove == 1:
            firstMove = 2
        else:
            firstMove = 1
else:
    while True:
        print("1|2|3")
        print("-+-+-")
        print("4|5|6")
        print("-+-+-")
        print("7|8|9")
        print("Here are your options for Tic Tac Toe. Please select the number for the location you wish to move.")
        print("SCORES   Player 1 - " + str(player1Score) + "    Player 2 - " + str(player2Score))
        currentTurn = "X"
        currentBoard = {'1': ' ', '2': ' ', '3': ' ',
                        '4': ' ', '5': ' ', '6': ' ',
                        '7': ' ', '8': ' ', '9': ' '}


        def printBoard(board):
            print(board['1'] + "|" + board['2'] + "|" + board['3'])
            print("-+-+-")
            print(board['4'] + "|" + board['5'] + "|" + board['6'])
            print("-+-+-")
            print(board['7'] + "|" + board['8'] + "|" + board['9'])


        i: int = 0
        while True:
            printBoard(currentBoard)
            if i >= 9:
                break
            if i == 0:
                move = input("Player " + str(firstMove) + " you are " + currentTurn + ", where would you like to go? ")
            else:
                move = input(currentTurn + ", where would you like to go? ")
            if int(move) < 1 or int(move) > 9:
                move = input("Not a valid spot!" + currentTurn + ", where would you like to go? ")
            if currentBoard[move] == ' ':
                currentBoard[move] = currentTurn
                if currentTurn == "X":
                    currentTurn = "O"
                else:
                    currentTurn = "X"
            else:
                print("Spot already taken")
                i -= 1
            if currentBoard['1'] == currentBoard['2'] == currentBoard['3'] != ' ':
                print(currentBoard['1'] + " is the Winner!!!")
                if currentBoard['1'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['1'] == currentBoard['5'] == currentBoard['9'] != ' ':
                print(currentBoard['1'] + " is the Winner!!!")
                if currentBoard['1'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['1'] == currentBoard['4'] == currentBoard['7'] != ' ':
                print(currentBoard['1'] + " is the Winner!!!")
                if currentBoard['1'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['2'] == currentBoard['5'] == currentBoard['8'] != ' ':
                print(currentBoard['2'] + " is the Winner!!!")
                if currentBoard['2'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['3'] == currentBoard['5'] == currentBoard['7'] != ' ':
                print(currentBoard['3'] + " is the Winner!!!")
                if currentBoard['3'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['3'] == currentBoard['6'] == currentBoard['9'] != ' ':
                print(currentBoard['3'] + " is the Winner!!!")
                if currentBoard['3'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['4'] == currentBoard['5'] == currentBoard['6'] != ' ':
                print(currentBoard['4'] + " is the Winner!!!")
                if currentBoard['4'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif currentBoard['7'] == currentBoard['8'] == currentBoard['9'] != ' ':
                print(currentBoard['7'] + " is the Winner!!!")
                if currentBoard['7'] == 'X' and firstMove == 1:
                    player1Score += 1
                else:
                    player2Score += 1
                break
            elif i >= 9:
                print("Cats game.")
            i += 1

        print("Good game!!!")
        answer: str = input("Type \'yes\' or \'y\' to play again?")
        replay = answer.lower()
        if replay != 'yes' and replay != 'y':
            break
        if firstMove == 1:
            firstMove = 2
        else:
            firstMove = 1
