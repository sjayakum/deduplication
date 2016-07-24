# deduplication


Entity Resolution (ER) refers to the task of finding records in a dataset that refer to the same entity across different data sources (e.g., data files, books, websites, databases). ER is necessary when joining datasets based on entities that may or may not share a common identifier (e.g., database key, URI, National identification number), as may be the case due to differences in record shape, storage location, and/or curator style or preference. A dataset that has undergone ER may be referred to as being cross-linked.


## Data


The file format of Amazon Product Listing:
"id","title","description","manufacturer","price"

The file format of a Google Product Listing:
"id","name","description","manufacturer","price"



## Entity Resolution as Bag-of-Words (BOW)

A simple approach to entity resolution is to treat all records as strings and compute their similarity with a string distance function.

Here, tokens become the atomic unit of text comparison. 
If we want to compare two documents, we count how many tokens they share in common. The power of this approach is that it makes string comparisons insensitive to small differences that probably do not affect meaning much, for example, punctuation and word order.



## Entity Resolution using Weighted BOWs TF-IDF

Bag-of-words(previous model) comparisons are not very good when all tokens are treated the same: some tokens are more important than others.
Weights give us a way to specify which tokens to favor. With weights, when we compare documents, instead of counting common tokens, we sum up the weights of common tokens. A good heuristic for assigning weights is called "Term-Frequency/Inverse-Document-Frequency".


**Term Frequency** -  This rewards tokens that appear many times in the same document.
That is, more number of times a token (techinically a word) appears in a document (here summary/description of the article) then more important that word is for that document

TF of term that appears **t** times in a document which has **d** tokens is given by **t/d**

**Inverse DOcument Frequency** - This rewards tokens that are rare in overall datasent[which might contain multiple documents].
That is, if 2 or more documents share a rare word rather than a common word then this word is given more weightage.

IDF of a term that appears **n** times accross a total of **N** documents is given by **N/n**

Note that: this TF-IDF is just a we still need some metric to compute the similarity

## Entity Resolution using Cosine Similarity

#### $$ similarity = \cos \theta = \frac{a \cdot b}{\|a\| \|b\|} = \frac{\sum a_i b_i}{\sqrt{\sum a_i^2} \sqrt{\sum b_i^2}} $$



## Results/ Accuracy

#### $$ Fmeasure = 2 \frac{precision * recall}{precision + recall} $$

* #### Precision = true-positives / (true-positives + false-positives)
* #### Recall = true-positives / (true-positives + false-negatives)
* #### F-measure = 2 x Recall x Precision / (Recall + Precision)



## Future Work

#### Similarity Methods

* Simple Matching Coefficient
* Jaccard Coefficient
* Tanimoto Coefficient

