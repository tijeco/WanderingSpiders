import spider.spider as sp
import cricket.cricket as cr
from random import choices
import pandas as pd
import random

def prob_to_bool(prob_float):
    return (random.uniform(0,1) < prob_float )

def reproduce(daddy): # I will certainly need to retool this for multiple toxins
    #id doesn't work, only using 10000 codes isn't close to enough, need to just make it a string "index:baby_number"
    for toxin in daddy.toxins:
        ld50_bottom = 0.97 * daddy.toxins[toxin]["ld50"]
        ld50_top = 1.03 * daddy.toxins[toxin]["ld50"]
    babies = [sp.spider(1,ld50_bottom,ld50_top) , sp.spider(1,ld50_bottom,ld50_top)]
    for baby in babies:
        #something really weird is happeneing, they all land on the same baby bumber???
        if daddy.id != 0:
            # print(int(daddy.id), daddy.id,int(daddy.id) - daddy.id)
            # if round(daddy.id - int(daddy.id), 4) == 0.0001:
            daddy_index = int(daddy.id.split(":")[0])
            # print("daddy",daddy_index)
            baby_index = int(daddy.id.split(":")[1])
            # print("baby_start",baby_index)
            if baby_index == 1:
                # baby.id = round(daddy.id + (0.0001 * (1+babies.index(baby))),4)
                baby_index = 2 + babies.index(baby)
                # print("baby_one",baby_index)
            elif baby_index % 2:
                # baby.id = round(int(daddy.id) + (2 * round(daddy.id - int(daddy.id), 4) +(0.0002* (babies.index(baby)))-0.0001),4)
                baby_index = ((2 * baby_index) - 1) +  2*babies.index(baby)
            else:
                # print( "daddy",round(daddy.id - int(daddy.id),4),(0.0001* (babies.index(baby))))
                # baby.id = round(int(daddy.id) + (2 * round(daddy.id - int(daddy.id), 4) +(0.0002* (babies.index(baby)))),4)
                baby_index = (2 * baby_index) + 2*babies.index(baby)
            baby.id = str(daddy_index) + ":" + str(baby_index)
            # print("id",baby.id)
            # baby.id = daddy.id + (0.0003 * (1+babies.index(baby)))
            # baby.id = daddy.id + (0.0001 * (1+babies.index(baby)))
            #need to work out a way so that they won't overwrite themselves over time, so odd ids beget odd ids or something
    return babies


average_cricketMass = ((76.9+95.3)/2) #86.1
cricket = cr.cricket(average_cricketMass) # constant cricket size, for trial2, perhaps this varies
ld50_low = 0.01
ld50_high = 0.025 #avg =.0175
# expression_low = 0
# expression_high = 10000
spider_cluster = {"spiders": [sp.spider(1,ld50_low,ld50_high) for i in range(100)]}

# print(spider_cluster.keys())
# for t in range(2):
# t = 0
# while max([i.mass for i in spider_cluster["spiders"] ]) < 300: ## TODO: need to make sure this is a reasonable target mass
    # assimilated_mass = cricket.mass * 0.7038
def annualFeeding(spiderCluster,inCricket):
    final_spiders = {"mass":[],"spiders":[],"cricket":[]}
    for t in range(52): # consider making into annualFeeding(spider_clster,cricket) function
        current_time = "t_"+str(t)
        for spider in spiderCluster:
            # perhaps instead of updating spiders, I should be initializing new spiders each time? Seems dumb?
            feed_probability = cr.calc_toxicity(spider.toxins,inCricket.mass) # guaranteed cricket encounter every week
            if t == 0:
                # print("before:",spider.id)
                if spider.id == 0:
                    spider.id = str(list(spiderCluster).index(spider))+":1"
                    print(spider.id)

                #else:
                    #spider.id +=  0.0001
                # print("after:",spider.id)
                # print(current_time, spider.mass, feed_probability, spider.toxins) #first week values
            else:

                # print(choices([0,1],[feed_probability,(1-feed_probability)]))

                cricket_survive = choices([0,1],[feed_probability,(1-feed_probability)])[0]
                if not cricket_survive:
                    spider.update_mass(inCricket.mass) # MASS GAIN
                    #MASS also needs to be updated based on energy loss related to venom expression, or does it?? nah?

                    # spider_cluster["spiders"][spider] =
                # print(current_time, spider.mass, feed_probability, spider.toxins)
                ## TODO: This is a week by week thing, I need to incorporate daily mass loss here somehow using metabolic_rate
                daily_calorie_loss =  (0.0909 * spider.mass ) * 1.2 # 1.2 should only be included if a feeding attempt has been made
                #MASS also needs to be updated based on energy loss related to venom expression, 1.2 accomplishes that

                daily_mass_loss = daily_calorie_loss * 0.162

                # current_mass = spider.mass - daily_mass_loss*7

                spider.mass = spider.mass -  daily_mass_loss*7 #MASS LOSS/week
                for toxin in spider.toxins: # making this work for multiple toxins is for trial2 or 3
                    spider.toxins[toxin]["expression"] = spider.mass * (4/300)
                # print(current_time, spider.mass, feed_probability, spider.toxins) # weekly values
                if t == 51:
                    # print(spiderCluster["spiders"].index(spider)+0.0001)
                    # print(current_time, spider.mass, feed_probability, spider.toxins) # final week values
                    final_spiders["mass"].append(spider.mass)
                    # final_spiders["id"].append(spiderCluster["spiders"].index(spider)+0.0001)

                    final_spiders["spiders"].append(spider)
                    final_spiders["cricket"].append((cricket.mass,feed_probability))
    annual_dataframe = pd.DataFrame.from_dict(final_spiders)
    annual_dataframe["reproduce"] = annual_dataframe["mass"].rank(pct = True).apply(prob_to_bool)
    return annual_dataframe
year1 = annualFeeding(spider_cluster["spiders"],cricket)
# print(year1)
# print(year1[year1["reproduce"] == True].shape)
# print(annualFeeding(year1[year1["reproduce"] == True]["spiders"],cricket))

# current_spider = sp.spider(1,ld50_low,ld50_high)
# current_spider.id = "0:1"
#
# print(reproduce(current_spider)[0].id)
# current_list = reproduce(current_spider)
# print([s.id for s in current_list])
# while len(current_list) < 10:

# for spidey in current_list:
#     current_list += reproduce(spidey)
#     print([s.id for s in current_list])
#     if len(current_list) > 10:
#         break

        # for s in current_list:
            # print(s.id)
    # current_spider = reproduce(current_spider)

print("start HERE")
for year in range(50):
    print("year",year)
    offspring = []
    if year == 0:
        for survivor in year1[year1["reproduce"] == True]["spiders"]:
            offspring += reproduce(survivor)
        current_year = annualFeeding(offspring,cricket)

        continue
    for survivor in current_year[current_year["reproduce"] == True]["spiders"]:
        offspring += reproduce(survivor)
    current_year = annualFeeding(offspring,cricket)
    for i in current_year["spiders"]:
        print(i.id)

# NOTE: All that needs to be done now is to figure out the best way to log stuff to a csv file

# print(current_year)

    # for toxin in i.toxins:
        # print(i.toxins[toxin]["ld50"])



## TODO: need to take spiders from year1 that can reproduce, and reproduce them... perhaps with reproduce() function...

# year1["reproduce"] = year1["mass"].rank(pct = True).apply(prob_to_bool)

# print(year1["mass"].rank(pct = True).apply(prob_to_bool))
# print(year1["spiders"])

# year2 = annualFeeding(year1,cricket)
# for s in year2["spiders"]:
#     print(s.id)

# print(prob_to_bool(0.9))

# print((year1["mass"]-year1["mass"].mean())/year1["mass"].std() )
# print((year1["mass"]-year1["mass"].min())/(year1["mass"].max() - year1["mass"].min()) )
# print(year1)
# print(year1["mass"].rank(pct = True))

    # t +=1
    # if t == 52: ## TODO: potentialy will do for i in 1-52 instead of while, so that final mass at end determines fitness
        # break
# print(max([i.mass for i in spider_cluster["spiders"] ]))
# for i in spider_cluster["spiders"]:
#     print(i.mass)
