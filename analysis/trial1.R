library(tidyverse)

trial1 <- read.table("year1_ld50_0.01-0.03.txt", header = T)
trial1
aspect_ratio <- 2.5
p <- ggplot(trial1,aes(x=week, y=mass, group=id)) #+ coord_fixed(ratio = 0.01)

# jpeg("trial1.jpg")
p <- p + geom_line(aes(color=id)) + geom_point(size=3,aes(color=id))

print(p)
ggsave("plt.png", width = 16, height = 9, dpi = 120)
# dev.off()
# p + coord_fixed(ratio = 0.2)



trial1_50years <- read.csv("trial1.csv")
head(trial1_50years)

parent_change <- trial1_50years %>% separate(id, c("parent","offspring"), remove = F) %>% group_by(year,parent)  %>% summarise(count_id = n_distinct(id))

p1 <- ggplot(parent_change, aes(x = year, y = count_id, fill = parent))  + geom_area()

print(p1)
ggsave("parent.png", width = 16, height = 9, dpi = 120)
# this plot would look way better with just 10 or so parents

trial1_ld50 <- trial1_50years %>% group_by(year) %>% summarise(sd = sd(ld50),ld50 = mean(ld50))
head(trial1_ld50)

p2 <- ggplot(trial1_ld50, aes(x = year, y = ld50)) + geom_line() + geom_point()
p2 <- p2 + geom_errorbar(aes(ymin=ld50-sd, ymax=ld50+sd), width=.2, position=position_dodge(0.05))

print(p2)
ggsave("ld50.png", width = 16, height = 9, dpi = 120)

#100 spiders, 1000 years

trial1_1000years <- read.csv("trial1.100sp_1000y.csv")

head(trial1_1000years)

# parent_change <- trial1_1000years %>% separate(id, c("parent","offspring"), remove = F) %>% group_by(year,parent)  %>% summarise(count_id = n_distinct(id))

# p1 <- ggplot(parent_change, aes(x = year, y = count_id, fill = parent))  + geom_area()

# print(p1)
# ggsave("parent.1000y.png", width = 16, height = 9, dpi = 120)
# this plot would look way better with just 10 or so parents

trial1_ld50_1000y <- trial1_1000years %>% group_by(year) %>% summarise(sd = sd(ld50),ld50 = mean(ld50))

head(trial1_ld50)

p2 <- ggplot(trial1_ld50_1000y, aes(x = year, y = ld50)) + geom_line() #+ geom_point()

# p2 <- p2 + geom_errorbar(aes(ymin=ld50-sd, ymax=ld50+sd), width=.2, position=position_dodge(0.05))

print(p2)
ggsave("ld50.1000y.png", width = 16, height = 9, dpi = 120)
