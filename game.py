import numpy as np
import random


class Game:

    def __init__(self, size):
        self.size = size
        self.size2 = size * size
        self.board = [None for x in range(self.size2)]
        self.player_one = "one"
        self.player_two = "two"
        self.player_one_points = 0
        self.player_two_points = 0

    def move(self, player, position):
        self.board[position] = player
        self.check_row(position, player)
        self.check_column(position, player)
        self.check_diagonal_one(position, player)
        self.check_diagonal_two(position, player)

    def move_random(self, player):
        self.move(player, random.randint(0, self.size2))

    def count_points(self, player, points):
        if player == self.player_one:
            self.player_one_points += points
        elif player == self.player_two:
            self.player_one_points += points
        pass

    def check_row(self, position, player):
        count = position % self.size
        row_start = count * self.size - 1
        row_end = row_start + self.size - 1
        for x in range(row_start, row_end):
            if self.board[x] is None:
                return False
        self.count_points(player, self.size)
        return True

    def check_column(self, position, player):
        n = position
        while 0 <= n:
            n -= self.size
        n += self.size
        while n < self.size2:
            if self.board[n] is None:
                return False
            n += self.size
        self.count_points(player, self.size)
        return True

    def check_diagonal_one(self, position, player):
        x = position % self.size
        y = position / self.size
        b = y - x
        points = 0
        for i in range(0, self.size2):
            x_check = i & self.size
            y_check = i / self.size
            if (y_check == x_check + b):
                points += 1
                if self.board[i] is None:
                    return False
        self.count_points(player, points)
        return True

    def check_diagonal_two(self, position, player):
        x = position % self.size
        y = position / self.size
        b = y - x
        points = 0
        for i in range(0, self.size2):
            x_check = i & self.size
            y_check = i / self.size
            if y_check == b - x_check:
                points += 1
                if self.board[i] is None:
                    return False
        self.count_points(player, points)
        return True

    def print_board(self):
        c = 0
        while c < len(self.board):
            print("| ", end=" ")
            for r in range(0, self.size):
                print(str(self.board[c + r]) + " | ", end=" ")
            c += self.size
            print("\n", end="")


game = Game(5)

game.print_board()
player_one = "one"
game.move(player_one, 1)
print("")
game.print_board()

game.move(player_one, 5)
game.print_board()
print("")
print(str(game.player_one_points))
