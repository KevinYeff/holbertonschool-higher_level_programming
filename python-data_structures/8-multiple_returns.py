#!/usr/bin/python3
def multiple_returns(sentence):
    firstCharacter = sentence[0:1]
    length = len(sentence)
    if sentence == sentence[0:0]:
        firstCharacter = None
    return (length, firstCharacter)
