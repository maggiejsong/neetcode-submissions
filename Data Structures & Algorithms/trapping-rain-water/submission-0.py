# Input: height = [2, 1]
# Output: 1

# Input: height = [0, 6, 0, 0, 0, 1]
# Output: 3
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        heightL = height[left]
        heightR = height[right]
        total = 0

        while left < right:
            if heightL < heightR:
                left += 1
                heightL = max(heightL, height[left])
                total += heightL - height[left]
            
            else:
                right -= 1
                heightR = max(heightR, height[right])
                total += heightR - height[right]

        return total

        