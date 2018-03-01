class Car(object):
    def __init__(self):
        self.rides = []
        self.target = (0,0)
        self.remainingSteps = 0

    def is_free(self):
        return not self.remainingSteps

    def choose_ride(self,step,rides):
        scores = [getScores(ride) :  ride in rides]
        max = -1
        pos = 0
        for i in range(scores.size() ):
            if max < scores[i]:
                max = scores[i]
                pos = i
        return rides[pos]
            
        
                  
