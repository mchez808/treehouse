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

def prereqs(data, pres=None):
    pres = pres or set()
    list_of_dicts = data['prereqs']
    if list_of_dicts:
        pres.add(data['title'])
        for dict in list_of_dicts:
            if dict['prereqs']:
                prereqs(dict, pres)
    return pres

required_courses = prereqs(courses)
