import yake

from Dictionary import text, text2
from Hashtags import set_hash_final

kw_extractor = yake.KeywordExtractor()
language = "en"
numOfKeywords = 100
max_ngram_size = 4
deduplication_threshold = 0.9
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)

keywords = custom_kw_extractor.extract_keywords(text)
keywords += custom_kw_extractor.extract_keywords(text2)

newKeywords = list()
for kw in keywords:
    l = list(kw[0].split())
    if len(l) >= 2:
        newKeywords.append(kw[0])

# newKeywords = sortList(k)
newKeywords += set_hash_final
# Min of 2-gram and max of 4-gram

sortedKeywords = list()
for i in range(0, len(newKeywords), 10):
    sortedKeywords += newKeywords[i:i+10]

querylist = list()
for j in range(0, len(sortedKeywords), 10):
    newlist = sortedKeywords[j:j + 10]
    query = "(-is:retweet -is:quote -is:reply -is:verified lang:en) ("
    for i in newlist:
        query += "\"" + i + "\" OR "

    query = query[:len(query) - 4]
    query += ')'
    querylist.append(query)
# for items in querylist:
#     print(items)
