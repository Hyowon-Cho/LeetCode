"""
42. Trapping Rain Water
Hard
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        maxleft, maxright = height[0], height[len(height)-1]
        volume = 0
        while left < right:
            maxleft = max(maxleft, height[left])
            maxright = max(maxright, height[right])

            if maxleft <= maxright:
                volume += maxleft - height[left]
                left += 1
            else:
                volume += maxright - height[right]
                right -= 1
        return volume 
