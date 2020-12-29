import itertools


suits = ['hearts','spades','clubs','diamonds']

cycle_suits = itertools.cycle(suits)


cards = [[''] * 4 for i in range(3)]



list_of_lists = [["test"] * 3 for x in range(10)]






for suit in cycle_suits:
    insert_string = "%s" % suit
    cards = [[insert_string] * 4 for i in range(3)]
