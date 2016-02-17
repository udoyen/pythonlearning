from sys import exit
from random import randint



# Class structure from game concept
"""
Map
- next_scene
-opening_scene
Engine
- play
Scene
- enter
  Death
  Central Corridor
  Laser Weapon Armory
  The Bridge
  Excape Pod

"""


# Actual class creation

class Scene(object):
    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "first instance current_scene:  %s" % current_scene
        
        while True:
            print "\n---------"
            next_scene_name = current_scene.enter() # calls the enter function for each scene to get the next_sceene_name
            print "next_scene_name: %s " % next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name) # This serve to change the current scene value
            print "second instance current_scene:  %s" %  current_scene


class Death(Scene):
    quips = [
             "You died. You knida suck at this.",
             "Your mom would be proud...if she were smarter.",
             "Such a luser.",
             "I have a small puppy that's better at this."
         ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        exit(1)    

class CentralCorridor(Scene):
    def enter(self):
        print "This Gothons of Planet Percal #25 invaded your ship and destroyed"
        print "your entire crew. You are the last surviving member and your last"
        print "mission is to get the neutron destruct bomb from the Weapons Armory."
        print "put it in the bridge, and blow ths ship up after getting into an "
        print "escape pod."
        print "\n"
        print "You\'re running down the central corridpr to the Weapons Armory when"
        print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print "flowing around his hate filled body. He\'s blocking the door to the"
        print "Armory and about to pull a weapon to blast you."
        print "\n"
        print "Try one of this if you don't know what to do: shoot!, dodge!, or tell a joke"

        action = raw_input("> ")
        

        if action == "shoot!":
            print "Quick on the draw you yank out your blaster and fire it at the Gothon."
            print "His clown costume is flowing and moving around his body, which throws"
            print "off your aim. Your laser hits his custom but misses him entirely. This"
            print "completely ruins his brand new costume his mother bought him, which"
            print "makes him fly into a rage and blast you repeatedly in the face until"
            print "you are dead. Then he eats you."
            return 'death'
        
        elif action == "dodge!":
            
            print "Like a world class boxer you dodge, weave, slip and slide right"
            print "as th Gothon's blaster cranks a laser past your head."
            print "In the middle of your artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out."
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you."
            return 'death'

        elif action =="tell a joke":
            print "Lucky for you they made you learn Gothon insults in the acedemy."
            print "You tell the one Gothon joke you know:"
            print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr."
            print "The Gothon stops , tries not to laugh, then busts out laughing and can't move."
            print "while he's laughing you run up and shoot him square in the head"
            print "putting him down, then through then jump through the Weapon Armory door."
            return 'laser_weapon_armory'
        else:
            print"DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print "You do a dive roll into the Weapon Armory, crouch and scan the room"
        print "for more Gothons that might be hiding. It's dead wuiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "neutron bomb in its container. There's a keypad lock on the box"
        print "and you need the code to get the bomb out. if you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "If your feeling lucky you may try this number: %s" % code
        guess = raw_input("[keypad]> ")
        guesses = 1
       
        
        while guess != code and guesses < 10:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print "You grab the neutron bomb and run as fast as you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickening"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'


class TheBridge(Scene):
    def enter(self):
        print "You burst unto the Bridge with the neutron destruction bomb"
        print "under our arm and surprise 5 Gothons who are tring to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pulled their"
        print "weapons out yet, as they see the active bomb under your"
        print "arm and don't want to set it off."
        print "\n"
        print "suggested response: 'slowly place the bomb'"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "In a panic you throw the bomb at the group of Gothons."
            print "and make a leap for the door. Rights as you drop it a"
            print "Gothon shoots you right in the back killing you."
            print "As you die you see another Gothon frantically try to disarm"
            print "the bomb. You die knowing they will probably blow up when"
            print "it goes off."
            return 'death'
        elif action == "slowly place the bomb":
            print "You point your blaster at the bomb under your arm"
            print "and the Gothons put their hands up and start to sweat."
            print "You inch backward to the door, open it, and then carefully"
            print "place the bomb on the floor, pointing your blaster at it."
            print "You then jumpback through the door, puch the close button"
            print "and blast the lock so the Gothons can't get out."
            print "Now that the bomb is placed you run to the escape pod to"
            print "get off this tin can"
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"


class EscapePod(Scene):
    def enter(self):
        print "You rush through the ship desperately trying to make it to"
        print "the excape pad before the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interference. You get to the chamber with the escape pods, and"
        print "now need to pick one to take. SOme of them could be damaged"
        print "but you don't have time to look. There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        print "I would suggest the pod number of: %s" % good_pod
        guess = raw_input("[pad #]> ")

        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planet below. As it flies to the planet, you look"
            print "back ans see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"

            return 'finished'



class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
        }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
      
    def next_scene(self, scene_name):
        print "get function calls:  %s" % Map.scenes.get(scene_name)
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
        """ """


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

"""
STUDY DRILLS

1. Door lock guessing 11 times, why? 
   answer: guesses variable set to 0 rather than .

2. How the returning the next door works?
   answer: The engine class uses the while loop in the play function to juggle through
           the variuos doors.
           The return value of the enter function of each scene class will give the next scene
           which then becomes the current_scene and has its enter function called. This continues
           until Map class opening_scene function returns no value.


 """
