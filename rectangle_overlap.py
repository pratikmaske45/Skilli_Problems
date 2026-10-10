# Rectangle Overlap
# You are given two axis-aligned rectangles.

# The first rectangle is represented using: (r1x1, r1y1) as its bottom-left corner and (r1x2, r1y2) as its top-right corner.

# The second rectangle is represented using: (r2x1, r2y1) as its bottom-left corner and (r2x2, r2y2) as its top-right corner.

# Its top and bottom edges are parallel to the X-axis, and its left and right edges are parallel to the Y-axis.

# Return true if the two rectangles have a positive-area overlap. Otherwise, return false.

# Two rectangles that only touch at an edge or corner are not considered overlapping.

# Input Parameters r1x1, r1y1, r1x2, r1y2, r2x1, r2y1, r2x2, r2y2

# Constraints -10^9 <= r1x1, r1y1, r1x2, r1y2 <= 10^9 -10^9 <= r2x1, r2y1, r2x2, r2y2 <= 10^9

# Example1:
# Input:
# r1x1: 0, r1y1: 0, r1x2: 2, r1y2: 2, r2x1: 1, r2y1: 1, r2x2: 3, r2y2: 3 Output: true


class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0]:
            return False

        if rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False

        return True

