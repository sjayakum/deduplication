
def tf(tokens): 
	""" Compute TF 
	Args: 
		tokens (list of str): input list of tokens from tokenize 
	Returns: 
		dictionary: a dictionary of tokens to its TF values 
	""" 
	tokenCounts = {} for t in tokens: tokenCounts[t] = tokenCounts.get(t, 0) + (1.0/len(tokens))
	return tokenCounts


def idfs(corpus): 
	""" Compute IDF 
	Args: 
		corpus (RDD): input corpus 
	Returns: 
		RDD: a RDD of (token, IDF value) 
	""" 
	N = corpus.count() uniqueTokens = corpus.flatMap(lambda x: list(set(x[1])))
	tokenCountPairTuple = uniqueTokens.map(lambda x: (x, 1))
	tokenSumPairTuple = tokenCountPairTuple.reduceByKey(lambda a,b: a+b)
	return (tokenSumPairTuple.map(lambda x: (x[0], float(N)/x[1])))


def tfidf(tokens, idfs): 
	""" Compute TF-IDF 
	Args: 
		tokens (list of str): input list of tokens from tokenize idfs (dictionary): record to IDF value 
	Returns: 
		dictionary: a dictionary of records to TF-IDF values 
	"""
	tfs = tf(tokens)
	tfIdfDict = {k: v*idfs[k] for k, v in tfs.items()}
	return tfIdfDict

