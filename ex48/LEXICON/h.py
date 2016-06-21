direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verb = ('go', 'stop', 'kill', 'eat')
stop = ('the', 'in', 'of', 'from', 'at', 'it')
noun = ('door', 'bear', 'princess', 'cabinet')
number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
error_message = "wrong choice!"


def scan(word, *words):  # '*words' lets you give a variable number of arguments to a function
    # split the passed arguments
    words = word.lower().split()

    src = {frozenset(direction): 'direction',
           frozenset(verb): 'verb',
           frozenset(stop): 'stop',
           frozenset(noun): 'noun',
           frozenset(number): 'number'
           }
    for word in words:
        for k, v in src.items():
            if word in k:
                m = v
                # break

    return [('direction', w) for w in words if w in src.items()]
# ---------------------------------------------------

# Singles string as key are prefered (just my opinion)
src = {'direction': direction,
       'verb': verb,
       'stop': stop,
       'noun': noun,
       'number': number}


def scan(word, *words):
    words = word.split() if not words else words
    for word in words:
        for k, v in src.items():
            if word in v:
                print((word, k))


def scan_with_ret(word, *words):
    words = word.split() if not words else words
    ret = []
    for word in words:
        for k, v in src.items():
            if word in v:
                ret.append((word, k))
    return ret


def scan_with_ret_oneliner(word, *words):
    words = word.split() if not words else words
    return [(word, k) for word in words for k, v in src.items() if word in v]


print("scan")
scan("I was going north and south")

print("scan_with_ret")
print(scan_with_ret("I was going north and south"))

print("scan_with_ret_oneliner")
print(scan_with_ret_oneliner("I was going north and south"))
