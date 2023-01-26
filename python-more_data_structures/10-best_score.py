#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == "":
        return None
    bestScore = None
    bestKey = None

    for key, value in (a_dictionary.items()):
        if bestScore is None or value > bestScore:
            bestScore = value
            bestKey = key
    return bestKey
