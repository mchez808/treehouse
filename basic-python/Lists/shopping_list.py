# This file, shopping_list.py, contains the most sophisticated functionality
# including infinite loop control flow: break and continue commands
# https://teamtreehouse.com/workspaces/38131302
# ¯\_(ツ)_/¯
 
# Create a new empty list
shopping_list = list()

# Create a function add_to_list that declares parameter item
# Add the item to the list
def add_to_list(item):
    shopping_list.append(item)
    print("Added! Your list now has {} items".format(len(shopping_list)))


def show_list():
    print(shopping_list)


def show_help():
    print("What should we buy?")
    print("""
        Enter 'DONE' when done.
        Enter 'HELP' for this help.
        Enter 'SHOW' to view list.
    """)


print("Welcome to the shopping list.")
show_help()

while True:
    new_item = input("Enter command, or new item  > >  ")
    if new_item.lower() == "done":
        input("Okay, all done with shopping list.")
        break
    elif new_item.lower() == "help":
        show_help()
        continue
        # IMPORTANT: the continue command redirects the flow back up to the [while True] line
    elif new_item.lower() == "show":
        show_list()
        continue
    add_to_list(new_item)

