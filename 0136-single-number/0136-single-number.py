class Solution(object):
    def singleNumber(self, nums):
        d1={}
        for element in d1:
            if element in d1:
                d1[element]=d1[element]+1
            else:
                d1[element]=1
        for key,value in d1.items():
            if value==1:
                return key

        """
        :type nums: List[int]
        :rtype: int
        """
        