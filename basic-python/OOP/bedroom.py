# rileywestonmiller@outlook.com

class Bed:

    softness = ["soft", "med", "hard"]  # the huge takeaway is written at bottom

    def __init__(self):
        self.is_made = True

    def make(self):
        self.is_made = True

    def sleep(self):
        self.is_made = False

mybed = Bed()
yourbed = Bed()
print(mybed.softness)
print(yourbed.softness)

input('Press any key to continue...')
print('\nExecuting this line:\n\n mybed.softness.append("very_hard")\n# appends to list mybed.softness')
mybed.softness.append("very_hard")
input('Press any key to continue...')

print('\nQuestion: what happens when you execute this line?\n print(yourbed.softness)\n')
print('read the comments to understand this IMPORTANT OOP behavior.')

"""
There is a class object, an object called class.

mutable and immutable objects are treated differently when it comes to encapsulation



"""
