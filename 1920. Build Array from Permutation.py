#Solution du premier problème : (1920. Build Array from Permutation)
class Solution(object):
    def buildArray(self, nums):
        list=[]
        for i in range(len(nums)):
            list.append(nums[nums[i]])
        return(list)
