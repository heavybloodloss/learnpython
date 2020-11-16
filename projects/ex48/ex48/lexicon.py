# remove comment for "s = raw_input("> ")" to use as a python LUI check
# s = raw_input("> ")

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None


def scan(s):
    directions = ['north', 'south', 'west', 'east']
    verbs = ['go', 'kill', 'eat']
    stops = ['the', 'in', 'of']
    nouns = ['bear', 'princess']

    result = []

    words = s.lower().split()

    for word in words:
        if word in directions:
            result.append(('direction', word))
        elif word in verbs:
            result.append(('verb', word))
        elif word in stops:
            result.append(('stop', word))
        elif word in nouns:
            result.append(('noun', word))
        elif convert_number(word):
            result.append(('number', int(word)))
        else:
            result.append(('error', word))
    print result

    return result

# remove comment for "scan(s)" to use as a python LUI check
# scan(s)
