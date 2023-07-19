def threeSum(self, nums: List[int]) -> List[List[int]]:
    combinations=set()
    length = len(nums)
    nums.sort()
        
    for i in range(0, length-2):
        left=i+1
        right=len(nums)-1
        while left < right:
            sum_val=nums[i]+nums[left]+nums[right]
            if sum_val==0:
                combinations.add((nums[i],nums[left],nums[right]))
                left +=1
            elif sum_val > 0:
                right -=1
            elif sum_val < 0:
                left +=1
    return combinations 