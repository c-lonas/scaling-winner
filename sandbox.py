def bubble_sort(nums):
    length = len(nums)
    for i in range(length):
        for j in range(length - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        

    print("bubble_sort:", nums)


def insert_sort(nums):
    length = len(nums)
    for i in range(1, length):
        idx = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > idx:
            nums[j + 1] = nums[j]
            j -= 1
            print("current insert sort:", nums)
        nums [j + 1] = idx
    print("insert sort: ", nums) 



nums = [5, 2, 1, 8, 4, 1, 56, 7]
# bubble_sort(nums)

nums2 = [4, 1, 8, 2, 4, 7, 6]
insert_sort(nums)





            

