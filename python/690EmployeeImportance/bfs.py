"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp = {}
        sub = {}
        for emp in employees:
            imp[emp.id] = emp.importance
            sub[emp.id] = emp.subordinates
        res = 0
        queue = deque()
        queue.append(id)
        while queue:
            idx = queue.popleft()
            res += imp[idx]
            if sub[idx] != []:
                for i in sub[idx]:
                    queue.append(i)
        return res
