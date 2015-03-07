#!/usr/bin/python
# -*- coding: utf-8 -*-
import data     # Get our horrendous dictionary (called "deltas") of hashtag pairs with corresponding deltas
		# This also has the "probabilities" dictionary and a "user_percent" dictionary.
import re       # regular expressions package

class UserProcess(object):

	def __init__(self,users_tweets,username,nothing=False):
		# usersTweets is a dictionary.
		# set up empty list and dictionary for later output.
		self.to_follow=[] 
		self.related_tags={}

		# calculate all the things, so that we can then get results when necessary.		
		if nothing is False:
			self.calculate(users_tweets,username)
		
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
		percentages = self.tweets_percentage(user_tweets)
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
	
	def tweets_percentage(self,tweets):
		# Takes in a list of tweets (each tweet is a separate string).
		# Outputs a dictionary with keys of hashtags and values of percentages.
		# For hashtag A, A:(number of A)/len(tweets)

		percentages={}

		# Go through all tweets, get all percents and add to the dictionary.
		for tweet in tweets:
			print tweet
			# Is it a hashtag?
			tags = set(re.findall(r'([#＃][a-zA-Z0-9_\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u024f\u0253-\u0254\u0256-\u0257\u0300-\u036f\u1e00-\u1eff\u0400-\u04ff\u0500-\u0527\u2de0-\u2dff\ua640-\ua69f\u0591-\u05bf\u05c1-\u05c2\u05c4-\u05c5\u05d0-\u05ea\u05f0-\u05f4\ufb12-\ufb28\ufb2a-\ufb36\ufb38-\ufb3c\ufb40-\ufb41\ufb43-\ufb44\ufb46-\ufb4f\u0610-\u061a\u0620-\u065f\u066e-\u06d3\u06d5-\u06dc\u06de-\u06e8\u06ea-\u06ef\u06fa-\u06fc\u0750-\u077f\u08a2-\u08ac\u08e4-\u08fe\ufb50-\ufbb1\ufbd3-\ufd3d\ufd50-\ufd8f\ufd92-\ufdc7\ufdf0-\ufdfb\ufe70-\ufe74\ufe76-\ufefc\u200c-\u200c\u0e01-\u0e3a\u0e40-\u0e4e\u1100-\u11ff\u3130-\u3185\ua960-\ua97f\uac00-\ud7af\ud7b0-\ud7ff\uffa1-\uffdc\u30a1-\u30fa\u30fc-\u30fe\uff66-\uff9f\uff10-\uff19\uff21-\uff3a\uff41-\uff5a\u3041-\u3096\u3099-\u309e\u3400-\u4dbf\u4e00-\u9fff\u20000-\u2a6df\u2a700-\u2b73f\u2b740-\u2b81f\u2f800-\u2fa1f]*[a-z_\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u024f\u0253-\u0254\u0256-\u0257\u0300-\u036f\u1e00-\u1eff\u0400-\u04ff\u0500-\u0527\u2de0-\u2dff\ua640-\ua69f\u0591-\u05bf\u05c1-\u05c2\u05c4-\u05c5\u05d0-\u05ea\u05f0-\u05f4\ufb12-\ufb28\ufb2a-\ufb36\ufb38-\ufb3c\ufb40-\ufb41\ufb43-\ufb44\ufb46-\ufb4f\u0610-\u061a\u0620-\u065f\u066e-\u06d3\u06d5-\u06dc\u06de-\u06e8\u06ea-\u06ef\u06fa-\u06fc\u0750-\u077f\u08a2-\u08ac\u08e4-\u08fe\ufb50-\ufbb1\ufbd3-\ufd3d\ufd50-\ufd8f\ufd92-\ufdc7\ufdf0-\ufdfb\ufe70-\ufe74\ufe76-\ufefc\u200c-\u200c\u0e01-\u0e3a\u0e40-\u0e4e\u1100-\u11ff\u3130-\u3185\ua960-\ua97f\uac00-\ud7af\ud7b0-\ud7ff\uffa1-\uffdc\u30a1-\u30fa\u30fc-\u30fe\uff66-\uff9f\uff10-\uff19\uff21-\uff3a\uff41-\uff5a\u3041-\u3096\u3099-\u309e\u3400-\u4dbf\u4e00-\u9fff\u20000-\u2a6df\u2a700-\u2b73f\u2b740-\u2b81f\u2f800-\u2fa1f][a-z0-9_\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff\u0100-\u024f\u0253-\u0254\u0256-\u0257\u0300-\u036f\u1e00-\u1eff\u0400-\u04ff\u0500-\u0527\u2de0-\u2dff\ua640-\ua69f\u0591-\u05bf\u05c1-\u05c2\u05c4-\u05c5\u05d0-\u05ea\u05f0-\u05f4\ufb12-\ufb28\ufb2a-\ufb36\ufb38-\ufb3c\ufb40-\ufb41\ufb43-\ufb44\ufb46-\ufb4f\u0610-\u061a\u0620-\u065f\u066e-\u06d3\u06d5-\u06dc\u06de-\u06e8\u06ea-\u06ef\u06fa-\u06fc\u0750-\u077f\u08a2-\u08ac\u08e4-\u08fe\ufb50-\ufbb1\ufbd3-\ufd3d\ufd50-\ufd8f\ufd92-\ufdc7\ufdf0-\ufdfb\ufe70-\ufe74\ufe76-\ufefc\u200c-\u200c\u0e01-\u0e3a\u0e40-\u0e4e\u1100-\u11ff\u3130-\u3185\ua960-\ua97f\uac00-\ud7af\ud7b0-\ud7ff\uffa1-\uffdc\u30a1-\u30fa\u30fc-\u30fe\uff66-\uff9f\uff10-\uff19\uff21-\uff3a\uff41-\uff5a\u3041-\u3096\u3099-\u309e\u3400-\u4dbf\u4e00-\u9fff\u20000-\u2a6df\u2a700-\u2b73f\u2b740-\u2b81f\u2f800-\u2fa1f]*)',tweet))	

			print tags
			# Is it a mention?
			tags | set(re.findall(r'@[a-zA-Z\_]*',tweet))
			
			for tag in tags:
				# Account for each tag showing up.
				if tag not in percentages:
					percentages[tag]=0
					print tag
				percentages[tag] += 1
				print percentages[tag]

		# Divide by total tweets to get actual percentages.
		tweets_size = len(tweets)
		for tag in percentages:
			percentages[tag] = percentages[tag]/float(len(tweets))
		
		return percentages

	def graph(self):
		# Draws a fancy graph using Wolfram. This graphs is of all the hashtag 
		# clusters with better delta similarities corresponding to closer clusters
		# of hashtags. It is colored according to the user's interests, with grayed
		# out bits representing parts that the user is not involved in even indirectly.
		pass
