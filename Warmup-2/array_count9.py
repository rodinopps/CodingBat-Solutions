def array_count9(nums):
  score = 0
  for i in nums:
    if i == 9:
      score += 1
  return score
      
