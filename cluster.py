import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

from db import verifiedTweetDict

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words=set(stopwords.words('english'))
lemma=WordNetLemmatizer()

def preprocess( text ):
    
    text = re.sub( r'\W', ' ', str( text ))
    text = re.sub( r'\s+[a-zA-Z]\s+', ' ', text )
    text = re.sub( r'\^[a-zA-Z]\s+', ' ', text )
    text = re.sub( r'\s+', ' ', text )
    text = re.sub( r'^b\s+', '', text )
    
    tokenize = nltk.tokenize.word_tokenize( text )
    tokenize = [ word.lower() for word in tokenize if word.isalpha() ]
    nonStops = [ i for i in tokenize if i not in stop_words ]    
    lemmas = [ lemma.lemmatize(i) for i in nonStops ]    
    tokens = [ word for word in lemmas if len( word ) > 5 ]
    
    return tokens

# This function returns the dict of label: clusterID from the clusterLabels
def getClusterOfIds( clusterLabels, tweetDictionary ):
    
    tweetDict = {}
    for i, j in enumerate( clusterLabels ):
        if j not in tweetDict:
            tweetDict[j] = [i]
        else:
            tweetDict[j].append(i)

    labelizedIds = {}
    keysList = list(tweetDictionary.keys())
    for i, j in tweetDict.items():
        for k in j:
            if i not in labelizedIds:
                labelizedIds[i] = [ keysList[k] ]
            else:
                labelizedIds[i].append( keysList[k] )

    return labelizedIds