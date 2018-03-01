from collections import namedtuple

Problem = namedtuple('Map', ['rows', 'cols', 'fleet', 'bonus', 'steps', 'rides'])
Position = namedtuple('Position', ['row', 'col'])
Ride = namedtuple('Ride', ['start', 'finish', 't_start', 't_finish'])

R, C, F, N, B, T = [ int(x) for x in input().split() ]


rides = []

for _ in range(N):
    a, b, x, y, s, f = [ int(x) for x in input().split() ]
    ride = Ride(
        t_start=s,
        t_finish=f,
        start=Position(row=a, col=b),
        finish=Position(row=x, col=y)
    )

    rides.append(ride)

problem = Problem(rows=R, cols=C, fleet=F, bonus=B, steps=T, rides=rides)
    
print(problem)
