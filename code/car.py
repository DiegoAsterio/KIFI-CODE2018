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

    def choose_ride(self,step,rides):
        max = -1
        ret = None
        for ride in rides:
            aux_score = get_score(ride)
            if max < aux_score
                max = aux_score
                ret = ride
        return ret

    def output(self):
        print('{} {}'.format(len(self.rides), ' '.join(str(ride.ride_id) for ride self.rides))
