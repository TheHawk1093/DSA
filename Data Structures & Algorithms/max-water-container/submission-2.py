class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left, right = 0, len(heights) - 1
        area = min(heights[left], heights[right]) * (right - left)
        if area > max_area:
            max_area = area
        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -=1
            area = min(heights[left], heights[right]) * (right - left)
            if area > max_area:
                max_area = area
        
        return max_area