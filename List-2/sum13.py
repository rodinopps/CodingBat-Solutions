def sum13(nums):
  total = 0
  skip = False
  for i in nums:
    if i == 13:
      skip = True
    elif skip:
      skip = False
    else:
      total += i
      
  return total
      
