# Meeting Schedule
# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

# Example 1:

# Input: intervals = [(0,30),(5,10),(15,20)]

# Output: false

# Explanation:
# (0,30),(5,10) and (0,30),(15,20) will conflict

# Example 2:
# Input: intervals = [(5,8),(9,15)]

# Output: true

# Note:

# (0,8),(8,10) is not considered a conflict at 8
from typing import List

"""
Definition of Interval:

"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if(len(intervals)==0):
            return True
        sorted_intervals = sorted(intervals, key=lambda x: x.start)
        prev = sorted_intervals[0]

        for index in range(1, len(sorted_intervals)):
            curr = sorted_intervals[index]
            if curr.start < prev.end:
                return False
            prev = curr
        
        return True

# intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
intervals = [Interval(5,8),Interval(9,15)]

solulu = Solution()
print(solulu.canAttendMeetings(intervals))