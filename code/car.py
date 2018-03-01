class Car(object):
    def __init__(self):
        self.rides = []
        self.target = (0,0)
        self.remainingSteps = 0

    def is_free(self):
        return not self.remainingSteps

    def choose_ride(self,step,rides):
        max = -1
        ret = None
        for ride in rides:
            aux_score = get_score(ride)
            if max < aux_score
                max = aux_score
                ret = ride
        return ret
            
        
                  
