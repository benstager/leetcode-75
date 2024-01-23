# given list size with n integeres from 0 -> n-1, return index of target integer or return 0
def binary_search(nums:list[int], target) -> int:
    # initialize indices at endpoints
    l = 0
    r = len(nums) - 1

    # do loop while l <= r
    while l <= r:
        # set average index each time
        mid = (l+r)//2
        if nums[mid] < target: # slides pointer right one if average is less than target
            l = mid + 1
        elif nums[mid] > target: # slide pointer left one if average is greater than target
            r = mid - 1
        else:
            return mid
    
    # unsuccessful return -1
    return -1

test = [0,3,5,6,9,11,15]
target = 5
print(binary_search(test,target))