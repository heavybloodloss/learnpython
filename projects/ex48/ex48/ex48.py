# writing my lexicon for better user inputs

def convert_numbers(s):
    try:
        return int(s)
    except ValueError:
        return None


stuff = raw_input("> ")
words = stuff.split()

first_word = ('direction', 'north')
second_word = ('verb', 'go')
sentence = [first_word, second_word]

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
    ('nouns', 'cabinet')
}


# def lexicon(self, input):
#     self.input = words
