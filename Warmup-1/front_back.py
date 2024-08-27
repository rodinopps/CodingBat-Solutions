def front_back(str):
  if len(str) <= 1:
    return str
  start = str[0]
  end = str[-1]
  return end + str[1:-1] + start
