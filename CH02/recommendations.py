from math import sqrt


# A dictionary of movie critics and their
# ratings of a small set of movies
critics = {
    'Lisa Rose' : {
        'Lady in the Water' : 2.5,
        'Snakes on a Plane' : 3.5,
        'Just My Luck' : 3.0,
        'Superman Returns' : 3.5,
        'You, Me and Dupree' : 2.5,
        'The Night Listener' : 3.0
    },
    'Gene Seymour' : {
        'Lady in the Water' : 3.0,
        'Snakes on a Plane' : 3.5,
        'Just My Luck' : 1.5,
        'Superman Returns' : 5.0,
        'The Night Listener' : 3.0,
        'You, Me and Dupree' : 3.5
    },
    'Michael Phillips' : {
        'Lady in the Water' : 2.5,
        'Snakes on a Plane' : 3.0,
        'Superman Returns' : 3.5,
        'The Night Listener' : 4.0
    },
    'Claudia Puig' : {
        'Snakes on a Plane' : 3.5,
        'Just My Luck' : 3.0,
        'The Night Listener' : 4.5,
        'Superman Returns' : 4.0,
        'You, Me and Dupree' : 2.5
    },
    'Mick LaSalle' : {
        'Lady in the Water' : 3.0,
        'Snakes on a Plane' : 4.0,
         'Just My Luck' : 2.0,
         'Superman Returns' : 3.0,
         'The Night Listener' : 3.0,
        'You, Me and Dupree' : 2.0
    },
    'Jack Matthews' : {
        'Lady in the Water' : 3.0,
        'Snakes on a Plane' : 4.0,
         'The Night Listener' : 3.0,
         'Superman Returns' : 5.0,
         'You, Me and Dupree' : 3.5
     },
    'Toby' : {
        'Snakes on a Plane' : 4.5,
        'You, Me and Dupree' : 1.0,
        'Superman Returns' : 4.0
    }
}

# Returns a distance based similarity score for person1 and person2
def sim_euclidean(prefs, p1, p2):
    # Get the list of shared items
    sim_items = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            sim_items[item] = 1

    # if they have no ratings in common, return 0
    if len(sim_items) == 0:
        return 0

    # Add up the squared of all the differences
    sum_of_squares = sum([pow(prefs[p1][item] - prefs[p2][item], 2) for item in sim_items])

    return 1 / (1 + sum_of_squares)

# Returns the Pearson Correlation Coefficient for p1 and p2
def sim_pearson(prefs, p1, p2):
    # Get the list of shared items
    sim_items = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            sim_items[item] = 1

    # Find the number of elements
    n = len(sim_items)

    # if they have no ratings in common, return 0
    if n == 0:
        return 0

    # Add up all the preferences
    sum1 = sum([prefs[p1][it] for it in sim_items])
    sum2 = sum([prefs[p2][it] for it in sim_items])

    # Sum up all the squares
    sum1Sq = sum([pow(prefs[p1][it], 2) for it in sim_items])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in sim_items])

    # Sum up all the products
    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in sim_items])

    # Calculate Pearson score
    num = pSum - ((sum1 * sum2) / n)
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0:
        return 0

    r = num / den

    return r

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity fuction are optional params.
def topMatches(prefs, person, n=5, similarity=sim_pearson):
	scores = [(similarity(prefs, person, other), other) for other in prefs if other != person]
	# Sort the list so the highest scores appear at the top
	scores.sort()
	scores.reverse()
	return scores[0:n]

# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs, person, similarity=sim_pearson):
	totals = {}
	simSums = {}
	for other in prefs:
		# Don't compare me to myself
		if other == person:
			continue
		sim = similarity(prefs, person, other)

		# ignore scores of zero or lower
		if sim <= 0:
			continue

		for item in prefs[other]:
			# only score movies I haven't seen yet
			if item not in prefs[person] or prefs[person][item] == 0:
				# Similarity * Score
				totals.setdefault(item, 0)
				totals[item] += prefs[other][item] * sim
				
				# Sum of similarities
				simSums.setdefault(item, 0)
				simSums[item] += sim
		
		# Create the normalized list
		rankings = [(total/simSums[item]. item) for item, total in totals.items()]

		# Return the sorted list
		rankings.sort()
		rankings.reverse()
		return rankings

print(sim_euclidean(critics, 'Lisa Rose', 'Gene Seymour'))
# print(sim_pearson(critics, 'Lisa Rose', 'Gene Seymour'))
# print(topMatches(critics, 'Toby', n=3, similarity=sim_euclidean))
# print(topMatches(critics, 'Toby', n=3))



KWaG+iLVCA1wV2/EM1k+Wqltd0FNg/aRtPS55fvg