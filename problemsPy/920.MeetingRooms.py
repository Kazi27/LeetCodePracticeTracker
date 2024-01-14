
# Problem:
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

# Example 1:
# Input: intervals = [(0,30),(5,10),(15,20)]
# Output: false
# Explanation: (0,30), (5,10) and (0,30),(15,20) will conflict

# Example 2:
# Input: intervals = [(5,8),(9,15)]
# Output: true
# Explanation: Two times will not conflict 

#Solution:
from typing import (
    List,
)

#Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key = lambda i : i.start) #sort intervals array based on start, key and lamba are just python syntax

        for x in range(1, len(intervals)): #from 1 to the end
            interval1 = intervals[x - 1] #so it'll start at 0
            interval2 = intervals[x] #this will start at 1, increment both

            if interval1.end > interval2.start: #if the second meeting starts before the first one ends, thats a conflict so return false
                return False

        return True #this is outside the loop so if you didnt execute false at all ur here meaning no conflicts so return true