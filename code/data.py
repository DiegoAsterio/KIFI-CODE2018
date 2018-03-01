from collections import namedtuple

Problem = namedtuple('Map', ['rows', 'cols', 'fleet', 'bonus', 'steps', 'rides'])
Position = namedtuple('Position', ['row', 'col'])
Ride = namedtuple('Ride', ['ride_id', 'start', 'finish', 't_start', 't_finish'])
