class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # [1, 4, 2, 3, 2, 5]
        # when we see 4, we know theres the first five numbers must have a repeat (until we see
        # a number higher than 4) 
        # [1, 4, 4, 2, 3, 5]

        slow = nums[0]
        fast = nums[0]

        slow = nums[slow]
        fast = nums[nums[fast]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
                
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow