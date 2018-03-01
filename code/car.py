from data import Position, dist
import sys


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
        duration = dist(ride.start, ride.finish)
        bonus = bonus * (waiting_time >= distance)

        if ride.t_finish < current_time + duration + distance:
            return -float("inf")

        return sim_params.compute_score(distance, waiting_time, duration, bonus)

    def tick(self):
        if self.remaining_steps:
            self.remaining_steps -= 1

    def choose_ride(self, step, rides, bonus, sim_params):
        def ride_score(ride):
            return self.get_score(ride, step, bonus, sim_params)

        #print(list(map(ride_score, rides)), file=sys.stderr)
        candidate = max(rides, key=ride_score)

        if self.get_score(candidate, step, bonus, sim_params) > -float('inf'):
            self.rides.append(candidate)

            waiting_time = max(
                0,
                candidate.t_start - (step + dist(self.target, candidate.start))
            )

            self.remaining_steps = (dist(self.target, candidate.start)
                                    + waiting_time
                                    + dist(candidate.start, candidate.finish))
            self.target = candidate.finish
            return candidate

        return None


    def output(self):
        print('{} {}'.format(
            len(self.rides),
            ' '.join(
                str(ride.ride_id) for ride in self.rides
            )
        ))
