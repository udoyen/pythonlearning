class lexicon(object):

    direction = [('direction', 'north'),('direction', 'south'), ('direction', 'east'), 
                 ('direction', 'west'), ('direction', 'down'), ('direction','up'), 
                 ('direction'), ('direction', 'left'), ('direction', 'right'), ('direction', 'back')]
    verb = [('ver', 'go'), ('verb', 'stop'), ('verb', 'kill'), ('verb', 'eat')]
    stop_word = [('stop_word', 'the'), ('stop_word', 'in'), ('stop_word', 'of'), ('stop_word', 'from'), 
                 ('stop_word', 'at'), ('stop_word', 'it')]
    noun = [('noun', 'door'), ('moun', 'bear'), ('noun', 'princess'), ('noun', 'cabinet')]
    number = [('number', '0'), ('number', '1'), ('number', '2'), ('number', '3'), ('number', '4'), 
              ('number', '5'), ('number', '6'), ('number', '7'), ('number', '8'), ('number', '9')]

     
    def __init__(self):
        
        self.sentence = sentence
        self.direction = direction
        self.verb = verb
        self.noun = noun
        self.number = number


    def scan(self, sentence):
	    stuff = raw_input('> ')
	    words = stuff.split()
	
        return sentence

          
