def rakna_vokaler(text):
    vokaler = "aeiouåäöAEIOUÅÄÖ"  # Lista på vokaler både små och stora
    return sum(1 for char in text if char in vokaler)

text = "Hej världen"
print(rakna_vokaler(text))