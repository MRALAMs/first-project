#!/usr/bin/python3

class player:
	def __init__(self): 
		self.level=1
		self.HP=100
	def levelup(self):
		self.level+=1
		self.HP+=10

