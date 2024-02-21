#Functional
def flatten(d):
    result = sorted(d)
    return result

#1. This function doesn't changee the incoming data. The data is sorted and saved to results.
#2. This is a pure function. It does not produce or rely on side effects. Its output purely depends on its input.
#3. This is not a higher function. It doesn't accept nor returns a function.
#4. I don't believe it would've been easier in another programming style. 
#5. This is helpful because you'll always get the same output for the same input.  

#Object Oriented Prompt
class Podracer:
    def __init__(self, max_spreed, condition, price):
        self.max_speed = max_spreed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"
        return self.condition

class AnakinsPod(Podracer):
    def __init__(self, max_spreed, condition, price):
        super().__init__(max_spreed, condition, price)
    def boost(self):
        return self.max_speed * 2
    
class SebulbasPod(Podracer):
    def __init__(self, max_spreed, condition, price):
        super().__init__(max_spreed, condition, price)
    def flame_jet(self, pod):
        pod.condition = "trashed" 
           
print(flatten([9,2,4,1,5,8]))

my_pod = Podracer(100, "trashed", 4000)
print(my_pod.repair())

new_pod = AnakinsPod(115, "repaired", 11500)
print(new_pod.boost())

sebulbas = SebulbasPod(110, "repaired", 10000)
sebulbas.flame_jet(new_pod)
print(new_pod.condition)

# Inheritance -- both AnakinsPod and SebulbasPod both inherit from Podracer.