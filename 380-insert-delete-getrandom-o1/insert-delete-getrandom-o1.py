class RandomizedSet:

    def __init__(self):
        self.num_dict = {}
        self.num_list = []

    def insert(self, val: int) -> bool:
        res = val not in self.num_dict
        if res:
            self.num_dict[val] = len(self.num_list)
            self.num_list.append(val)
        return res
    def remove(self, val: int) -> bool:
        res = val in self.num_dict
        if res:
            idx = self.num_dict[val]
            lastval = self.num_list[-1]
            self.num_list[idx] = lastval
            self.num_list.pop()
            self.num_dict[lastval] = idx
            del self.num_dict[val]
        return res
        

    def getRandom(self) -> int:
        return random.choice(self.num_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()