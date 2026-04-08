class MinStack:

    def __init__(self):
        self.my_list = []
        self.min_num = float('inf')

    def push(self, val: int) -> None:
        if val < self.min_num:
            self.min_num = val
        self.my_list.append([val, self.min_num])

    def pop(self) -> None:
        poped = self.my_list.pop()
        if self.my_list:
            self.min_num = self.my_list[-1][1]
        else:
            self.min_num = float('inf')

    def top(self) -> int:
        return self.my_list[-1][0]

    def getMin(self) -> int:
        return self.min_num
