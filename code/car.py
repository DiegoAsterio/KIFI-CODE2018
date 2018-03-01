from data import Position

class Car(object):
    def __init__(self):
        self.rides = []
        self.target = Position(row=0, col=0)
        self.remaining_steps = 0

    def is_free(self):
        return not self.remaining_steps
    
    def get_score(self, ride, current_time, bonus, a, b, c, b):
        distance = dist(ride.start, self.target)
        waiting_time = max(ride.t_start - current_time, 0)
        duration = ride.t_finish - ride.t_start
        bonus = bonus * (waiting_time >= distance)
        
        if ride.t_finish < current_time + duration + distance:
            return -float("inf")
        
        return a * distance + b * waiting_time + c * duration + d * bonus

    def tick(self):
        if self.remaining_steps:
            self.remaining_steps -= 1

    def choose_ride(self,step,rides):
        ret = max(rides, key=lambda r: r.get_score(ride,step) )
        if (ret.get_score() > 0):
            self.rides.append(ret)
            waiting_time = max(0,ret.start - (step + dist(self.target,ret.start) ))
            self.remaining_steps = dist(self.target,ret.start) + waiting_time + dist(ret.start, ret.end)
            self.target = ret.finish
        
            return ret

        return None
