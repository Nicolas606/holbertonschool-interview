#!/usr/bin/python3
'''Lockboxes'''


def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened'''
    for j in range(len(boxes)):
        if(boxes[j]):
            continue
        else:
            if(j != len(boxes) - 1):
                return False
    return True