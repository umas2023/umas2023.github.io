def find_max_product(nums):
    if len(nums) < 2:
        return None
    
    max_product = float('-inf')
    
    for i in range(len(nums)-1):
        product = nums[i] * nums[i+1]
        if product > max_product:
            max_product = product
            
    return max_product


print(find_max_product([1,2,3,4]))