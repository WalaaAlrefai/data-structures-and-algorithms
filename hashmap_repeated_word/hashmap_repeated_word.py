from hash_table.hash_table import Hashtable

def repeated_word(string):
    valid_chars = "abcdefghijklmnopqrstuvwxyz "
    words = "".join([i for i in string.lower() if i in valid_chars])
    hashs = Hashtable()
    for i in words.split():
        if hashs.has(i):
            return i
        hashs.set(i, "i")

    return "no words found"

text1='Once upon a time, there was a brave princess who...'
text2='It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...'
text3='It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...'
print(repeated_word(text1))
print()
print(repeated_word(text2))
print()
print(repeated_word(text3))