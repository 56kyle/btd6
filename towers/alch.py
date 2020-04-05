from tower import Tower


class Alch(Tower):
    name = "alch"
    keybind = "f"
    range_radius = 242
    width = 65
    height = 57

    def __init__(self, placement=None):
        super(Alch, self).__init__(Alch, placement)
