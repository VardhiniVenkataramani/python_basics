import random
health=50
difficulty= 1
portion_health= int(random.randint(25,50)/ difficulty)
health= portion_health+ health
print(health)
