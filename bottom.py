class Bottom:
    def __init__(self):
        self.ordinates = list()
        self.abscisses = list()

    def is_row_completed(self, bottom_group):
        completed = list()
        for y in self.ordinates:
            if self.ordinates.count(y) == 10:
                completed.append(y)
        for row in completed:
            for sprite in bottom_group:
                if sprite.get_position()[1] == row:
                    bottom_group.remove(sprite)
                    del sprite
                    # переместить ряды вниз

    def add(self, bottom_group):
        for sprite in bottom_group:
            self.ordinates.append(sprite.get_position()[1])
            self.abscisses.append(sprite.get_position()[0])
