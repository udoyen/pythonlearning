direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')
number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
error_message = "wrong choice!"

src = {'direction': direction,
       'verb': verb,
       'stop': stop,
       'noun': noun,
       'number': number}


def scan(word, *words):
    words = word.split() if not words else words
    ret = []
    for word in words:
        for k, v in src.items():
            if word in v:
                ret.append((k, word))
    return ret
