

class Gear:
    """ Understands being a speficic combring = ination of chainring and cog"""

    def __init__(self, chainring, cog):
        self._chainring = chainring
        self._cog = cog

    def ratio(self):
        return self._chainring / self._cog


if __name__ == "__main__":
    gear = Gear(52, 11)
    print(gear.ratio())
    gear = Gear(30, 27)
    print(gear.ratio())
