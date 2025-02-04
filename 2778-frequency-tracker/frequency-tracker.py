class FrequencyTracker:
    def __init__(self):
        self.num_count = defaultdict(int)  
        self.freq_count = defaultdict(int)  

    def add(self, number: int) -> None:
        prev_count = self.num_count[number]
        
        if prev_count > 0:
            self.freq_count[prev_count] -= 1  
        
        self.num_count[number] += 1
        self.freq_count[self.num_count[number]] += 1  

    def deleteOne(self, number: int) -> None:
        if self.num_count[number] > 0:
            prev_count = self.num_count[number]
            self.freq_count[prev_count] -= 1  

            self.num_count[number] -= 1
            if self.num_count[number] > 0:
                self.freq_count[self.num_count[number]] += 1  

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq_count[frequency] > 0




# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)