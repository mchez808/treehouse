
class Robot1(object):
    """Python does not have the private keyword, unlike some other object oriented languages, but encapsulation can be done.
        Instead, it relies on the convention: a class variable that should not directly be accessed should be prefixed with an underscore.
    """
    def __init__(self):
        self.a = 123
        self._b = 123
        self.__c = 123


obj = Robot1()
print(obj.a)
print(obj._b)
print("Quiz: does this line throw an error?  (y/n)")
ans = input('print(obj.__c)  ')
print("Yes, yes it does.")
if ans != 'y':
    print(obj.__c)
try:
    print(obj.__c)
except AttributeError:
    print("A single underscore: Private variable, it should not be accessed directly. But nothing stops you from doing that (except convention).")
    input("A double underscore: Private variable, harder to access but still possible.")


class Robot2(object):
    """Private variables are intended to be changed using getter and setter methods.
        These provide indirect access to them:
    """
    def __init__(self):
        self.__version = 22

    def getVersion(self):
        print(self.__version)

    def setVersion(self, version):
        self.__version = version


obj = Robot2()
obj.getVersion()
obj.setVersion(23)
obj.getVersion()
print("Quiz: does this line throw an error?  (y/n)")
ans = input('print(obj.__version)  ')
print("Yes, yes it does.")
if ans != 'y':
    print(obj.__version)
try:
    print(obj.__version)
except AttributeError:
    input("Private variables are intended to be changed using getter and setter methods. These provide indirect access to them.")
