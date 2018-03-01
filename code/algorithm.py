from car import Car
import sys
from random import randint

LOOKAHEAD_RIDES = 3

def algorithm(problem, params):
    steps = problem.steps
    cars = [ Car() for _ in range(problem.fleet) ]
    rides = problem.rides
    lookahead = LOOKAHEAD_RIDES * problem.fleet
    bonus = problem.bonus

    for step in range(steps):
        print(step, file=sys.stderr)
        for car in cars:
            if not rides:
                break
            if car.is_free() and randint(1, 5) == 1:
                ride = car.choose_ride(
                    step,
                    rides[:lookahead],
                    bonus,
                    params
                )

                if ride is not None:
                    rides.remove(ride)
            
            car.tick()
        if not rides:
            break

    for car in cars:
        car.output()
