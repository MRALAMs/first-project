#!/usr/bin/python3
from pro60 import player
class Elf(player):
	def levelup(self):
		self.level+=1
		self.HP+=15

