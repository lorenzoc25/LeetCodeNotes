  Since we are traversing from the begining to the end, if we encounter a left parenthesis, we need a right to close it. But if we encounter a right parenthesis 
before a left parenthesis, we'd have to insert a left right away to make sure it's valid.
  So, we can set 2 variables to record the time we need to insert a left parenthesis and the number of right parenthesis we need to have(so we can add it to the end)
to make the whole parenthesis string valid.

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        numInsertionOfLeft,needAddRight = 0,0
        for c in s:
            if c == '(':
                needAddRight += 1
            elif c == ')':
                needAddRight -= 1
                if needAddRight == -1:
                    # need add left parenthesis
                    needAddRight = 0
                    numInsertionOfLeft += 1
        return numInsertionOfLeft + needAddRight
```
