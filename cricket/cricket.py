import random
import math
import numpy as np
import pandas as pd
import datetime

class cricket:
    def __init__(self,mass):
        self.mass = mass


def calc_toxicity(toxins,cricketMass):
    toxicity = 1
    if True:

        for toxin in toxins:
            # use toxicity variables and expression value to calculate toxicity per component
            ld50 = toxins[toxin]["ld50"]
            # for trial one, this is an average value and remains constant, but will eventually be variable

            dose = toxins[toxin]["expression"] / cricketMass
            if dose == 1:
                print("ERROR!!!")
            # print(dose)
            # I believe the base value below would determine the shape of the LD50 curve
            base = math.log(dose)/math.log(ld50)

            probability_death = 1/(1 + 10**(math.log(ld50)-math.log(dose)))

            # print(toxin)
            # print("LD50",ld50)
            # print("dose",dose)
            # print("probability_death",probability_death)
            toxicity = (1 - probability_death) * toxicity
        toxicity = 1 - toxicity # is the cumalative probability_death
    return toxicity
