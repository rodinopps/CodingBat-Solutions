def alarm_clock(day, vacation):
  if vacation == True:
    if day == 0 or day == 6:
      return "off"
    elif 0 < day < 6:
      return "10:00"
  elif vacation == False:
    if day == 0 or day == 6:
      return "10:00"
    elif 0 < day < 6:
      return "7:00"
      
