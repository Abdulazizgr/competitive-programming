class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = list(range(1, n+1))
        i = 0

        while len(players) > 1:
            i = (i + k - 1) % len(players)
            players.pop(i)
        return players[0]
