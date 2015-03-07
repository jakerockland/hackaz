import data.py # Get our horrendous dictionary of hashtag pairs with corresponding deltas

class UserProcess:

	def __init__(usersTweets,username):
		# set up empty list and dictionary for later output.
		self.to_follow=[] 
		related_tags={}
	 	
		# calculate all the things, so that we can then get results when necessary.		
		self.calculate(usersTweets,username)
		
	def calculate(usersTweets,username):
		# Calculates the users similarities with others
		# Is only internal, returns nothing
		pass 

	def calc_weights(userTweets):
		# Calculates weights for each node by adding users adjusted percentage
		# to the delta-adjusted percentages of similar nodes and subtracting
		# the delta-adjusted overcounted weights
		pass

	def weight_diff(user_weights,match_weights,match_name):
		# Returns the "distance" between two users using their weights.
		# Also, stores a list of 5 top hashtags related to user from match
		# in self.related_tags with match_name as the key.
		pass

	def graph():
		# Draws a fancy graph using Wolfram. This graphs is of all the hashtag 
		# clusters with better delta similarities corresponding to closer clusters
		# of hashtags. It is colored according to the user's interests, with grayed
		# out bits representing parts that the user is not involved in even indirectly.
		pass
