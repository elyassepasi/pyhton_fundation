import random
def randInt(min= 0  , max= 100  ):
    num = random.random()*100
    num=int(num)
    return num
print(randInt()) 		    # should print a random integer between 0 to 100

import random
def randInt(min= 0  , max= 50  ):
    num = random.random()*50
    num =int(num)
    return num
print(randInt(max=50)) 	    # should print a random integer between 0 to 50

import random
def randInt(min= 50  , max=  100 ):
    num = random.random()*50+50
    num=int(num)
    return num
print(randInt(min=50)) 	    # should print a random integer between 50 to 100

import random
def randInt(min= 50  , max=500   ):
    num = random.random()*450+50
    num=int(num)
    return num
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500
