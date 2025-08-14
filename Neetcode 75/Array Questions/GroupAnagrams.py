# Group Anagrams
# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram_dict = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in anagram_dict:
                anagram_dict[sorted_str] = []
            anagram_dict[sorted_str].append(s)
        return list(anagram_dict.values())
    


    