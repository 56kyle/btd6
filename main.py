from towers.dart import Dart
from towers.boomer import Boomer
from towers.bomb import Bomb
from towers.tack import Tack
from towers.ice import Ice
from towers.glue import Glue
from towers.sniper import Sniper
from towers.sub import Sub
from towers.bucc import Bucc
from towers.ace import Ace
from towers.heli import Heli
from towers.mortar import Mortar
from towers.wizard import Wizard
from towers.souper import Souper
from towers.ninja import Ninja
from towers.alch import Alch
from towers.druid import Druid
from towers.farm import Farm
from towers.spact import Spact
from towers.village import Village
from towers.engi import Engi

import time
from pyautogui import *
from tower import Tower

types = [
    Dart,
    Boomer,
    Bomb,
    Tack,
    Ice,
    Glue,
    Sniper,
    Sub,
    Bucc,
    Ace,
    Heli,
    Mortar,
    Wizard,
    Souper,
    Ninja,
    Alch,
    Druid,
    Farm,
    Spact,
    Village,
    Engi
]


def main():
    time.sleep(3)
    Dart.box(5, 4)
    print(Tower.towers)


if __name__ == '__main__':
    main()
