import os

# helper function to print the board
def printBoard(board):
        # clear the console after every move
        os.system("clear")
        print(board["1"] + "|" + board["2"] + "|" + board["3"])
        print("-+-+-")
        print(board["4"] + "|" + board["5"] + "|" + board["6"])
        print("-+-+-")
        print(board["7"] + "|" + board["8"] + "|" + board["9"])

 # helper function to print the winner
def printWinner(player):
    print("Game Over: " + player + " hat gewonnen!")


class Game:
    def __init__(self):
        # create the board
        self.board = {  "1": " ", "2": " ", "3": " ",
                        "4": " ", "5": " ", "6": " ",
                        "7": " ", "8": " ", "9": " "}
        # initial player
        self.player = "X"
        # initial play count
        self.count = 0

    def start(self):
        # each iteration is a move
        for _ in range(10):
            # print the fresh board
            printBoard(self.board)

            # ask the player for the next move
            print(self.player, "ist an der Reihe.")
            move = input("Welches Feld willst du besetzen? ")

            # if the place on the board is empty, make the move
            if self.board[move] == " ":
                self.board[move] = self.player
                self.count += 1
            else:
                print(
                    "Dieses Feld ist bereits besetzt. Welches Feld willst du besetzen?")
                continue

            # The min acmount of moves to get a winner is 5
            # So if we have more than 5 moves, check if there is a winner
            if self.count >= 5:
                if self.board["7"] == self.board["8"] == self.board["9"] != " ":
                    printBoard(self.board)
                    printWinner(self.player)
                    break
                elif self.board["4"] == self.board["5"] == self.board["6"] != " ":
                    printBoard(self.board)
                    printWinner(self.player)
                    break
                elif self.board["1"] == self.board["2"] == self.board["3"] != " ":
                    printBoard(self.board)
                    printWinner(self.player)
                    break
                elif self.board["1"] == self.board["4"] == self.board["7"] != " ":
                    printBoard(self.board)
                    printWinner(self.player)
                    break
                elif self.board["2"] == self.board["5"] == self.board["8"] != " ":
                    printBoard(self.board)
                    printWinner(self.player)
                    break
                elif self.board["3"] == self.board["6"] == self.board["9"] != " ":
                    printBoard(self.board)
                    printWinner(self.player)
                    break
                elif self.board["7"] == self.board["5"] == self.board["3"] != " ":
                    printBoard(self.board)
                    printWinner(self.player)
                    break
                elif self.board["1"] == self.board["5"] == self.board["9"] != " ":
                    printBoard(self.board)
                    printWinner(self.player)
                    break

            # If neither X nor O wins and the board is full, it is a tie
            if self.count == 9:
                print("Game Over: Unentschieden!")

            # If the game goes on, switch the player
            if self.player == "X":
                self.player = "O"
            else:
                self.player = "X"
