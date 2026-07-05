def cel_to_fahren(c):   return (c*9/5)+32
def cel_to_kel(c):  return c+273.15
def fahren_to_cel(f):   return (f-32)*5/9
def fahren_to_kel(f):   return fahren_to_cel(f) + 273.15
def kel_to_cel(k):  return k-273.15
def kel_to_fahren(k): return cel_to_fahren(kel_to_cel(k))
def inch_to_cm(i):  return i*2.54
def cm_to_inch(cm):  return cm/2.54
def lb_to_gm(l):    return l*453.59
def gm_to_lb(gm):   return gm/453.59

# clean dictionary lookup 

CONVERSIONS = {
    ("Temperature","Celsius","Fahrenheit") : cel_to_fahren,
    ("Temperature","Celsius","Kelvin") : cel_to_kel,
    ("Temperature","Fahrenheit", "Celsius") : fahren_to_cel,
    ("Temperature","Fahrenheit","Kelvin") : fahren_to_kel,
    ("Temperature","Kelvin","Fahrenheit") : kel_to_fahren,
    ("Temperature","Kelvin","Celsius") : kel_to_cel,
    ("Length", "Inch", "Centimeter") : inch_to_cm,
    ("Length", "Centimeter","Inch") : cm_to_inch,
    ("Weight", "Gram", "Pound") : gm_to_lb,
    ("Weight", "Pounds", "Grams"): lb_to_gm
}

def convert(catagory, from_unit, to_unit, value):
    func = CONVERSIONS.get((catagory,from_unit,to_unit))
    return func(value) if func else None