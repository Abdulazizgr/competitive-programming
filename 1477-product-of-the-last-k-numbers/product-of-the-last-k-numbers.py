class ProductOfNumbers:

    def __init__(self):
        self.zero_check = [0]
        self.prefix_pro = [1]
        

    def add(self, num: int) -> None:
        if num != 0:
            self.prefix_pro.append(self.prefix_pro[-1] *num)
            self.zero_check.append(self.zero_check[-1])
        else:
            self.prefix_pro.append(1)
            self.zero_check.append(self.zero_check[-1] + 1)

    def getProduct(self, k: int) -> int:
        if self.zero_check[-1] != self.zero_check[-(k+1)]:
            return 0
        return self.prefix_pro[-1] // self.prefix_pro[-(k+1)]

        


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)