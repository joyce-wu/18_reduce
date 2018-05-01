# reduceReuseRecyle - Holden Higgens & Joyce Wu
# Softdev2 pd 7
# k18 -- Reductio ad Absurdum
# 2018-04-30

from functools import reduce

def open_f():
    #opens file and creates list of words in text
    f = open("pope.txt", "r")
    file = f.read()
    return file.split()

#test ary
sample = ['hi', 'hello', 'hola', 'heh', 'hi', 'nihao', 'bonjour', 'hi', 'hello']
#actual book
words = open_f()

#find frequency of single word
def word_freq(word, f):
   return reduce((lambda x,y: x+(1 if y==word else 0)),f,0)
#print word_freq('hello', sample)

#find frequency of group of words
def words_freq(phrase, f):
    split_phrase = phrase.split()
    #print(split_phrase)
    #finds if phrase is found by iterating through list of words
    lst = [1 for w in range(len(f)) if split_phrase == sample[w: w+len(split_phrase)]]
    if lst == []: #no appearance of phrase
        return 0
    return reduce((lambda x, y: x + y), lst) #adds up total frequency

#print words_freq('hola heh', sample)

#find most frequently occurring word
def most_freq(f):
    #creates a set of words without repeating
    unique_words = {x for x in f}
    w={}
    for x in unique_words:
        w[x]=0
    for x in f:
        w[x]+=1
    longest=""
    longfreq=0
    for x in unique_words:
        if w[x]>longfreq:
            longfreq=w[x]
            longest=x
    return longest+" "+str(longfreq)
    #turns back to list so indexOf can be used
    """"print 2
    lst = [x for x in unique_words]
    print 3
    counts = [word_freq(x, f) for x in lst]
    return lst[counts.index(max(counts))] #max num corresponds with word

    #non-list comprehension way
    # current_word = ''
    # current_highest = 0
    # for w in f:
    #     count = word_freq(w, f)
    #     if count > current_highest:
    #         current_word = w
    #         current_highest = count
    # return current_word"""
#print word_freq("the",words)
print most_freq(words)
#print "hi"
