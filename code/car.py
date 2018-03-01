from data import Position

class Car(object):
    def __init__(self):
        self.rides = []
        self.target = Position(row=0, col=0)
        self.remainingSteps = 0

    def is_free(self):
        return not self.remainingSteps
    
    def get_score(self, ride, current_time, bonus):
        distance = dist(ride.start, self.target)
        waiting_time = max(ride.t_start - current_time, 0)
        duration = ride.t_finish - ride.t_start

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
