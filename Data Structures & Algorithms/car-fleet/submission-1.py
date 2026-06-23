class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # destination is target miles away
        # position and speed lists are of equal size
        # repersent ith cars speed and position
        # return how many car fleets are at destination
        # cars cant pass only speed up to the one infront
        # so cars can chunk up, but single car is also considered a car fleet
        # start from car closest to dest, see when it will arrive and check the one behind it
        # if one behind time = or greater they turn into a fleet how to do this?
        # keep track of inital fleets if above condition -1 from that trcker then return that tracker

        # need formula to calcualte time a car will get to dest
        # (target - pos)/speed = time

        # need to sort arrays in descending order after putting in stack.
        stack = []
        for i in range(len(position)):
            stack.append([position[i],speed[i]])

        # stack now has values together per car
        # sort stack from highest pos to low
        sorted_stack = sorted(stack, key=lambda x: x[0], reverse=True)
        
        # its now sorted

        fleet_size = 0
        slowest_time = 0

        # do math to see if second fleet can catch first, if not continue, if it can
        # remove the second fleep and decremtn fleet_size
        for pos, speed in sorted_stack:
            time = (target - pos)/ speed
            if time > slowest_time:
                fleet_size += 1
                slowest_time = time
        return fleet_size
        