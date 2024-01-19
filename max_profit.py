
def max_profit(prices: list[int])->int:
    # use two pointer approach
    left = 0 # initialize left at index 0
    right = 1 # initialize right at index 1
    max_profit = 0
    current_profit = 0

    # iterate over prices until end is reached
    while right < len(prices):
        current_profit = prices[right] - prices[left]
        #checks if the right price is greater than left prices
        if prices[left] < prices[right]:
            #checks max between max and current
            max_profit = max(max_profit, current_profit)
        # if its not greater, the left index is set to the right index
        else:
            left = right
        # slide pointer over
        right +=1
    return max_profit

test = [7,6,4,3,1]
print(max_profit(test))