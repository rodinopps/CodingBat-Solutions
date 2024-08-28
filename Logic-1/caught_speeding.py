def caught_speeding(speed, is_birthday):
  if is_birthday == True:
    if speed <= 65:
      return 0
    elif 66 <= speed <= 85:
      return 1
    elif speed >= 86:
      return 2
  elif is_birthday == False:
    if speed <= 60:
      return 0
    elif 61 <= speed <= 80:
      return 1
    elif speed >= 81:
      return 2
