from heapq import heapify, heappop, heappush
class SmallestInfiniteSet:

    def __init__(self):
        self.removedList = [i for i in range(1,1001)]
        heapify(self.removedList)

    def popSmallest(self) -> int:
        return heappop(self.removedList)
        

    def addBack(self, num: int) -> None:
        if num not in self.removedList:
            heappush(self.removedList,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)