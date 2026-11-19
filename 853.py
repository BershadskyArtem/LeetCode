# https://leetcode.com/problems/car-fleet/

# There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
#
# You are given two integer arrays position and speed, both of length n,
# where position[i] is the starting mile of the ith car and speed[i] is the speed of the ith car in miles per hour.
#
# A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
#
# A car fleet is a single car or a group of cars driving next to each other.
# The speed of the car fleet is the minimum speed of any car in the fleet.
#
# If a car catches up to a car fleet at the mile target, it will still be considered as part of the car fleet.
#
# Return the number of car fleets that will arrive at the destination.

# Example 1:
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
# The fleet forms at target.
# The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6.
# The fleet moves at speed 1 until it reaches target.

# Example 2:
# Input: target = 10, position = [3], speed = [3]
# Output: 1
# Explanation:
# There is only one car, hence there is only one fleet.

class Solution:
    # if the car in front arrives at the dest in 2 hours
    # and another car just behind the front in 1 hour
    # it means that they will collide and form a fleet
    # otherwise no

    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        stack = []
        pairs = [[p, s] for p, s in zip(position, speed)]

        # from front to back (aka in reverse order)
        for pos, s in sorted(pairs)[::-1]:
            arrives_in = (target - pos) / s
            if len(stack) == 0:
                stack.append(arrives_in)
                continue

            if stack[-1] < arrives_in:
                stack.append(arrives_in)
                continue

            the_slowest_car_arrives_in = arrives_in
            while len(stack) != 0 and stack[-1] >= the_slowest_car_arrives_in:
                the_slowest_car_arrives_in = max(stack.pop(), the_slowest_car_arrives_in)

            stack.append(the_slowest_car_arrives_in)

        return len(stack)


sol = Solution()
res = sol.carFleet(12, [10,8,0,5,3], [2,4,1,1,3])
# res = sol.carFleet(100, [0,2,4], [4,2,1])
# res = sol.carFleet(10, [3], [3])
# 1
# res = sol.carFleet(10, [0,4,2], [2,1,3])
# 4
# res = sol.carFleet(12, [4,0,5,3,1,2], [6,10,9,6,7,2])

print(res)
