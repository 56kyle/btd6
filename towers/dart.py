from tower import Tower


class Dart(Tower):
    name = "dart"
    keybind = "q"
    range_radius = 172
    width = 65
    height = 57

    def __init__(self, placement=None):
        super(Dart, self).__init__(Dart, placement)
