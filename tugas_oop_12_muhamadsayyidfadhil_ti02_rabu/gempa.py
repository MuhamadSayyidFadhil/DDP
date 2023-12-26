class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print("Dampak gempa: Tidak berasa.")
        elif 2 <= self.skala < 4:
            print("Dampak gempa: Bangunan retak-retak.")
        elif 4 <= self.skala < 6:
            print("Dampak gempa: Bangunan roboh.")
        elif self.skala >= 6:
            print("Dampak gempa: Bangunan roboh dan berpotensi tsunami.")


lokasi_gempa = "Pesisir Barat"
skala_gempa = 5.8

gempa_terkini = Gempa(lokasi_gempa, skala_gempa)
gempa_terkini.dampak()
