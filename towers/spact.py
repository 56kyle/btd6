from tower import Tower


class Spact(Tower):
    name = "spact"
    keybind = "j"
    range_radius = 183
    width = 87
    height = 75

    def __init__(self, placement=None):
        super(Spact, self).__init__(Spact, placement)
