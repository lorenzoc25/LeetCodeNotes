# this way is kinda of a cheating way to do this problem
# and this is a daily challenge problem
# but basically, we just need to find out the maximal digit and we are done

class Solution:
    def minPartitions(self, n: str) -> int:
        m = 0  # max digital value
        for i in range(len(n)):
            # we could also simplify a bit by add if int(n[i] == 9): return
            m = max(int(n[i]), m)
        return m
