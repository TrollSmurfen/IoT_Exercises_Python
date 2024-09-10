projekt_tider = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}

max_arbetstid = 0
projekt_med_max_arbetstid = ""

for projekt, arbetstider in projekt_tider.items():
    if "Erik" in arbetstider and arbetstider["Erik"] > max_arbetstid:
        max_arbetstid = arbetstider["Erik"]
        projekt_med_max_arbetstid = projekt

print(f"Erik har lagt ner mest tid på {projekt_med_max_arbetstid} med {max_arbetstid} timmar.")