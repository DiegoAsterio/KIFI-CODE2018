from data import Problem, Position, Ride, SimulationParameters
from algorithm import algorithm

content = open('../datasets/d_metropolis.in')
R, C, F, N, B, T = [ int(x) for x in content.readline().split() ]

rides = []

for i in range(N):
    a, b, x, y, s, f = [ int(x) for x in content.readline().split() ]
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
sim_parameters = SimulationParameters(-1, -1, 1, 10)
algorithm(problem, sim_parameters)
