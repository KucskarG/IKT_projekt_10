while True:
    val=input("Melyik nap van?")
    try:
        if val== "hétfő":
            print("1.nap hétköznap")
            break
        if val== "kedd":
            print("2.nap hétköznap")
            break
        if val== "hétfő":
            print("3.nap hétköznap")
            break
        if val== "hétfő":
            print("4.nap hétköznap")
            break
        if val== "hétfő":
            print("5.nap hétköznap")
            break
        if val== "hétfő":
            print("6.nap hétvége")
            break
        if val== "hétfő":
            print("7.nap hétvége")
            break
        else:
            print("Nem jól írod ", end=" ")
    except Exception:
        print("error")
