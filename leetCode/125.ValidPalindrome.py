#Reminder: convert to lowercase
class Solution:
    def isPalindrome(self, s: str) -> bool:
        slow = ""
        for c in s:
            if c <= 'Z' and c >= 'A':
                c = c.lower()
            if c <= 'z' and c >= 'a' or c <= '9' and c >= '0':
                slow += c
        size = len(slow)
        for i in range(size//2):
            if slow[i] != slow[size-1-i]:
                return False
        return True





s = "A man, a plan, a canal: Panama"
print(Solution.isPalindrome(Solution,s))
