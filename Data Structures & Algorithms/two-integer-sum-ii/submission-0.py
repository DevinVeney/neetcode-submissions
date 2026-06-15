class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers) - 1
        sortednum = sorted(numbers)
        output = []
        while l < r:
            current_sum = sortednum[l] + sortednum[r]
            if current_sum == target:
                return [l + 1, r + 1]
            elif current_sum < target:
                l += 1  # Need a larger sum, move rightward
            else:
                r -= 1 # Need a smaller sum, move leftward
        return output
        print(output)

