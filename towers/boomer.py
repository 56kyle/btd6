from tower import Tower


class Boomer(Tower):
    name = "boomer"
    keybind = "w"
    range_radius = 231
    width = 76
    height = 66

    def __init__(self, placement=None):
        super(Boomer, self).__init__(Boomer, placement)
