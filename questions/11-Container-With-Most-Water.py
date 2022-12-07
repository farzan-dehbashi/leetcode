class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            area = min(height[l], height[r]) * (r-l)
            if area > max_area:
                max_area = area
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area
