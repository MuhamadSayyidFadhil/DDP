from gempa import Gempa

gempa_banten = Gempa("Banten", 1.2)
gempa_palu = Gempa("Palu", 6.1)
gempa_cianjur = Gempa("Cianjur", 5.6)
gempa_jayapura = Gempa("Jayapura", 3.3)
gempa_garut = Gempa("Garut", 4.0)

print("Gempa di", gempa_banten.lokasi)
gempa_banten.dampak()

print("\nGempa di", gempa_palu.lokasi)
gempa_palu.dampak()

print("\nGempa di", gempa_cianjur.lokasi)
gempa_cianjur.dampak()

print("\nGempa di", gempa_jayapura.lokasi)
gempa_jayapura.dampak()

print("\nGempa di", gempa_garut.lokasi)
gempa_garut.dampak()
