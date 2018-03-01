class Car(object):
    def __init__(self):
        self.rides = []
        self.target = (0,0)
        self.remainingSteps = 0

    def is_free(self):
        return not self.remainingSteps
    
    def get_score(self, ride, current_time, bonus):
        distance = dist(ride.start, self.target)
        waiting_time = max(ride.t_start - current_time, 0)
        duration = ride.t_finish - ride.t_start
