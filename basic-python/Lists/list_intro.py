# quiz of lists

dict_of_lists = {
    'list("Paul")': list("Paul"),
    'list(["Paul"])': list(["Paul"]),
    'list(["Paul", "John"])': list(["Paul", "John"])
    }

def quiz_of_lists(dict_of_lists):
    for key, value in dict_of_lists.items():
        print("=" * 44)
        print("What is the length of this list? ")
        print("    " + str(key))
        guess = int(input("Your guess is: "))
        answer = len(value)
        if bool(guess==answer):
            print("Correct!")
        else:
            print("Sorry. The answer is " + str(answer))
        input("Press Enter")


def insert_first():
    # putting Jesus first in the Beatles
    pass
    # beatles.insert(0, "Jesus")


def quiz_del():
    print("=" * 44)
    print('''
        surname = "Rasputin"
        advisor = surname
        del surname
    
        What is stored in the variable advisor?
        A) 'Rasputin'
        B) NameError, advisor not found
        C) None, the object has been deleted
        ''')
    guess = input()
    while guess.upper() != "A":
        print("Nope, guess again.")
        guess = input()
    print("Well done! That's right! del just deletes the label, not the value. surname is no longer available, but advisor still is.")


def multidimensional_list():
    pass
    '''
    travel_expenses = [ [5.00, 2.75, 22.00, 0.00, 0.00], [24.75, 5.50, 15.00, 22.00, 8.00], [2.75, 5.50, 0.00, 29.00, 5.00], ]
    print("Travel Expenses")
    week_number = 1
    for week in travel_expenses:
        print("****")
        print("* Week #{}: ${}".format(week_number, sum(week)))
        week_number += 1
    '''


quiz_of_lists(dict_of_lists)



quiz_del()

insert_first()

multidimensional_list()


def display_wishlist(display_name, wishes):
    print(display_name + ":")
    suggestions = wishes.copy()
    suggested_gift = suggestions.pop(0)
    print("=========>" + suggested_gift + "<=========")
    for suggestion in suggestions:
        print("* " + suggestion)
        print()

input("view the wishlist feature")
games = ["Bomberman", "Captain Chaos", "X-Men"]
display_wishlist("games", games)


beatles = list(["Paul", "John"])
others = list(["George","Ringo"])
beatles.extend(others)
