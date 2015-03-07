import data.py # Get our horrendous dictionary of hashtag pairs with corresponding deltas

class UserProcess:

	def __init__(users_tweets,username):
		# usersTweets is a dictionary.
		# set up empty list and dictionary for later output.
		self.to_follow=[] 
		self.related_tags={}

		# calculate all the things, so that we can then get results when necessary.		
		self.calculate(users_tweets,username)
		
	def calculate(users_tweets,username):
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
			distance = weight_diff(username_weights,match_weights)

			# Check if match in top 10 matches; add if it is.
			if len(temp_list)>=10 and distance<temp_list[-1][1]:
				del temp_list[-1]
				temp_list.append((match,distance))
				temp_list.sort(key=lambda tup: tup[1]) # Sorts by second element.
			elif len(temp_list)<10:
				self.to_follow.append((match,distance))
				temp_list.sort(key=lambda tup: tup[1])
		
		# Save to_follow for later
		self.to_follow = list(zip(*temp_list)[0])

	def calc_weights(user_tweets):
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
