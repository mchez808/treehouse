# Finish the prereqs function so that it recursively finds all of the prerequisite
# course titles in courses (like "Object-Oriented Python" is a prerequisite for
# "Django Basics"). You should add() the title of the prerequisite to the pres set
#  and then call prereqs again with the child courses.
#
# In the end, return the prereqs set.
#
courses = {'count': 2,
           'title': 'Django Basics',
           'prereqs': [{'count': 3,
                     'title': 'Object-Oriented Python',
                     'prereqs': [{'count': 1,
                               'title': 'Python Collections',
                               'prereqs': [{'count':0,
                                         'title': 'Python Basics',
                                         'prereqs': []}]},
                              {'count': 0,
                               'title': 'Python Basics',
                               'prereqs': []},
                              {'count': 0,
                               'title': 'Setting Up a Local Python Environment',
                               'prereqs': []}]},
                     {'count': 0,
                      'title': 'Flask Basics',
                      'prereqs': []}]}

c = courses
print("len(str(c))")
print(len(str(c)))
print("-"*12)

list_1 = c['prereqs']
print("len(str(list_1))")
print(len(str(list_1)))
if list_1:
    print("<<< NOT empty list >>>")
print("-"*12)

i=0
if type(c) != type(list_1[i]):
    raise TypeError("Hi, it's Mark :)  cannot continue recursion.")
list_2 = list_1[i]['prereqs']
print("len(str(list_2))")
print(len(str(list_2)))
if list_2:
    print("<<< NOT empty list >>>")
print("-"*12)

i=0
if type(c) != type(list_2[i]):
    raise TypeError("Hi, it's Mark :)  cannot continue recursion.")
list_3 = list_2[i]['prereqs']
print("len(str(list_3))")
print(len(str(list_3)))
if list_3:
    print("<<< NOT empty list >>>")
print("-"*12)

i=0
if type(c) != type(list_3[i]):
    raise TypeError("Hi, it's Mark :)  cannot continue recursion.")
list_4 = list_3[i]['prereqs']
print("len(str(list_4))")
print(len(str(list_4)))
if list_4:
    print("<<< NOT empty list >>>")
print("-"*12)




a = []
for dict in courses['prereqs']:
    a.append(dict['prereqs'])




def prereqs(data, pres=None):
    pres = pres or set()
