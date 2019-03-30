#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 14:31:44 2019

@author: manasikulkarni

In elections that use the ballot box system for voting, each voter writes the name of a candidate on a ballot and places it in the ballot box. The candidate with the highest number
of votes wins the election. If two or more candidates have the same number of votes, then the tied candidates' names are ordered alphabetically and the last name in the alphabetical
order wins.

For example, votes are in the names ['Joe','Mary','Mary','Joe']. Each candidate received two votes, but Mary is alphabetically later than Joe, so she wins.

"""

from collections import Counter

def electionWinner(votes):
    counterList = {}
    newList = []
    
    #Counter creates a dictionary with keys as names and values as number of votes
    counterList.update(Counter(votes))
    
    #Calculating the maximum number of votes
    maxVotes = max(counterList.values())
    
    for key, value in counterList.items():
        if value == maxVotes:
            #For same number of votes, add all the names in newList
            newList.append(key)
    
    #Sort the list in reverse order, so that the last name will be on the top       
    answer = sorted(newList, reverse = True)
    
    return answer[0]

votesList = ['Alex','John','Hari','Alex','Michael','John','Michael','Alex','Michael','John']
res = electionWinner(votesList)
print(res)
    