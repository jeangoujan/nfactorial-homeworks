"""
💎 Exercise-1 (Longest Consecutive Sequence):
Write a function "longest_consecutive(my_list: list[int]) -> int" that takes a 
list of integers and returns the length of the longest consecutive elements 
sequence in the list. The list might be unsorted.

Example:

longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
"""


def longest_consecutive(my_list: list[int]) -> int:
    counter = 1
    if not my_list:
        counter = 0
    for i in set(my_list):
        if (i+1 or i-1) in set(my_list):
            counter = counter + 1
    return counter


"""
💎 Exercise-2 (Find missing number):
Write a function "find_missing(my_list: list[int]) -> int" that takes a 
list of integers from 1 to n. The list can be unsorted and have one 
number missing. The function should return the missing number.

Example:

find_missing([1, 2, 4]) -> 3
"""


def find_missing(my_list: list[int]) -> int:
    new_list = list(range(my_list[0], my_list[-1]+1))
    for i in new_list:
        if i not in my_list:
            return i
        elif 1 not in my_list:
            return 1


"""
💎 Exercise-3 (Find duplicate number):
Write a function "find_duplicate(my_list: list[int]) -> int" that takes a list 
of integers where each integer is in the range of 1 to n (n is the size of the list). 
The list can have one number appearing twice and the function should return this number.

Example:

find_duplicate([1, 3, 4, 2, 2]) -> 2
"""

def find_duplicate(my_list: list[int]) -> int:
    counter = 0
    frequent_num = int()
    if not my_list:
        counter = None
        frequent_num = None
    for i in my_list:
        if my_list.count(i) > counter:
            counter = my_list.count(i)
            frequent_num = i
    return frequent_num



"""
💎 Exercise-4 (Group Anagrams):
Write a function "group_anagrams(words: list[str]) -> list[list[str]]" that 
takes a list of strings (all lowercase letters), groups the anagrams together, 
and returns a list of lists of grouped anagrams.

An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly once.

group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) 
-> [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
"""


def group_anagrams(words: list[str]) -> list[list[str]]:
    pass