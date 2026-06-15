class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        storage_tank = 0
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                storage_tank += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                storage_tank += right_max - height[r]
            
        return storage_tank