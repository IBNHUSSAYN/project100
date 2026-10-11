def add_number(a,b):
  if not isinstance(a,(int,float)) or isinstance(a,bool): 
    raise ValueError("Inputs must be a number")
  return a+b
