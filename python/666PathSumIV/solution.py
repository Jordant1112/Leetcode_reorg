class Solution:
    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = 0
        self.d = {}
        self.sum = 0
        for n in nums:
            val = n % 10
            code = n // 10
            self.d[code] = val
        root_code = nums[0]//10
        self.traverse(root_code, res)
        return res

    def traverse(self, root, res):
        if not root:
            return 
        val = self.d[root]
        code = root // 10
        idx = root % 10
        level = code // 10
        left_code = (level + 1) * 10 + idx * 2 -1
        right_cpde = (level+1) * 10 + idx * 2
        if left_code not in self.d and right_code not in self.d:
            self.sum += res + val
            return 
        self.traverse(left_code, res + val)
        self.traverse(right_code, res + val)
