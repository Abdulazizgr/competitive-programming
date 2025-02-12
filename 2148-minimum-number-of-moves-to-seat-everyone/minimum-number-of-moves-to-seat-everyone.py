class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        min_ope = 0
        for val in range(len(seats)):
            min_ope += abs(seats[val]- students[val])
        return min_ope
        