def lone_sum(a, b, c):
  if a != b and b != c and a != c:
    return a + b + c
  elif a == b and a != c:
    return c
  elif a == c and a != b:
    return b
  elif b == a and b != c:
    return c
  elif b == c and b != a:
    return a
  else:
    return 0
