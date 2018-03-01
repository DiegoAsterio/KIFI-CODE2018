from collections import namedtuple

Problem = namedtuple('Map', ['rows', 'cols', 'fleet', 'bonus', 'steps', 'rides'])
Position = namedtuple('Position', ['row', 'col'])
Ride = namedtuple('Ride', ['ride_id', 'start', 'finish', 't_start', 't_finish'])


class SimulationParameters(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def compute_score(self, distance, waiting_time, duration, bonus):
        return (self.a * distance + self.b * waiting_time
                + self.c * duration + self.d * bonus)


def dist(pos1, pos2):
    return abs(pos1.rows - pos2.rows) + abs(pos1.cols - pos2.cols)
