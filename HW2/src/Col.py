from abc import ABCMeta, abstractmethod, abstractproperty

class Col:
	__metaclass__ = ABCMeta
	txt = ""
	n = 0
	weight = 0
	pos = 0

	def __init__(self):
		pass

	@abstractmethod
	def update(self, x):
		pass

	@abstractmethod
	def updates(self, xs):
		pass

	@abstractmethod
	def norm(self, x):
		pass

	@abstractmethod
	def distance(self, x, y):
		pass

	@abstractmethod
	def __str__(self):
		pass