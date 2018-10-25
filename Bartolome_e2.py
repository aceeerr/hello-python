import sys
Sustained_Winds = sys.argv[1]



if float(Sustained_Winds) >= 220.0 :
    print(Sustained_Winds, "is equal to Super Typhoon")
elif float(Sustained_Winds) >= 118.0:
    print(Sustained_Winds, "is equal to Typhoon")
elif float(Sustained_Winds) >= 89.0:
    print(Sustained_Winds, "is equal to Severe Tropical Storm")
elif float(Sustained_Winds) >= 62.0:
    print(Sustained_Winds, "is equal to Tropical Storm")
else:
    print(Sustained_Winds, "is equal to Tropical Depression")