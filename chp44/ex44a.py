# Implicit Inheritance


class Parent(object):
    def implicit(self):
        print "PARENT implicit()"


class Child(Parent):
    pass # The use of pass under the class Child: is how you tell Python that you want an empty block.

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
