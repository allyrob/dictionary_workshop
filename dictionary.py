stores = {"target":["socks", "soap", "detergent", "sponges"], 
            "bi-rite": ["butter", "cake", "cookies", "bread"],
            "safeway": ["oreos", "soda", "brownies"],
            "berkeley bowl": ["apples", "oranges", "bananas", "milk"],}



def main_menu():
    print """
    0 - Main Menu
    1 - Show all lists.
    2 - Show a specific list.
    3 - Add a new shopping list.
    4 - Add an item to a shopping list.
    5 - Remove an item from a shopping list.
    6 - Remove a list by nickname.
    7 - Exit when you are done.
    """

def show_lists():
    print stores.keys()


def show_specific_lists(specific_store):
    print stores[specific_store]

def add_new_list():
    pass

def add_item():
    pass

def remove_item():
    pass

def remove_list():
    pass

def exit_lists():
    pass

def main(): 
    main_menu()
    show_lists()
    show_specific_lists("target")
    add_new_list()
    add_item()
    remove_item()
    remove_list()
    exit_lists()







if __name__ == '__main__':
    main()
