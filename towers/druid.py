from tower import Tower


class Druid(Tower):
    name = "druid"
    keybind = "g"
    range_radius = 188
    width = 76
    height = 66

    def __init__(self, placement=None):
        super(Druid, self).__init__(Druid, placement)
