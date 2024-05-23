"""
88. Merge Sorted Array
Easy
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        del nums1[m:] ## 1. nums1 리스트를 슬라이싱으로 m개까지 자른다.
        del nums2[n:] ## 2. nums2 리스트를 슬라이싱으로 n개까지 자른다.
        nums1 += nums2 ## 3. num1 리스트에 nums2 리스트를 더하여 합친다.
        nums1.sort() ## 4. 합쳐진 nums1 리스트를 정렬한다.
