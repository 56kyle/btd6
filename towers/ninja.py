from tower import Tower


class Ninja(Tower):
    name = "ninja"
    keybind = "d"
    range_radius = 215
    width = 65
    height = 57

    def __init__(self, placement=None):
        super(Ninja, self).__init__(Ninja, placement)
