class Car(object):
    def __init__(self):
        self.rides = []
        self.target = (0,0)
        self.remainingSteps = 0

    def is_free(self):
        return not self.remainingSteps

    def tick(self):
        self.remainingSteps -= 1
