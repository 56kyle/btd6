from tower import Tower


class Village(Tower):
    name = "village"
    keybind = "k"
    range_radius = 215
    width = 119
    height = 103

    def __init__(self, placement=None):
        super(Village, self).__init__(Village, placement)
