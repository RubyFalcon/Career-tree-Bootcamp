import random
# we have standard libraries
# for i in range(3):
    # print(random.random())
    # print(random.randint(10,20))
# Generating random values

members = ['John',"Mary",'Bob','Mosh']
leader = random.choice(members)
print(leader)

# 01: Roll a dice 
class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second
        # we want to return a tuple of rolling two dice


dice1 = Dice()
print(dice1.roll())