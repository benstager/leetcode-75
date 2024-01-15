def two_sum(nums, target):
    ans = []

    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                ans.append((i,j))
                return ans