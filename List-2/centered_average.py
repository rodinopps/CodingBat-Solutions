def centered_average(nums):
  small = min(nums)
  big = max(nums)
  nums.remove(small)
  nums.remove(big)
  total = sum(nums)
  return total / len(nums)
