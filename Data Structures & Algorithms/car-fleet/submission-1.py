class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # First sort by position
        # If the most behind one has a lower speed then the next in the list
        # then we know it will never catch up. we add one to the count
        # We then pop this dragger off the list and look at the next 2
        # while they can catch, up, appen
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse = True)
        stack = []
        for p, s in cars:
            stack.append((target - p) / s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)


        





        

    
        