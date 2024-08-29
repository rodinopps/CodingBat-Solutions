def end_other(a, b):
  alow = a.lower()
  blow = b.lower()
  return alow.endswith(blow) or blow.endswith(alow)
