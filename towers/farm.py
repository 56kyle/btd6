from tower import Tower


class Farm(Tower):
    name = "farm"
    keybind = "h"
    range_radius = 215
    width = 162
    height = 141

    def __init__(self, placement=None):
        super(Farm, self).__init__(Farm, placement)
