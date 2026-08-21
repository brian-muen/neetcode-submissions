import heapq

class MedianFinder:

    def __init__(self):
        self.l_heap = []
        self.r_heap = []
        self.n = 0
        
    def addNum(self, num: int) -> None:
        self.n += 1
        l_heap = self.l_heap
        r_heap = self.r_heap

        if self.n % 2 == 0:
            if num > r_heap[0]:
                old_min = heapq.heappop(r_heap)
                heapq.heappush(l_heap, -old_min)
                heapq.heappush(r_heap, num)
            else:
                heapq.heappush(l_heap, -num)

        if self.n % 2 != 0:
            if l_heap and num < -l_heap[0]:
                old_max = -heapq.heappop(l_heap)
                heapq.heappush(r_heap, old_max)
                heapq.heappush(l_heap, -num)
            else:
                heapq.heappush(r_heap, num)


    def findMedian(self) -> float:
        if self.n % 2 != 0:
            return self.r_heap[0]
        else:
            return (self.r_heap[0] + -self.l_heap[0]) / 2
        