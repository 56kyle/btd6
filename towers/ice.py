from tower import Tower


class Ice(Tower):
    name = "ice"
    keybind = "t"
    range_radius = 123
    width = 65
    height = 57

    def __init__(self, placement=None):
        super(Ice, self).__init__(Ice, placement)
