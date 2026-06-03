class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) # O(nlogn) for sorting

        stack = []

        for p, s in cars:
            time_to_dest = (target - p) / s
            
            # If stack is empty OR this car takes longer than the fleet ahead of it,
            # it cannot catch up and forms a new fleet.
            if not stack or time_to_dest > stack[-1]:
                stack.append(time_to_dest)
                
        return len(stack)