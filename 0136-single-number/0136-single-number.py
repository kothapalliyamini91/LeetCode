class Solution:
    def singleNumber(self, nums):
        dic = {}
        for num in nums:
            if not num in dic: dic[num]=1
            else: dic.pop(num)
        return list(dic.keys())[0]
