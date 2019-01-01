def hist(string):
    frequency = {}
    for word in string.split(' '):
        frequency.setdefault(word.lower(),0)
        frequency[word.lower()]+=1
    return frequency