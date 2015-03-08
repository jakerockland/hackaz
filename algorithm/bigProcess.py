#!/usr/bin/python
# -*- coding: utf-8 -*-
from tweets_percentage import *
import networkx as nx
import matplotlib.pyplot as plt

class BigProcess(object):
	
	def __init__(self, tweets_info):
		# Initializes the process. Searches through a bunch of tweets and builds
		# a model, consisting of "probabilities", "deltas", and "user_percent"
		
		print "Initializing BigProcess"
		print "Stripping tweets and getting rid of uppercase and underscores."
		tweets = self.strip_basic_tweets(tweets_info)
		print "Getting tweet percentages."
		self.percentages = tweets_percentage(tweets)
		print "Getting two-way tweet probabilities."
		self.probabilities = self.calc_probabilities(tweets)
		print "Getting deltas."
		self.deltas = self.calc_deltas()
		print "Getting per user percent adjustments."
		self.user_percent = self.percentages
		print "Writing file."
		self.write_file()
		print "BigProcess Initialized."

	def strip_basic_tweets(self,tweets_info):
		tweets = []
		for t in tweets_info:
			new = t.replace("_","")
			tweets.append(new.lower())
		return tweets # TODO make this take in twitter status objects and spit out just the text of the tweets.

	def graph(self):
		print "Graphing..."
		G = nx.Graph()
		nx.draw(G,with_labels=False)
		for delta in self.deltas:
			#print "Graphing "+str(delta)+"."
			split_lines = delta.split("|")
			first = split_lines[0]
			second = split_lines[1]
			G.add_edge(first,second,weight=self.deltas[delta])
		print "Arranging graph"
		pos=nx.spring_layout(G)
		
		print "Coloring and prettifying graph."
		for delta in self.deltas:
			split_lines = delta.split("|")
			first = split_lines[0]
			second = split_lines[1]
			w = 5*self.deltas[delta]**(1)
			a = self.deltas[delta]
			nx.draw_networkx_edges(G,pos,edgelist=[(first,second)],width=w,alpha=a,edge_color='#8ccfff')
		
		percents_to_rank = self.percentages.values()
		max_percent=max(percents_to_rank)
		
		print "Drawing graph labels."
		for node in self.percentages:
			f = self.percentages[node]**(0.5)*16/max_percent
			print node, f
			# nx.draw_networkx_nodes(G,pos,nodelist=[node],node_size=n, node_color='#55acee')
			nx.draw_networkx_labels(G,pos,{node:node},font_size=f,font_family='Source Sans Pro',font_color='#333333')

		plt.axis('off')
		plt.savefig("weighted_graph.png")
		# plt.show()

	def calc_deltas(self):
		# Takes probabilities, and does a sum across all neighbors of each 
		# node and spits out a "distance" between two nodes.
		# These are symmetric, so we only need to do half.
		deltas = {}
		
		hashtag_size=float(len(self.percentages))
		for tag1 in self.percentages:
			#print "Calculating deltas across "+str(tag1)+"."
			for tag2 in self.percentages:
				if tag1 < tag2:
					terms = []
					denom = []
					for y in self.percentages:
						terms.append(abs(self.probabilities[y+"|"+tag1]-self.probabilities[y+"|"+tag2]))
						denom.append(self.probabilities[y+"|"+tag1]+self.probabilities[y+"|"+tag2])
					if sum(denom)!=0:
						deltas[tag1+"|"+tag2]=1-(sum(terms)/float(sum(denom)))**2
					else: 
						print tag1+"|"+tag2+"+"+str(sum(terms))+"+"+str(sum(denom))
						deltas[tag1+"|"+tag2]=0
					#print tag1+"|"+tag2+": "+str(1-(sum(terms)/sum(denom))**2)+"+"+str(sum(terms))+"+"+str(sum(denom))
		return deltas

	def calc_probabilities(self,tweets):
		# Calculates P(tag1|tag2)'s for all pairs of hashtags tag1,tag2
		probabilities = {}
		for tag2 in self.percentages:
			#print "Calculating probabilities across "+str(tag2)+"."
			conditional_percents=tweets_percentage(tweets,tag2)
			print conditional_percents
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
