class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        ssort = sorted(s.lower())
        tsort = sorted(t.lower())

        if ssort == tsort:
            return True
        return False


print(Solution.isAnagram(Solution,"anagram", "nagaram"))
strs = ["eat","tea","tan","ate","nat","bat"]
print(strs[0])
