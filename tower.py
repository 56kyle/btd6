

from pyautogui import *


class Tower:
    """A tower in btd6"""
    towers = []
    name = None
    keybind = None
    range_radius = None
    width = None
    height = None

    def __init__(self, tower_type, placement=None):
        self.placement = None
        self.name = tower_type.name
        self.range_radius = tower_type.range_radius
        self.keybind = tower_type.keybind
        self.width = tower_type.width
        self.height = tower_type.height
        try:
            self.aquatic = tower_type.aquatic
        except AttributeError:
            self.aquatic = False
        if not placement:
            placement = position()
        self.placement = self.place(placement)
        if not self.placement:
            press('escape')
            del self
        else:
            Tower.towers.append(self)

    @classmethod
    def row(cls, length, start=None, inverse=None):
        if not start:
            start = position()
        for i in range(length):
            change = i * cls.width
            if inverse:
                change = change*-1
            Tower(cls, Point(start.x + change, start.y))

    @classmethod
    def column(cls, length, start=None, inverse=None):
        if not start:
            start = position()
        for i in range(length):
            change = i * cls.width
            if inverse:
                change = change*-1
            Tower(cls, Point(start.x, start.y + change))

    @classmethod
    def box(cls, width, height, start=None, inverse=None):
        if not start:
            start = position()

        for i in range(height):
            change = i * cls.height
            if inverse:
                change = change*-1
            cls.row(width, Point(start.x, start.y + change))

    def can_be_placed(self, placement):
        moveTo(placement)
        if placement.x > 1100:
            measuring_point = Point(placement.x - (self.range_radius - 2), placement.y)
        else:
            measuring_point = Point(placement.x + (self.range_radius - 2), placement.y)

        before = pixel(measuring_point.x, measuring_point.y)
        press(self.keybind)
        after = pixel(measuring_point.x, measuring_point.y)
        if (after[0] - before[0]) >= 8:
            return False
        else:
            return True

    def place(self, placement):
        if self.can_be_placed(placement):
            click(placement)
        else:
            return False
        return placement

    def remove(self):
        click(self.placement)
        press('backspace')
