class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mymap = defaultdict(int)

        for i in range(len(nums)):
            mymap[nums[i]] += 1

        for i,j in mymap.items():
            if j > ((len(nums))/2) or j == (len(nums)/2):
                return i
        
        return -1