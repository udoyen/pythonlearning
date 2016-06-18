class lexicon(object):

    direction = (north, south, east, west, down, up, left, right, back)
    verb = (go, stop, kill, eat)
    stop_word = (the, in, of, from, at, it)
    noun = (door, bear, princess, cabinet)
    number = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) 
    
    def __init__(self, sentence):
        
        self.sentence = sentence
        self.direction = direction
        self.verb = verb
        self.noun = noun
        self.number = number


    def scan(self, sentence):
        return sentence
          
