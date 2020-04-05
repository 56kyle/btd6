from tower import Tower


class Sniper(Tower):
    name = "sniper"
    keybind = "z"
    range_radius = 107
    width = 65
    height = 57

    def __init__(self, placement=None):
        super(Sniper, self).__init__(Sniper, placement)
