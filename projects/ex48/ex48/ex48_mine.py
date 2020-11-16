# writing my lexicon for better user inputs

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None


# first_word = ('direction', 'north')
# second_word = ('verb', 'go')
# sentence = [first_word, second_word]

lexicon = {
    ('directions', 'north'),
    ('directions', 'south'),
    ('directions', 'east'),
    ('directions', 'west'),
    ('directions', 'up'),
    ('directions', 'down'),
    ('directions', 'left'),
    ('directions', 'right'),
    ('directions', 'back'),
    ('verbs', 'go'),
    ('verbs', 'stop'),
    ('verbs', 'kill'),
    ('verbs', 'eat'),
    ('nouns', 'door'),
    ('nouns', 'bear'),
    ('nouns', 'princess'),
    ('nouns', 'cabinet'),
    ('stops', 'at'),
    ('stops', 'the'),
    ('stops', 'of'),
    ('stops', 'in'),
    ('stops', 'from'),
    ('stops', 'it')
}

sentence = raw_input("> ")


def scan(sentence):
    words = sentence.lower().split()
    pairs = []

    for word in words:
        word_type = lexicon[word]
        tupes = (word, word_type)
        pairs.append(tupes)

    return pairs
