from data import Position, dist


class Car(object):
    def __init__(self):
        self.rides = []
        self.target = Position(row=0, col=0)
        self.remaining_steps = 0

    def is_free(self):
        return not self.remaining_steps

    def get_score(self, ride, current_time, bonus, sim_params):
        distance = dist(ride.start, self.target)
        waiting_time = max(ride.t_start - current_time, 0)
        duration = ride.t_finish - ride.t_start
        bonus = bonus * (waiting_time >= distance)

        if ride.t_finish < current_time + duration + distance:
            return -float("inf")

        return sim_params.compute_score(distance, waiting_time, duration, bonus)

    def tick(self):
        if self.remaining_steps:
            self.remaining_steps -= 1

    def choose_ride(self,step,rides,bonus,sim_params):
        f = lambda r: self.get_score(r, step, bonus, sim_params)
        ret = max(rides, key=f) 
        if self.get_score(ret,step,bonus,sim_params) > 0:
            self.rides.append(ret)
            
            waiting_time = max(
                0,
                ret.t_start - (step + dist(self.target,ret.start))
            )

            self.remaining_steps = dist(self.target,ret.start) + waiting_time + dist(ret.start, ret.finish)
            self.target = ret.finish

            return ret

        return None


    def output(self):
        print('-- {} {}'.format(
            len(self.rides),
            ' '.join(
                str(ride.ride_id) for ride in self.rides
            )
        ))

