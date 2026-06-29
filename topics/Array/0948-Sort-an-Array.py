############################################################
# Problem  : Sort an Array
# ID       : 948
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Sorting, Heap (Priority Queue), Merge Sort, Bucket Sort, Radix Sort, Counting Sort
# Runtime  : 1014
# Memory   : 25976000
# Language : Python3
# Solved   : 2026-06-29 16:54
# URL      : https://leetcode.com/problems/sort-an-array/
############################################################
class Solution:
    def merge(self,nums,mid,l,r):
        a = []
        b = []
        for i in range(l,mid+1):
            a.append(nums[i])

        for i in  range(mid+1, r+1):
            b.append(nums[i])

        i,j,k = 0,0,l

        while k <= r:
            if i == len(a):
                nums[k] = b[j]
                j += 1
                k += 1

            elif j == len(b):
                nums[k] = a[i]
                i += 1
                k += 1

            elif a[i] < b[j]:
                nums[k] = a[i]
                i += 1
                k += 1
            
            else:
                nums[k] = b[j]
                j += 1
                k += 1

                
    def mergeSort(self, nums, l, r):
        if l >= r:
            return
        mid = (l + r)//2
        self.mergeSort(nums,l,mid)
        self.mergeSort(nums,mid+1,r)
        self.merge(nums,mid,l,r)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums)-1)
        return nums
        