import math
import random


"""
Class to generate Random numbers
"""
class Random:
	seed0 = 10013
	seed = seed0
	multipler = 16807.0
	modulus = 2147483647.0
	randomtable = None

	@staticmethod
	def park_miller_randomizer():
		Random.seed = (Random.multipler * Random.seed) % Random.modulus
		return Random.seed / Random.modulus

	# updates the seed
	@staticmethod
	def rseed(n):
		if n:
			Random.seed = n
		else:
			Random.seed = Random.seed0
		Random.randomtable = None

	# initializes a new randomly selected seed
	@staticmethod
	def system():
		Random.rseed(random.uniform(0,1)*Random.modulus)

	# This function generates next random number in the sequence
	@staticmethod
	def another():
		if Random.randomtable is None:
			Random.randomtable = [None]*97
			for i in range(0, 97):
				Random.randomtable[i] = Random.park_miller_randomizer()
		x = Random.park_miller_randomizer()
		i = int(math.floor(97*x))
		temp = x
		x = Random.randomtable[i]
		Random.randomtable[i] = temp
		return x


if __name__=="__main__":
	print Random.system()
	for i in range(10):
		print Random.another()