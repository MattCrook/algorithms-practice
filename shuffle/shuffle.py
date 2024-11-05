import random
import math

a = [1,2,3,4,5]

# modifies original list in place.
def shuffle_0(list):
  random.shuffle(list)

shuffle_0(a)
print(a)



def shuffle_2(list):
  temp = random.sample(list, len(list))
  return temp

print(shuffle_2(a))
