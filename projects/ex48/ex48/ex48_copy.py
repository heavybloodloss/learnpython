# taken from https://stackoverflow.com/questions/15424895/creating-lexicon-and-scanner-in-python
lexicon = {
    ('directions', 'north'),
    ('directions', 'south'),
    ('directions', 'east'),
    ('directions', 'west'),
    ('verbs', 'go'),
    ('verbs', 'stop'),
    ('verbs', 'look'),
    ('verbs', 'give'),
    ('stops', 'the'),
    ('stops', 'in'),
    ('stops', 'of'),
    ('stops', 'from'),
    ('stops', 'at')
    }

def scan(sentence):

    words = sentence.lower().split()
    pairs = []

    for word in words:
        word_type = lexicon[word]
        tupes = (word, word_type) 
        pairs.append(tupes)

    return pairs