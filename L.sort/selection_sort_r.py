def selection_sort (nums):

    for i in range(len(nums)-1):
        min_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j

        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp


lst = [5, 9, 12, 0, -15, 18]
selection_sort(lst)

print(lst)
