class DataStream:

    def __init__(self, value: int, k: int):
        self.target = value
        self.k = k
        self.count = 0
        

    def consec(self, num: int) -> bool:
        if num == self.target:
            self.count += 1
            if self.count == self.k:
                self.count -= 1
                return True
        else:
            self.count = 0
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)