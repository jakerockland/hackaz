#!/usr/bin/python
# -*- coding: utf-8 -*-
import data     # Get our horrendous dictionary (called "deltas") of hashtag pairs with corresponding deltas
		# This also has the "probabilities" dictionary and a "user_percent" dictionary.
from tweets_percentage import * 
import 

class UserProcess(object):

	def __init__(self,user_tweets,username,nothing=False):
		# usersTweets is a dictionary.
		# set up empty list and dictionary for later output.
		self.to_follow=[] 
		self.related_tags={}
		
		self.calcTop(user_tweets)
		# calculate all the things, so that we can then get results when necessary.		
		#if nothing is False:
		#	self.calculate(users_tweets,username)

	def calcTop(self,user_tweets):
		all_list = calc_weights(self,user_tweets).values()
		all_list.sort(key=lambda tup: tup[1])
		return all_list[0:10]

	def calculate(self,users_tweets,username):
		# Calculates the users similarities with others
		# Is only internal, returns nothing

		# Get user's weights
		username_weights = calc_weights(users_tweets[username])
		
		# Pull out username's tweets. Del from dictionary to speed up for loop.
		username_tweets = users_tweets[username]
		del users_tweets[username]
		
		temp_list = []

		# Loop through all users and calculate "distance" with username.
		for match in users_tweets:
			match_weights=calc_weights(users_tweets[match])
			distance = weight_diff(username_weights,match_weights,match)

			# Check if match in top 10 matches; add if it is.
			if len(temp_list)>=10 and distance<temp_list[-1][1]:
				del temp_list[-1]
				temp_list.append((match,distance))
				temp_list.sort(key=lambda tup: tup[1]) # Sorts by second element.
			elif len(temp_list)<10:
				temp_list.append((match,distance))
				temp_list.sort(key=lambda tup: tup[1])
		
		# Save to_follow for later
		self.to_follow = list(zip(*temp_list)[0])

	def calc_weights(self,user_tweets):
		# Calculates weights for each node by adding user's adjusted percentage
		# to the delta-adjusted percentages of similar nodes and subtracting
		# the delta-adjusted overcounted weights
		
		# Get adjusted user percentages as a dictionary with hashtags as keys
		percentages = tweets_percentage(user_tweets)
		delta_percentages = {}
		
		# adjust all nodes based on deltas and probabilities from BigProcess.
		for node in percentages:
			delta_percent = percentages[node]
			for connected_node in percentages:
				if node < connected_node:
					delta_percent += (percentages[connected_node]-probabilities[connected_node+"|"+node])*deltas[node+"|"+connected_node] # TODO make this not loop twice as many times as necessary.
			delta_percentages[node] = delta_percent/float(user_percent[node])
		
		return delta_percentages
			

	def weight_diff(self,user_weights,match_weights,match_name):
		# Returns the "distance" between two users using their weights.
		# Also, stores a list of 5 top hashtags related to user from match
		# in self.related_tags with match_name as the key.
		
		weight_list=[]
		top_tags=[]

		for hashtag in user_weights:
			distance = ((user_weights[hashtag])**(0.5)-(match_weights[hashtag])**(0.5))^2	
			weight_list.append(distance)
			
			# Check if x in top 5 tags for this match; add if so.
			if len(top_tags)>=5 and distance<top_tags[-1][1]:
				del top_tags[-1]
				top_tags.append((hashtag,distance))
				top_tags.sort(key=lambda tup: tup[1])
			elif len(top_tags)<5:
				top_tags.append((hashtag,distance))
				top_tags.sort(key=lambda tup: tup[1])
		
		# Save to related_tags for later.
		self.related_tags[match_name] = top_tags

		return sum(weight_list)
	
	def getRelatedTags(self):
		return self.related_tags

	def getToFollow(self):
		return self.to_follow

	def graph(self):
		# Draws a fancy graph using Wolfram. This graphs is of all the hashtag 
		# clusters with better delta similarities corresponding to closer clusters
		# of hashtags. It is colored according to the user's interests, with grayed
		# out bits representing parts that the user is not involved in even indirectly.
		pass
