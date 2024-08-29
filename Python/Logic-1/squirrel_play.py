def squirrel_play(temp, is_summer):
  if is_summer == True:
    if 60 <= temp <= 100:
      return True
    else:
      return False
  else:
    if 60 <= temp <= 90:
      return True
    else:
      return False
