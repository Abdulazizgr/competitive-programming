class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        matches = 0
        player_idx = 0
        trainer_idx = 0

        while player_idx < len(players) and trainer_idx < len(trainers):
            if players[player_idx] <= trainers[trainer_idx]:
                matches += 1
                player_idx += 1
                trainer_idx += 1
            else:
                trainer_idx += 1

        return matches
