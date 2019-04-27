# simulating spiders: how long can a spider go with out eating

## first we need to set up the spider

Mass (mg)

* spiderMassMin = 222.4
* spiderMassMax = 267.4

Caloric loss per day (cal/mg)
* calPerDayMin = 0.0112
* calPerDayMax = 0.1706

## The spider's food will be a cricket

Mass (mg)

* cricketMin = 76.9
* cricketMax = 95.3
* cricketAssimilatedMin = 50.6
<!--  60.6 -->
* cricketAssimilatedMax = 70.6

Caloric content (cal/mg)
* cricketCal = 6.17

## Now we can make a spider datatype

the spider will have the three following properties

* Mass (mg)
* Cals (cal)
* Metabolism (cals/mg)/day
* Oxygen (uL O2/mg per hour)
* Loss (related to oxygen and respiration)

log uL O2/g per hour = 2.612 - 0.08 * log X

X = mass (g)


n<sub>H = hills coefficient

<img src="https://latex.codecogs.com/svg.latex?\Large&space;Y=\frac{100 }{1+10^{logDose_{50}\times n_H} }"  />





If we feed our spider a cricket, and it assimilates 60.6 mg, with 6.17 cal/mg, can have a variable that represents the total amount of calories available from this cricket.



```go
calsFromCricket :=  60.6 * 6.17
```

Let's make a spider that weighs 244.9 mg and burns 0.0909 cals/mg body weight per day, then we will add 60.6 mg to its mass

```go
oneSpider := spider.Spider{Mass: 244.9, Metabolism: 0.0909, Cals: calsFromCricket}
oneSpider.Mass += 60.6
```
How long will this spider be able to sustain itself with this food supply?

```go
fmt.Println(oneSpider.Cals / oneSpiderCalLoss)
```

About two weeks!

## how much mass does the spider lose each day?
