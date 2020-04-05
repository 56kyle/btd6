from tower import Tower


class Tack(Tower):
    name = "tack"
    keybind = "r"
    range_radius = 123
    width = 65
    height = 57

    def __init__(self, placement=None):
        super(Tack, self).__init__(Tack, placement)
