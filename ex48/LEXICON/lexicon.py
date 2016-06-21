import re

direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')
# number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
error_message = "wrong choice!"

src = {'direction': direction,
       'verb': verb,
       'stop': stop,
       'noun': noun
       }


def scan(word, *words):
    words = word.split() if not words else words

    # create an empty list
    ret = []

    # use regular expression to determine if number was passed
    m = r"^[0-9]+"
    p = re.compile(m, re.IGNORECASE)

    for word in words:
        # match regex with pass arguments
        pmatch = p.match(word)
        if pmatch:
            ret.append(('number', int(word)))
        for k, v in src.items():
            if word in v:
                ret.append((k, word))
    return ret
