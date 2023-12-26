class Hewan:
    def __init__(self, nama, makanan, habitat, reproduksi):
        self.nama = nama
        self.makanan = makanan
        self.habitat = habitat
        self.reproduksi = reproduksi

    def deskripsi(self):
        return f"Nama: {self.nama}, Makanan: {self.makanan}, Habitat: {self.habitat}, Reproduksi: {self.reproduksi}"


class Badak(Hewan):
    def __init__(self, nama, makanan, habitat, reproduksi, ukuran_tanduk):
        super().__init__(nama, makanan, habitat, reproduksi)
        self.ukuran_tanduk = ukuran_tanduk

    def suara(self):
        return "Hingus!"

    def info(self):
        return f"{super().deskripsi()}, Ukuran Tanduk: {self.ukuran_tanduk}"


class Ikan(Hewan):
    def __init__(self, nama, makanan, habitat, reproduksi, tipe_air):
        super().__init__(nama, makanan, habitat, reproduksi)
        self.tipe_air = tipe_air

    def berenang(self):
        return "Ikan berenang dengan menggerakkan ekornya."

    def info(self):
        return f"{super().deskripsi()}, Tipe Air: {self.tipe_air}"


class Ular(Hewan):
    def __init__(self, nama, makanan, habitat, reproduksi, panjang):
        super().__init__(nama, makanan, habitat, reproduksi)
        self.panjang = panjang

    def merayap(self):
        return "Ular bergerak dengan merayap di tanah."

    def info(self):
        return f"{super().deskripsi()}, Panjang: {self.panjang}"


badak = Badak("Badak", "Rumput", "Padang Rumput", "Vivipar", "Besar")
print(badak.info())
print(badak.suara())

ikan = Ikan("Ikan Emas", "Serpihan", "Air Tawar", "Ovipar", "Air Tawar")
print(ikan.info())
print(ikan.berenang())

ular = Ular("Python", "Hewan Kecil", "Berbagai", "Ovipar", "Panjang")
print(ular.info())
print(ular.merayap())
