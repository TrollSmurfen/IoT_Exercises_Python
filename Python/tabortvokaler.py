def ta_bort_vokaler(text):
    vokaler = "aeiouåäöAEIOUÅÄÖ"  # Lista på vokaler både små och stora
    return ''.join([char for char in text if char not in vokaler])

text = "Hej världen"
print(ta_bort_vokaler(text)) 