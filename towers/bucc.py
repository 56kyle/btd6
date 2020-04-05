from tower import Tower


class Bucc(Tower):
    name = "bucc"
    keybind = "c"
    range_radius = 323
    aquatic = True
    width = 87
    height = 75

    def __init__(self, placement=None):
        super(Bucc, self).__init__(Bucc, placement)
