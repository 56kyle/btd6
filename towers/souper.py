from tower import Tower


class Souper(Tower):
    name = "souper"
    keybind = "s"
    range_radius = 269
    width = 119
    height = 103

    def __init__(self, placement=None):
        super(Souper, self).__init__(Souper, placement)
