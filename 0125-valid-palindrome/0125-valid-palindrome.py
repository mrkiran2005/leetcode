class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        rev=""
        for char in s:
            if char.isalpha() or char.isdigit():
                rev=rev+char
        print(rev)
        return rev==rev[::-1]
        """
        :type s: str
        :rtype: bool
        """
        