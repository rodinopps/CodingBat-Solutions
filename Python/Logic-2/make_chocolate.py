def make_chocolate(small, big, goal):
  max = min(goal // 5, big)
  remainingweight = goal - (max * 5)
    
  if remainingweight <= small:
      return remainingweight
  else:
      return -1
