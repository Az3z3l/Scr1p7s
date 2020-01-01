#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import string
import hashlib


ALLOWED_CHARACTERS = string.ascii_letters+string.digits
NUMBER_OF_CHARACTERS = len(ALLOWED_CHARACTERS)

def characterToIndex(char):
    return ALLOWED_CHARACTERS.index(char)

def indexToCharacter(index):
    if NUMBER_OF_CHARACTERS <= index:
        raise ValueError("Index out of range.")
    else:
        return ALLOWED_CHARACTERS[index]

def listToString(s):  
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  


def next(string):
    """ Get next sequence of characters.
    Treats characters as numbers (0-255). Function tries to increment
    character at the first position. If it fails, new character is
    added to the back of the list.
    It's basically a number with base = 256.
    :param string: A list of characters (can be empty).
    :type string: list
    :return: Next list of characters in the sequence
    :rettype: list
    """
    if len(string) <= 0:
        string.append(indexToCharacter(0))
    else:
        string[0] = indexToCharacter((characterToIndex(string[0]) + 1) % NUMBER_OF_CHARACTERS)
        if characterToIndex(string[0]) is 0:
            return list(string[0]) + next(string[1:])
    return string

# def shacollision(cs):
#     result=hashlib.sha1(cs.encode()) 
#     result=result.hexdigest()
#     result=str(result)
#     # print result
#     result=result[0:4]
#     if (result=="7c00"):
#         print "[------>]"+cs+"=========="+result
#         # exit(0)
#     return result



def main():
    sequence = list()
    status=True
    while status:
        sequence = next(sequence)
        string=listToString( sequence)
        print string
        # sha=shacollision(string)




if __name__ == "__main__":
    main()

