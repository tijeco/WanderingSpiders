# WanderingSpiders
A suite of tools for ruining simulations to explore how venom toxicity evolves

## first we need to set up the spider

Mass (mg)

* spiderMassMin = 222.4
* spiderMassMax = 267.4
  * average_spiderMass = 244.9

Caloric loss per day (cal/mg spider body weight)
* calPerDayMin = 0.0112
* calPerDayMax = 0.1706
  * average_calorieLoss = 0.0909





## now we can set up the cricket



Mass (mg)

* cricketMin = 76.9
* cricketMax = 95.3
  * average_cricketMass = 86.1
* cricketAssimilatedMin = 50.6
* cricketAssimilatedMax = 70.6
  * average_AssimilatedMass = 60.6

* mass_to_assimilation ratio = 60.6/86.1 = 0.7038

Caloric content (cal/mg)
* cricketCal = 6.17

Thus, for every calorie burned, 1/6.17 (0.162) mg of body weight are lost


# venom
ld50 (ug/mg body weight)
expression (ug)

expression has a hard max, there can only be so much protein in the gland
the gland can also only be so big, but supposedly gets bigger proportionately with the body

hibernalis is ~300 mg, with venom of 4000 ug/mL or 4 ug/mL
spider has ~ 4ug venom per 300 mg body (4/300) =

# fitness
should fitness be whoever reaches maturity first, or just whoever weighs the most at the end of the year?
I think it's cleaner to have one birth event per year

# setup for trial 1

Cricket size is constant, and spider's are guaranteed a cricket encounter each week.
The spider only has one toxin. Its expression is directly proportionate to its mass and increases as it gets larger
Expression is maxed out
Crickets do not evolve.
Simulate 1000 spiders for 52 weeks, let the probability of reproduction = their mass ranking.
Larger spiders are more likely to reproduce.
Asexual reproduction for ~half the population.
Generates two offspring, only thing allowed to vary is ld50, which only changes by a certain amount.
Continue for 1000 generations/years.

## prediction

ld50 will bottom out, it is unrestrained, so it will continue to get lower and lower after rounds of selection
Although, perhaps over time because they are given a finite amount of crickets of a finite mass, the finalized mass will level off over time, so that there is less pressure for ld50 to get lower and lower

Something worth noting is that ld50 is evolving via brownian motion, meaning it should meander randomly and asymptotically to zero. There is, however, a limit to how low ld50 can be. The minimum dosage is one single toxin protein. Then the ld50 would be something like the mass of the protein (ug) divided by the mass of the cricket (mg). This will almost certainly be an extremely small number. One 10 kDa toxin weighs 1.6605402e-14 ug.

Question?: Under this scenario, over a certain amount of time, will ld50 reach that threshold? If not, why" If so, how long would it take?

# setup for trial 2

Cricket size is random, and spider's are guaranteed a cricket encounter each week.
The spider only has one toxin. Its expression is directly proportionate to its mass and increases as it gets larger
Crickets do not evolve.
Simulate 1000 spiders for 52 weeks, let the probability of reproduction = their mass ranking.
Larger spiders are more likely to reproduce.
Asexual reproduction for half the population.
Generates two offspring, only thing allowed to vary is ld50, which only changes by a certain amount.
Continue for 1000 generations/years.

## prediction

ld50 will still bottom out, but perhaps more stochastically than trial1
perhaps it is necessary to have average cricket mass grow over time too, though maybe just fine to expand cricket max to be 400 mg or something like that, that way they have access to large crickets at all time, but can only subdue them if they are large/ have potent enough venom.



#setup for trial3

Cricket size is random, and spider's are guaranteed a cricket encounter each week.
Initial number of toxins are generated randomly. The sum expression is directly proportionate to its mass and increases as it gets larger
Crickets do not evolve.
Simulate 1000 spiders for 52 weeks, let the probability of reproduction = their mass ranking.
Larger spiders are more likely to reproduce.
Asexual reproduction for half the population.
Generates two offspring, only thing allowed to vary is ld50, which only changes by a certain amount.
Continue for 1000 generations/years.

## prediction

having more things creates redundancy, so that it's fitness isn't as affected by one toxin being weak
This will create a buffer so that increased toxin number will likely  be prefered
An expected caveat is that spiders with only one toxin that is very potent will still have high fitness


# heritability

in human twin study (Silventoinen, K., Kaprio, J. & Lahelma, E. Behav Genet (2000) 30: 477. https://doi.org/10.1023/A:1010202902159) height was avg 163.4 std 5.28 rsd 0.0323, so we can try letting offspring vary by 3% of their parents values
