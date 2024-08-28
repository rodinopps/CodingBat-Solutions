def max_end3(nums):
  list = []
  if nums[0] > nums[-1]:
    for i in nums:
      list.append(nums[0])
  elif nums[0] < nums[-1]:
    for i in nums:
      list.append(nums[-1])
  elif nums[0] == nums[-1]:
    for i in nums:
      list.append(nums[0])
  return list
