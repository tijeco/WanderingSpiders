
import random
import math


class spider:



    spiderMassMax  = 267.4
    spiderMassMin = 222.4
    calPerDayMin =  0.0112
    calPerDayMax = 0.1706
    cals = 0
    mass = spiderMassMin
    metabolic_rate = (calPerDayMax + calPerDayMin)/2
    oxygen = 0
    mass_loss_rate = 0

    def change_mass(self):
        self.mass = random.uniform(self.spiderMassMin,self.spiderMassMax)
    def change_metabolic_rate(self):
        self.metabolic_rate = random.uniform(self.calPerDayMin,self.calPerDayMax)

class venom_gland:
    def __init__(self, num_toxins):
        self.num_toxins = num_toxins
        self.toxins = {}
        for num in range(num_toxins):
            self.toxins["component_"+str(num)] = {"ld50":random.uniform(50,100),"expression":random.uniform(0,500)}
        print(self.toxins)



    def calc_toxicity(self):
        self.toxicity = 1
        for toxin in self.toxins:
            # use toxicity variables and expression value to calculate toxicity per component
            ld50 = self.toxins[toxin]["ld50"]
            cricketMass = ((76.9+95.3)/2)
            dose = self.toxins[toxin]["expression"] / cricketMass
            if dose == 1:
                print("ERROR!!!")
            # print(dose)
            base = math.log(dose)/math.log(ld50)




            probability_death = 1/(1 + 10**(math.log(ld50)-math.log(dose)) )

            print(toxin)
            print("LD50",ld50)
            print("dose",dose)
            print("probability_death",probability_death)
            self.toxicity = (1 - probability_death) * self.toxicity
        self.toxicity = 1 - self.toxicity
            # print((1-self.toxins[toxin]["ld50"])*self.toxicity)



a = spider()
# a.change_mass()
print("Spider mass:",a.mass)
print("Spider metabolism:", a.metabolic_rate)
b = venom_gland(100)
b.calc_toxicity()
print(b.toxicity)

# print(1.0/(1.0+ (math.log(0.009)/math.log(76.26))**-12))
