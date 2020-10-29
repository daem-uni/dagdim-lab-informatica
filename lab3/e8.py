unit1 = input("Inserire unità inizio (Tra ml, l, g, kg, mm, cm, m, km): ")
unit2 = input("Inserire unità fine (Tra fl. oz, gal, oz, lb, in, ft, mi): ")

amount = float(input("Inserire quantità: "))

if len(unit1) > 1:
    if unit1.startswith("m"):
        amount /= 1000
    elif unit1.startswith("k"):
        amount *= 1000
    elif unit1.startswith("c"):
        amount /= 100

res = -1

if unit1.endswith("l"): # Volume
    if unit2 == "fl. oz":
        res = 33.814 * amount
    elif unit2 == "gal":
        res = 0.264172 * amount
elif unit1.endswith("g"): # Mass
    if unit2 == "oz":
        res = 0.35274 * amount
    elif unit2 == "lb":
        res = 0.00220462 * amount
elif unit1.endswith("m"): # Distance
    if unit2 == "in":
        res = 39.3701 * amount
    if unit2 == "ft":
        res = 3.28084 * amount
    if unit2 == "mi":
        res = 0.000621371 * amount

if res > 0:
    print(res, unit2)
else:
    print("Conversione Invalida")