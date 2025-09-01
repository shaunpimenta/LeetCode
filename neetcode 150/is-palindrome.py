import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss=re.sub("[^a-zA-Z0-9]","",s)
        ss=ss.lower()
        return ss==ss[::-1]