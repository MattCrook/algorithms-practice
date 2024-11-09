#--------------------------------------------------------#
# Write a function that takes in a list and shuffles it.
#--------------------------------------------------------#
import random

l = [1,2,3,4,5]

# Modifies original list in place.
def shuffle_1(list):
  random.shuffle(list)


shuffle_1(l)
print("shuffle_1: ", l)
print("--------------------------")



# Returns a new list, shuffled from original.
def shuffle_2(list):
  temp = random.sample(list, len(list))
  return temp


print("original list: ", l)
print("shuffle_2: ", shuffle_2(l))
print("--------------------------")
