# code challenge. Compare and Contrast
# source: Treehouse
# https://teamtreehouse.com/library/objectoriented-python-2/dice-roller/compare-and-contrast

# Objective: to compare songs by their length (measured in whole seconds).
#    Add the required methods for ==, <, >, <=, and >= comparisons.
#    Probably a good idea to be able to convert Songs to ints, too, huh?

class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

    def __int__(self):
        return int(self.length)

    def __eq__(self, other):
        return int(self) == int(other)

    def __ne__(self, other):
        return int(self) != int(other)

    def __lt__(self, other):
        return int(self) < int(other)

    def __le__(self, other):
        return int(self) <= int(other)

    def __gt__(self, other):
        return int(self) > int(other)

    def __ge__(self, other):
        return int(self) >= int(other)



# song1 = Song('Bush', 'Glycerine', 260)
# song2 = Song('Blur', 'Song #2', 170)
# song3 = Song('PUSA', 'Lump', 260)

