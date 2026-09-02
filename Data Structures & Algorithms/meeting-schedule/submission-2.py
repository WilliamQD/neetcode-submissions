"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        in_sorted = sorted(intervals, key=lambda x: x.start)

        for i in range(1, len(intervals)):
            a = in_sorted[i-1]
            b = in_sorted[i]

            if b.start < a.end:
                return False
        return True
