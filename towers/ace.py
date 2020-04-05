from tower import Tower


class Ace(Tower):
    name = "ace"
    keybind = "v"
    range_radius = 118
    width = 152
    height = 85

    def __init__(self, placement=None):
        super(Ace, self).__init__(Ace, placement)
