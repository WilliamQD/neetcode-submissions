class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) # O(nlogn) for sorting

        stack = []

        for car in cars:
            time_to_dest = (target - car[0]) / car[1]

            if not stack:
                stack.append(time_to_dest)
            else:
                if time_to_dest > stack[-1]:
                    stack.append(time_to_dest)
        
        return len(stack)