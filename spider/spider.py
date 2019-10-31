import random
import math
import numpy as np
import pandas as pd
import datetime


class spider:
    ## TODO:  determine how exp_max relates to body size
    # # TODO: also determine the effect that expression has on calories burned
    # just take scorpion concentration and multiply be some 20% factor
    spiderMassMax = 267.4
    spiderMassMin = 222.4
    calPerDayMin = 0.0112
    calPerDayMax = 0.1706
    cals = 0
    id = 0
    mass = spiderMassMin
    def __init__(self, num_toxins,ld50_min,ld50_max):
        self.num_toxins = num_toxins
        self.ld50_min = ld50_min
        self.ld50_max = ld50_max

        self.toxins = {}
        # self.toxicity = 1
        # expression and ld50 defined here as a random variable
        for num in range(num_toxins):## NOTE:  this doesn't actually update iteratively, so there needs to be an update function or something
            self.toxins["component_"+str(num)] = {"ld50": random.uniform(ld50_min, ld50_max),
                                                  "expression":  self.mass * (4/300)} # making this work for multiple toxins is for trial2
                    # NOTE: this needs to be reconsidered because it is hard to update without reshuffling, expression needs to be updated
                    # ld50 should not change once initialized
                    # perhaps expression should be constant, and is just the mass divided by the thing
                    # honestly, might be more trouble than it's worth ... but would be nice
    metabolic_rate = (calPerDayMax + calPerDayMin)/2
    oxygen = 0
    mass_loss_rate = 0

    def update_mass(self,cricketMass):
        self.mass += (60.6/86.1) * cricketMass

    def change_metabolic_rate(self):
        self.metabolic_rate = random.uniform(
            self.calPerDayMin, self.calPerDayMax)


# a = spider(1)
# print("Spider mass:", a.mass)
# print("Spider metabolism:", a.metabolic_rate)
# print("Spider venom:", a.toxicity)
# b = venom_gland(1)
# b.calc_toxicity()
# print(b.toxicity)

# def cricket_meets_spider(spider,venom_gland,cricket_mass):

# print(1.0/(1.0+ (math.log(0.009)/math.log(76.26))**-12))


# make small array with 10 or so tuples with spider and venom gland pairs
# print("\nCommence feeding\n")

# average_cricketMass = ((76.9+95.3)/2)
# spider_cluster = {"spiders": [spider(1) for i in range(3)]}
# for t in range(2):
#     current_time = "t_"+str(t)
#     for spider in spider_cluster["spiders"]:
#         print(current_time, spider.mass, calc_toxicity(spider.toxins,average_cricketMass), spider.toxins)
#         spider.update_mass(average_cricketMass)




# print(spider_cluster)
