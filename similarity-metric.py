
def cosineSimilarity(string1, string2, idfsDictionary):
 	""" Compute cosine similarity between two strings 
	Args: 
 		string1 (str): first string 
 		string2 (str): second string 
 		idfsDictionary (dictionary): a dictionary of IDF values 
	Returns:
  		cossim: cosine similarity value 
  	""" 
  	w1 = tfidf()
  	w2 = tfidf() 
  	return cossim(w1, w2)


def computeSimilarity(record):
	""" Compute similarity on a combination record 
	Args: 
		record: a pair, (google record, amazon record) 
	Returns: 
		pair: a pair, (google URL, amazon ID, cosine similarity value) 
	""" 
	googleRec = record[0]
	amazonRec = record[1] 

	cs = cosineSimilarity(googleValue, amazonValue, idfsSmallWeights) 
	return (googleURL, amazonID, cs)




def similar(amazonID, googleURL): 
	""" Return similarity value 
	Args: 
		amazonID: amazon ID 
		googleURL: google URL 
	Returns: 
		similar: cosine similarity value 
	""" 
	return (similaritiesRDD .filter(lambda record: (record[0] == googleURL and record[1] == amazonID)) .collect()[0][2])
