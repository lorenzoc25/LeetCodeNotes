# get wrong answer 1 times: wrongly used < instead of <= at line 16
# monotonic stack approach


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        ans = [0]*len(T)
        
        # starting from the back, we construct a monotonic stack
        i = len(T) -1;
        
        # loop backward to find minimum value that is greater than the previous one
        
        while i >= 0:
            # if the top of the stack is less than the index, it can't be the next greater val of its previous element(T[i-1])
            while stk and T[stk[-1]] <= T[i]: 
                stk.pop() 
            # at the current index, there's no value that's greater than it
            if not stk:
                ans[i] = 0
            else:
            # if there is a value on the stack, it would be the position of the next greater element
                ans[i] = stk[-1] - i
            # push the current index into the stack
            stk.append(i)
            i -= 1
        
        return ans