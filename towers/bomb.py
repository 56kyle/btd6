from tower import Tower


class Bomb(Tower):
    name = "bomb"
    keybind = "e"
    range_radius = 215
    width = 76
    height = 66

    def __init__(self, placement=None):
        super(Bomb, self).__init__(Bomb, placement)
