import random

class TicTacToe:

    def __init__(self):
        self.board = [" ", "X", "O",
                      " ", "O", " ",
                      "X", "X", " "]

    def printBoard(self):
        print("""
          {} | {} | {}
         -----------
          {} | {} | {}
         -----------
          {} | {} | {}
        """.format(*self.board))

    def getMovesFromPlayer(self, player):
        # Get all moves made by a given player
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == player:
                moves.append(i)
        return moves

    def checkForWinner(self):
        winningCombos = ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6])

        for player in ("X", "O"):
            positions = self.getMovesFromPlayer(player)
            for combo in winningCombos:
                win = True
                for pos in combo:
                    if pos not in positions:
                        win = False
                if win:
                    return player

    def returnWinner(self):
        if self.checkForWinner() == "X":
            return "X"
        elif self.checkForWinner() == "O":
            return "O"
        elif self.isGameOver() == True:
            return "Nobody"

    def getAvailableMoves(self):
        # Return empty spaces on the board"
        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def makeMove(self, position, player):
        # Make a move on the board
        self.board[position] = player

    def isGameOver(self):
        if self.checkForWinner() != None:
            return True
        for i in self.board:
            if i == " ":
                return False
        return True

    def minimax(self, node, depth, player):
        # Recursively analyze every possible game state and choose the best move location.
        if depth == 0 or node.isGameOver():
            if node.checkForWinner() == "X":
                return 0
            elif node.checkForWinner() == "O":
                return 100
            else:
                return 50

        if player == "O":
            bestValue = 0
            for move in node.getAvailableMoves():
                node.makeMove(move, player)
                moveValue = self.minimax(node, depth-1, changePlayer(player))
                node.makeMove(move, " ")
                bestValue = max(bestValue, moveValue)
            return bestValue

        if player == "X":
            bestValue = 100
            for move in node.getAvailableMoves():
                node.makeMove(move, player)
                moveValue = self.minimax(node, depth-1, changePlayer(player))
                node.makeMove(move, " ")
                bestValue = min(bestValue, moveValue)
            return bestValue

def changePlayer(player):
    if player == "X":
        return "O"
    else:
        return "X"

def make_best_move(board, depth, player):
    # helper function to get the best possible move
    neutralValue = 50
    choices = []
    for move in board.getAvailableMoves():
        board.makeMove(move, player)
        moveValue = board.minimax(board, depth-1, changePlayer(player))
        board.makeMove(move, " ")

        if moveValue > neutralValue:
            choices = [move]
            break
        elif moveValue == neutralValue:
            choices.append(move)
    # print("choices: ", choices)

    nextMove = ""

    if len(choices) > 0:
        nextMove = random.choice(choices)
    else:
        nextMove = random.choice(board.getAvailableMoves())

    print("nextMove from player " + str(player) + " is " + str(nextMove))

    return nextMove


game = TicTacToe()
game.printBoard()

while game.isGameOver() == False:
    #print("Computer choosing move...")
    ai_move = make_best_move(game, -1, "O")
    game.makeMove(ai_move, "O")
    #game.printBoard()

    if game.isGameOver() == True:
        break

    #print("Computer choosing move...")
    ai_move = make_best_move(game, -1, "X")
    game.makeMove(ai_move, "X")
    #game.printBoard()

print("Game Over. " + game.returnWinner() + " Wins")