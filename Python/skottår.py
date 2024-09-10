def är_skottår(år):
    if (år % 4 == 0 and år % 100 != 0) or (år % 400 == 0):
        return True
    else:
        return False

år = int(input("Mata in ett årtal: "))
if är_skottår(år):
    print(f"{år} är ett skottår.")
else:
    print(f"{år} är inte ett skottår.")