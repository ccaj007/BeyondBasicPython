class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def value(self):
        """ The value (in knuts) of all coins in this WizCoin object """
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def weightInGrams(self):
        return (self.galleons * 31.103) + (self.sickles + 11.34) + (self.knuts * 5.0)

