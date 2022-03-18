import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re
import gensim
from gensim import corpora

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')

stop_words=set(stopwords.words('english'))
lemma=WordNetLemmatizer()
ls = []

def preprocess(doc):
    
    doc = re.sub(r'\W', ' ', str(doc))
    doc = re.sub(r'\s+[a-zA-Z]\s+', ' ', doc)
    doc = re.sub(r'\^[a-zA-Z]\s+', ' ', doc)
    doc =  re.sub(r'\s+', ' ', doc)
    text = re.sub(r'^b\s+', '', doc)
    
    tokenize = nltk.tokenize.word_tokenize(text)
    tokenize = [ word.lower() for word in tokenize if word.isalpha() ]
    nonStops = [ i for i in tokenize if i not in stop_words ]    
    lemmas = [ lemma.lemmatize(i) for i in nonStops ]    
    tokens = [ word for word in lemmas if len( word ) > 5 ]
    
    return tokens

def predTweet( text ):

    text = preprocess( text )
    text = input_dict.doc2bow( text )
    l = lda.get_document_topics( text )
    l.sort(key=lambda x: x[1], reverse=True)
    
    return l[0][0]
