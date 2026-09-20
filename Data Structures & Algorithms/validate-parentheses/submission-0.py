class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        q = []
        for el in s:
            if el in hashMap:
                if q and q[-1] == hashMap[el]:
                   q.pop()
                else:
                    return False
            else:
                q.append(el)
               

        print(q)
        return not q