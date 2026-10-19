class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack is initally empty, so we add (7, 0)
        # We then check stack and compare is 1 < 7. Yes
        # We take max area from this height which is index - [2] = 7
        # We pop off this elem and add (1, 0 (index 7 was at))
        # We add (7, 2)
        # 2 is less than 7. 7 * (3 - 2) = 7. This is not greater than existing max of 7. We then pop and add (2, 2)
        # Ignore 2 
        # Add (4, 5)
        # We still have elemnts in the stack
        # [0] * (len(heights) - [1])
        stack = []
        maxArea = 0
        for i, height in enumerate(heights):
            index = i
            while stack and height < stack[-1][0]:
                maxArea = max(maxArea, stack[-1][0] * (i - stack[-1][1]))
                index = stack[-1][1]
                stack.pop()
            stack.append((height, index))
        while stack:
            maxArea = max(maxArea, stack[-1][0] * (len(heights) - stack[-1][1]))
            stack.pop()
        return maxArea

            
            
            
        