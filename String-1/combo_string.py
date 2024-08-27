def combo_string(a, b):
  alen = len(a)
  blen = len(b)
  if alen > blen:
    return b + a + b
  else:
    return a + b + a
