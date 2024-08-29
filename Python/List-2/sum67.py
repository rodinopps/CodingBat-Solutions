def sum67(nums):
  if not nums: 
    return 0

  total = 0
  ignore = False

  for num in nums:
    if num == 6:
      ignore = True  
    elif num == 7 and ignore:
      ignore = False 
    elif not ignore:
      total += num

  return total
