class Patterns:
    def __init__(self, num, string1):
        self.num = num
        self.string1 = string1

    def rect_pattern(self):
        for row in range(1, self.num+ 1):
            for j in range(1, self.num +1):
                print(self.string1, end ='')
            print()

    def right_triangle(self):
        for row in range(1, self.num + 1):
            for col in range(1, row + 1):
                print(self.string1, end=" ")
            print()

    def star_pattern(self):
        for row in range(1, self.num+1):
            for col in range(1, self.num - row + 1):
                print(end=" ")
            for col in range(1, row + 1):
                print(self.string1, end=" ")
            print()

    def inverse_star(self):
        for row in range(self.num, 0, -1):
            for col in range(1, self.num - row + 1):
                print(end=" ")
            for col in range(1, row + 1):
                print(self.string1, end=" ")

            print()


p = Patterns(5, '*')
p.rect_pattern()
p.star_pattern()
p.inverse_star()
p.right_triangle()
