class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        self.count += 1
        self.queue.append(val)
        self.window_sum += val
        removed = self.queue.popleft() if self.count > self.size else 0
        self.window_sum -= removed
        return self.window_sum * 1.0 / min(self.count, self.size)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
