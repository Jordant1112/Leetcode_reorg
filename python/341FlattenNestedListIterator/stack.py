class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for ele in nestedList:
            self.stack += self.process_element(ele)
        self.idx = 0

    def process_element(self, element):
        if element.isInteger():
            return [element.getInteger()]
        result = []
        for ele in element.getList():
            result += self.process_element(ele)
        return result

    def next(self):
        res = self.stack[self.idx]
        self.idx += 1
        return res

    def hasNext(self):
        return self.idx < len(self.stack)
