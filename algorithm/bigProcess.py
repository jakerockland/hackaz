#!/usr/bin/python
# -*- coding: utf-8 -*-
from tweets_percentage import *

class BigProcess(object):
	
	def __init__(self, tweets):
		# Initializes the process. Searches through a bunch of tweets and builds
		# a model, consisting of "probabilities", "deltas", and "user_percent"
		self.percentages = tweets_percentage(tweets)
		self.probabilities = self.calc_probabilities(tweets)
		self.deltas = self.calc_deltas()
		self.user_percent = self.percentages
		self.write_file()


	def calc_deltas(self):
		# Takes probabilities, and does a sum across all neighbors of each 
		# node and spits out a "distance" between two nodes.
		# These are symmetric, so we only need to do half.
		deltas = {}
		
		hashtag_size=float(len(self.percentages))
		for tag1 in self.percentages:
			for tag2 in self.percentages:
				if tag1 < tag2:
					terms = []
					denom = []
					for y in self.percentages:
						terms.append(abs(self.probabilities[y+"|"+tag1]-self.probabilities[y+"|"+tag2]))
						denom.append(self.probabilities[y+"|"+tag1]+self.probabilities[y+"|"+tag2])
					deltas[tag1+"|"+tag2]=1-(sum(terms)/sum(denom))**2
					print tag1+"|"+tag2+": "+str(1-(sum(terms)/sum(denom))**2)
		return deltas

	def calc_probabilities(self,tweets):
		# Calculates P(tag1|tag2)'s for all pairs of hashtags tag1,tag2
		probabilities = {}
		for tag2 in self.percentages:
			conditional_percents=tweets_percentage(tweets,tag2)
			for tag1 in self.percentages:
				if tag1 in conditional_percents:
					probabilities[tag1+"|"+tag2]=conditional_percents[tag1]
				else:
					probabilities[tag1+"|"+tag2]=0

		return probabilities

	def write_file(self):
		# Write a giant, sketchy dictionary.
		with open('data.py', 'w') as the_file:
			the_file.write('deltas = ')
			the_file.write(str(self.deltas))
			the_file.write('\n')
			the_file.write('probabilities = ')
			the_file.write(str(self.probabilities))
			the_file.write('\n')
			the_file.write('user_percent = ')
			the_file.write(str(self.user_percent))
			the_file.write('\n')
