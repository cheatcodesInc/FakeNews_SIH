from Dictionary import text2, text

list_text = text.split()
hashtags = []
set_hash = ()
for lt in list_text:
    if lt[0] == '#':
        newlt=[]
        for items in lt:
            if items=='#' or items.isalpha() or items.isdigit():
                newlt.append(items)
        hashtags.append(''.join(newlt))
set_hash = set(hashtags)
set_hash_final = list(set_hash)

list_text = text2.split()
hashtags = []
set_hash = ()
for lt in list_text:
    if lt[0] == '#':
        newlt = []
        for items in lt:
            if items == '#' or items.isalpha() or items.isdigit():
                newlt.append(items)
        hashtags.append(''.join(newlt))
set_hash = set(hashtags)
set_hash_final += list(set_hash)
