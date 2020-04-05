from tower import Tower


class Glue(Tower):
    name = "glue"
    keybind = "y"
    range_radius = 247
    width = 65
    height = 57

    def __init__(self, placement=None):
        super(Glue, self).__init__(Glue, placement)
