projekt_times = {
    "Projekt A": {"Erik": 25, "Lina": 30, "Tomas": 20},
    "Projekt B": {"Lina": 35, "Erik": 40},
    "Projekt C": {"Tomas": 45, "Erik": 50}
}

lina_projekt = {}

for projekt, times in projekt_times.items():
    if "Lina" in times and times["Lina"] > 30:
        lina_projekt[projekt] = times

print("Projekt där Lina har lagt ner mer än 30 timmar:", lina_projekt)