#!/usr/bin/python
# -*- coding: utf-8 -*-
from tweets_percentage import *
import networkx as nx
import matplotlib.pyplot as plt

class BigProcess(object):
	
	def __init__(self, tweets_info):
		# Initializes the process. Searches through a bunch of tweets and builds
		# a model, consisting of "probabilities", "deltas", and "user_percent"
		tweets = self.strip_basic_tweets(tweets_info)
		self.percentages = tweets_percentage(tweets)
		self.probabilities = self.calc_probabilities(tweets)
		self.deltas = self.calc_deltas()
		self.user_percent = self.percentages
		self.write_file()

	def strip_basic_tweets(self,tweets_info):
		return tweets_info # TODO make this take in twitter status objects and spit out just the text of the tweets.

	def graph(self):
		G = nx.Graph()
		for delta in self.deltas:
			split_lines = delta.split("|")
			first = split_lines[0]
			second = split_lines[1]
			G.add_edge(first,second,weight=self.deltas[delta])
		
		elarge=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] >0.5]
		esmall=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.5]
		enone=[(u,v) for (u,v,d) in G.edges(data=True) if d['weight'] <=0.1]

		pos=nx.spring_layout(G)
		nx.draw_networkx_nodes(G,pos,node_size=100)
		nx.draw_networkx_edges(G,pos,edgelist=elarge,width=3)
		nx.draw_networkx_edges(G,pos,edgelist=esmall,width=2,alpha=0.5,edge_color='b')
		nx.draw_networkx_edges(G,pos,edgelist=enone,width=1,alpha=.9)
		nx.draw_networkx_labels(G,pos,font_size=10,font_family='open sans')
		
		plt.axis('off')
		plt.savefig("weighted_graph.png")
		plt.show()

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
