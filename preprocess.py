##PATHS
stopfile = os.path.join(baseDir, inputPath, STOPWORDS_PATH)
stopwords = set(sc.textFile(stopfile).collect())



def simpleTokenize(string):
    """ A simple implementation of input string tokenization
    Args:
        string (str): input string
    Returns:
        list: a list of tokens
    """
    return filter(len, re.split(r'\W+', string.lower().strip()))

def tokenize(string):
    """ An implementation of input string tokenization that excludes stopwords
    Args:
        string (str): input string
    Returns:
        list: a list of tokens without stopwords
    """
    return filter(lambda x: x not in stopwords, simpleTokenize(string))


## Lets tokenize small datasets

amazonRecToToken = amazonSmall.map(lambda x: (x[0], tokenize(x[1])))
googleRecToToken = googleSmall.map(lambda x: (x[0], tokenize(x[1])))
def countTokens(vendorRDD):
    """ Count and return the number of tokens
    Args:
        vendorRDD (RDD of (recordId, tokenizedValue)): Pair tuple of record ID to tokenized output
    Returns:
        count: count of all tokens
    """
    return vendorRDD.map(lambda x: len(x[1])).reduce(lambda a,b: a+b)

totalTokens = countTokens(amazonRecToToken) + countTokens(googleRecToToken)
print 'There are %s tokens in the combined datasets' % totalTokens


