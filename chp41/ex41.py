import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []


PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
       "From *** get the *** function, and call it with parameters self, @@@.",

}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True


# load up the words from the website
# opens the website and reads text lines striped of spaces
# and appends to the WORDS list
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    # using list comprehension function capitalize every randomly picked class name from WORDS list
    # the number of words is determined by the "snippet.count()" function from the random module 
    class_names = [w.capitalize() for w in random.sample(WORDS, snippet.count("%%%"))]
    
    print class_names # debug statement
    
    # using random function pick randomly selected WORDS list elements, using "snippet.count()"
    # as the basis for the number picked
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    # generate parameter names based on the random number between 1 and 3
    # and place them in list "param_names" separated by a "," character
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # assign the contents or value of snippet and phrase to variable "result"
    """ Run this whole set function for both "snippet and phrase" 
        changing the "%%%", "@@@", and "***" string to elements of
        class_names, other_names, and param_names as created above """
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1) # replace the "%%%" string in snippet with the generated class names

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)


        # fake paramter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

# keep going until they hit CTRL-D

try:
    while True: # continue this operation until no more data, hence becomes false
        snippets = PHRASES.keys() # set the "key" variable in PHRASES to snippets
        random.shuffle(snippets) # shuffle these "keys"

        for snippet in snippets: # name every snippet(key) snippet
            phrase = PHRASES[snippet] # assign the value of each key(in dictionary PHRASES) as snippet in snippets to phrase
            question, answer = convert(snippet, phrase) # assign "snippet to question" and "phrase to answer"
            
            # if you enter "english" argument at the commandline, then the if statement runs
            # this interchanges the question making it an answer and vice versa
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER:  %s\n\n" % answer
except EOFError:
    print "\nBye"
