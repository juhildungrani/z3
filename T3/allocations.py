from random import randint, seed
from pprint import pprint


seed(9963148)  


def get_preferences(nm: int, nl: int):
    return [[randint(0,5) for i in range(nm)] for j in range(nl)]  # nl x nm matrix

if __name__=='__main__':
    nm = 20 # number of modules
    nl = 6  # number of lecturers
    preferences = get_preferences(nm, nl)
    pprint(preferences)
