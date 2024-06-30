def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = [0] * len(nums1)
        ind1 = 0
        ind2 = 0

        while ind1 < len(nums1) and ind2 < len(nums2):
            if nums1[ind1] <= nums2[ind2]:
                res[ind1] = nums1[ind1]
                ind1 += 1
            else:
                res[ind1] = nums2[ind2]
                ind2 += 1
        
        for i in range(len(nums1)):
            nums1[i] = res[i]
        print(nums1)
        
merge(merge, [1,2,3,0,0,0], 3, [2,5,6], 3)