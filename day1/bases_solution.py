import math
import random

bases="ACTTGCTTGAC"
l = len(bases)
s1 = random.random()*l # transform from a randome number in [0,1) to [0,len(bases)]
idx = math.floor(s1) # round down to get a random integer in [1, l-1]

print("random base ",bases[idx])