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
    freecars = 0
    try:
        for step in range(steps):
            print(step, freecars, file=sys.stderr)
            freecars = 0
            for car in cars:
                if not rides:
                    break
                if car.is_free():
                    freecars += 1
                    ride = car.choose_ride(
                        step,
                        rides[:lookahead],
                        bonus,
                        params
                    )

                    if ride is not None:
                        rides.remove(ride)

                    if freecars > 1:
                        break
                    
                car.tick()
            if not rides:
                break

    except KeyboardInterrupt:
        pass

    for car in cars:
        car.output()
