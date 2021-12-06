def temp(c):
    if c==0:
        print("Fagypont")
    elif c<0:
        print("fagy")
    elif c>99:
        print("normal")
    else:
        print("normal")

for homerseklet in range (-20,121,20):
    print(homerseklet, "C " , end="")
    temp(homerseklet)

    print(temp(int(input("most hány foksz van tesom? ird be : "))))
    