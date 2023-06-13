class Solution:  
    def reverse(self, A,start,end):
        while start < end:
            A[start],A[end] = A[end],A[start]
            start += 1
            end -= 1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        if l < 2:
            return
        if k > l:
            k = k % l
        self.reverse(nums, 0, l - k - 1)
        self.reverse(nums, l - k, l - 1)
        self.reverse(nums, 0, l - 1)
