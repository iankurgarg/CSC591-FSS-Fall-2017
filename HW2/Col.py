from abc import ABCMeta, abstractmethod

class Col:
	__metaclass__ = ABCMeta

	def __init__(self):
		self.n = 0

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