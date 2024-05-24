
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [0,1,2,2,3,0,4,2]
print(nums[-1])
val = 2

print(remove_element(nums, val))


def insert_at_i(i, arr, n):
    if i < len(arr):
        arr[i] = n
        return arr
    
print(insert_at_i(3, nums, 1010))