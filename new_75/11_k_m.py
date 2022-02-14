class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        right = len(height)-1
        left = 0
        while left<right:
            maxArea = max(maxArea, (right-left)*min(height[right],height[left]))
            if height[right]<height[left]:
                right -= 1
            else:
                left += 1
        return maxArea
