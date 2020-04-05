from tower import Tower


class Mortar(Tower):
    name = "mortar"
    keybind = "n"
    range_radius = 161
    width = 119
    height = 103

    def __init__(self, placement=None):
        super(Mortar, self).__init__(Mortar, placement)
