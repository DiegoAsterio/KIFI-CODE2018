LOOKAHEAD_RIDES = 3

def algorithm(problem):
    steps = problem.steps
    cars = [ Car() for _ in range(problem.fleet) ]
    rides = problem.rides
    lookahead = LOOKAHEAD_RIDES * problem.fleet
    bonus = problem.bonus

    for step in range(steps):
        for car in cars:
            if car.is_free():
                ride = car.choose_ride(
                    rides[:lookahead],
                    bonus
                )
                rides.remove(ride)
            
            car.tick()

    for car in cars:
        car.output()
