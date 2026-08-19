class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        reserved = {}

        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                reserved[row] = reserved.get(row, 0) | (1 << seat)

        result = (n - len(reserved)) * 2

        for mask in reserved.values():
            left = all(not (mask & (1 << seat)) for seat in range(2, 6))
            middle = all(not (mask & (1 << seat)) for seat in range(4, 8))
            right = all(not (mask & (1 << seat)) for seat in range(6, 10))

            if left and right:
                result += 2
            elif left or middle or right:
                result += 1

        return result