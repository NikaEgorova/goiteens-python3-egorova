George_Washington = 2
Thomas_Jefferson = 2
Herbert_Hoover = 1
Barack_Obama = 2
coef = 4
for a in range(1, 3):
    if a % 2 == 1:
        print("Herbert Hoover був президентом", a * coef, "роки")
    if a % 2 == 0:
        print("George Washington був президентом", a * coef, "років",
              "\n"  "Thomas Jefferson був президентом", a * coef, "років", "\n" "Barack Obama був президентом", a * coef, "років")
