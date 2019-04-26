import random

empty_window = [
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ']
        ]
Points = 0

class Game_2048:

    def __init__(self):
        self.Points = 0
        self.empty_window = [
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ']
        ]
        self.reset()
        self.empty_pos = []

    def start(self):
        self.reset()
        while True:
            self.window()

            enter = input('Command:')

            if enter == 'w':
                self.up()
            elif enter == 's':
                self.down()
            elif enter == 'a':
                self.left()
            elif enter == 'd':
                self.right()
            elif enter == 'r':
                self.reset()
                continue
            elif enter == 'q':
                exit('Quit')
            else:
                print('Wrong Command')
                continue
            if self.win():
                print('Win')
                break
            if self.game_over():
                print('Game over')
                break
            self.add_num()

    def window(self):
        window_str = """
        Points:{}
*-----*-----*-----*-----*
|{: ^5}|{: ^5}|{: ^5}|{: ^5}|
*-----*-----*-----*-----*
|{: ^5}|{: ^5}|{: ^5}|{: ^5}|
*-----*-----*-----*-----*
|{: ^5}|{: ^5}|{: ^5}|{: ^5}|
*-----*-----*-----*-----*
|{: ^5}|{: ^5}|{: ^5}|{: ^5}|
*-----*-----*-----*-----*

Command: w(up), s(down), a(left)
      d(right), r(reset),q(quit) 
        """.format(self.Points,
                   *self.empty_window[0],
                   *self.empty_window[1],
                   *self.empty_window[2],
                   *self.empty_window[3],
                   )
        print(window_str)

    def win(self):
        self.empty_pos = []
        for i in range(len(empty_window)):
            for j in range(len(empty_window)):
                if self.empty_window[i][j] == 2048:
                    return True
                elif self.empty_window[i][j] == ' ':
                    self.empty_pos.append((i, j))
        return False

    def game_over(self):
        flag = True
        if len(self.empty_window) == 0:
            for l in self.empty_window:
                for i in range(len(l)-1):
                    if l[i] == l[i+1]:
                        flag = False
            for l in self.right_turn(self.empty_window):
                for i in range(len(l)-1):
                    flag = False
        else:
            flag = False
        return flag

    def row_operation(self, row):
        global Points

        t = []
        for item in row:
            if item:
                t.append(item)

        new_row = []
        flag = True
        for i in range(len(t)):
            if flag:
                if i + 1 < len(t) and t[i] == t[i+1]:
                    new_row.append(t[i] + t[i])
                    flag = False
                else:
                    new_row.append(t[i])
            else:
                flag = True

        for k in range(len(row) - len(new_row)):
            new_row.append(' ')
        return new_row

    def up(self):
        self.left_turn()
        self.left()
        self.right_turn()

    def down(self):
        self.right_turn()
        self.left()
        self.left_turn()

    def left(self):
        global empty_window
        for i in range(len(self.empty_window)):
            self.empty_window[i] = self.row_operation(empty_window[i])

    def right(self):
        self.left_turn()
        self.up()
        self.right_turn()

    def right_turn(self):
        self.empty_window = [list(v)[::-1] for v in zip(*self.empty_window)]

    def left_turn(self):
        for i in range(3):
            self.right_turn()

    def add_num(self):
        if self.empty_pos:
            t = self.empty_pos.pop(random.randrange(len(self.empty_pos)))
            empty_window[t[0]][t[1]] = random.randrange(2, 5, 2)

    def reset(self):
        self.empty_window = [
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ']
        ]
        self.Points = 0
        while True:
            p1 = (random.randint(0, 3), random.randint(0, 3))
            p2 = (random.randint(0, 3), random.randint(0, 3))
            if p1 != p2:
                break
        self.empty_window[p1[0]][p1[1]] = random.randrange(2, 5, 2)
        self.empty_window[p2[0]][p2[1]] = random.randrange(2, 5, 2)



if __name__ == '__main__':
    game = Game_2048()
    game.start()







