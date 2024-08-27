def not_string(str):
  word = str.split()
  if "not" not in word[0]:
    return "not " + str
  else:
    return str
