
import yake

kw_extractor = yake.KeywordExtractor()
language = "en"
numOfKeywords = 20
max_ngram_size = 4
deduplication_threshold = 0.9
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=numOfKeywords, features=None)


text = 'pm narendramodi to address the valedictory function of 96th common foundation course at lbsnaa on 17th march via video conferencing. he will also inaugurate the new sports complex & dedicate revamped happy valley complex to the nation. read'

keywords = custom_kw_extractor.extract_keywords(text)

print(type(keywords))

for kw in keywords:
    print(kw)