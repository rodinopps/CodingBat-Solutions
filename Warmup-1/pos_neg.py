def pos_neg(a, b, negative):
  if negative == True and a < 0 and b < 0 or negative == False and a > 0 and b < 0 or negative == False and a < 0 and b > 0:
    return True
  else:
    return False
