import spider.spider as sp
import cricket.cricket as cr
from random import choices
import pandas as pd
import random

def prob_to_bool(prob_float):
    return (random.uniform(0,1) < prob_float )

def reproduce(daddy): # I will certainly need to retool this for multiple toxins
    for toxin in daddy.toxins:
        ld50_bottom = 0.97 * daddy.toxins[toxin]["ld50"]
        ld50_top = 1.03 * daddy.toxins[toxin]["ld50"]
    babies = [sp.spider(1,ld50_bottom,ld50_top) , sp.spider(1,ld50_bottom,ld50_top)]
    for baby in babies:
        #something really weird is happeneing, they all land on the same baby bumber???
        if daddy.id != 0:
            daddy_index = int(daddy.id.split(":")[0])
            baby_index = int(daddy.id.split(":")[1])
            if baby_index == 1:
                baby_index = 2 + babies.index(baby)
            elif baby_index % 2:
                baby_index = ((2 * baby_index) - 1) +  2*babies.index(baby)
            else:
                baby_index = (2 * baby_index) + 2*babies.index(baby)
            baby.id = str(daddy_index) + ":" + str(baby_index)
    return babies


average_cricketMass = ((76.9+95.3)/2) #86.1
cricket = cr.cricket(average_cricketMass) # constant cricket size, for trial2, perhaps this varies
ld50_low = 0.01
ld50_high = 0.025 #avg =.0175

spider_cluster = {"spiders": [sp.spider(1,ld50_low,ld50_high) for i in range(100)]}
# print_year1 = True
def annualFeeding(spiderCluster,inCricket,year):
    final_spiders = {"year":[],"mass":[],"id":[],"ld50":[],"spiders":[],"cricket":[]}
    for t in range(52): # consider making into annualFeeding(spider_clster,cricket) function
        current_time = "t_"+str(t)
        for spider in spiderCluster: # NOTE: this should be able to be paralelized somehow
            feed_probability = cr.calc_toxicity(spider.toxins,inCricket.mass) # guaranteed cricket encounter every week
            if t == 0:
                if spider.id == 0:
                    spider.id = str(list(spiderCluster).index(spider))+":1"
                    # print(spider.id)

            else:

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

                spider.mass = spider.mass -  daily_mass_loss*7 #MASS LOSS/week
                for toxin in spider.toxins: # making this work for multiple toxins is for trial2 or 3
                    spider.toxins[toxin]["expression"] = spider.mass * (4/300)
                if t == 51:
                    final_spiders["year"].append(year)
                    final_spiders["mass"].append(spider.mass)

                    final_spiders["spiders"].append(spider)
                    final_spiders["id"].append(spider.id)
                    final_spiders["ld50"].append(spider.toxins["component_0"]["ld50"])
                    final_spiders["cricket"].append((cricket.mass,feed_probability))
            # if print_year1:
                # print(t,spider.id,spider.mass,spider.toxins["component_0"]["ld50"],feed_probability)
    annual_dataframe = pd.DataFrame.from_dict(final_spiders)
    annual_dataframe["reproduce"] = annual_dataframe["mass"].rank(pct = True).apply(prob_to_bool)
    return annual_dataframe
year1 = annualFeeding(spider_cluster["spiders"],cricket,0)
# print_year1 = False
# print("start HERE")
df_list = [year1]
for year in range(1000):

    # print("year",year)
    offspring = []
    if year == 0:
        for survivor in year1[year1["reproduce"] == True]["spiders"]:
            offspring += reproduce(survivor)
        current_year = annualFeeding(offspring,cricket,year)
        continue

    for survivor in current_year[current_year["reproduce"] == True]["spiders"]:
        offspring += reproduce(survivor)
    current_year = annualFeeding(offspring,cricket,year)

    df_list.append(current_year)
out_df = pd.concat(df_list).drop(["spiders", "cricket"], axis=1)
out_df.to_csv("trial1.csv")
