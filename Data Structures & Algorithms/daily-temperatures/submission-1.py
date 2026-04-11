class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        
        for i in range(len(temperatures)):
            if stack:
                if temperatures[i] <= temperatures[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and temperatures[i] > temperatures[stack[-1]]:
                        index = stack.pop()
                        result[index] = i - index
                    stack.append(i)
            else:
                stack.append(i)

        
        return result

            
            