from data import Problem, Position, Ride

Problem = namedtuple('Map', ['rows', 'cols', 'fleet', 'bonus', 'steps', 'rides'])
Position = namedtuple('Position', ['row', 'col'])
Ride = namedtuple('Ride', ['ride_id', 'start', 'finish', 't_start', 't_finish'])

R, C, F, N, B, T = [ int(x) for x in input().split() ]

rides = []

for i in range(N):
    a, b, x, y, s, f = [ int(x) for x in input().split() ]
    ride = Ride(
        ride_id=i,
        t_start=s,
        t_finish=f,
        start=Position(row=a, col=b),
        finish=Position(row=x, col=y)
    )

    rides.append(ride)

rides.sort(key=lambda ride: ride.t_start)

problem = Problem(rows=R, cols=C, fleet=F, bonus=B, steps=T, rides=rides)

print(problem)
