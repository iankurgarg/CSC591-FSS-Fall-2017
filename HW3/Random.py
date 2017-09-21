# No class made because there is no this.x kind of reference
import math

#class Random:

seed0 = 10013
seed = seed0
multipler = 16807.0
modulus = 2147483647.0
randomtable = None

def park_miller_randomizer():
	global seed
	seed = (multipler * seed) % modulus
	return seed / modulus

def rseed(n):
	if n:
		seed=n
	else:
		seed=seed0
	randomtable = None

def system():
  return rseed(math.random()*modulus)

def random(x=None,i=None):
	global randomtable
	if randomtable == None:
		randomtable = []
		for i in range(1, 97):
			randomtable[i] = park_miller_randomizer()
	x = park_miller_randomizer()
	i = 1 + math.floor(97*x)
	x, randomtable[i] = randomtable[i], x
	return x
