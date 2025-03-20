class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        index = [i for i in range(len(deck))]
        index = deque(index)
        ans = [0 for i in range(len(deck))]
        idx = 0
        while index:
            num =index.popleft()
            ans[num] = deck[idx]
            idx +=1
            if index:
                index.append(index.popleft())

        return ans