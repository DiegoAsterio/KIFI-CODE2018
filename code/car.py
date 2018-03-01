from data import Position

class Car(object):
    def __init__(self):
        self.rides = []
        self.target = Position(row=0, col=0)
        self.remainingSteps = 0

    def is_free(self):
        return not self.remainingSteps

    def tick(self):
        if self.remainingSteps:
            self.remainingSteps -= 1
