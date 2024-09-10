class Solution:
    def pathSum(nums: List[int]) -> int:
        self.sum = 0
        self.tree = {}
        for code in nums:
            val = code % 10
            path = code // 10
            self.tree[path] = val
        path = nums[0] // 10
        self.traverse(path, 0)
        return self.sum

    def traverse(self, path, res):
        if path not in self.tree:
            return
        val = self.tree[path]
        position = path % 10
        level = path // 10
        left_path = (level+1)*10 + position * 2 -1
        right_path = (level+1) * 10 + position * 2
        if left_path not in self.tree and right_path not in self.tree:
            res += val + res
            return
        self.traverse(left_path, res + val)
        self.traverse(right_path, res + val)
