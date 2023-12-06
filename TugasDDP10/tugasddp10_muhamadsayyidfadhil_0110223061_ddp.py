# 1. Buat fungsi untuk menampilkan nama2 siswa yang lulus 
# saja dari hasil_akhir di slide sebelumnya (nilai > 65)
# hasil_akhir = [
# {'nama':'Reza', 'nilai':70},
# {'nama':'Ciut', 'nilai':63},
# {'nama':'Dian', 'nilai':80},
# {'nama':'Badu', 'nilai':40}
# ]
# lulus_saja(hasil_akhir) hasilnya:[‘Reza’, ‘Dian’]

# 2. Buat fungsi untuk membuat list baru berisi urutan terbalik dari buah2an 
# menggunakan for dan materi yang sudah diajarkan. (tidak boleh pakai 
# fungsi dari python).
# balikan(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']) hasilnya :['jambu', 
# 'durian', 'pisang', 'mangga', 'pepaya']

# 3. Buat fungsi untuk membuat list baru berisi isi list buah2an tetapi 
# terduplikasi.
# duplikasi(['pepaya', 'mangga', 'pisang', 'durian', 'jambu']) Hasilnya: 
# ['pepaya', 'pepaya', 'mangga', 'mangga', 'pisang', 'pisang', 'durian', 
# 'durian', 'jambu', 'jambu']

# 4. Buat fungsi untuk membuat string baru berisi hanya konsonan dari string
# fungsi(“Nurul Fikri”) Hasilnya: "NrlFkr"


# 1.
hasil_akhir = [
    {'nama': 'Reza', 'nilai': 70},
    {'nama': 'Ciut', 'nilai': 63},
    {'nama': 'Dian', 'nilai': 80},
    {'nama': 'Badu', 'nilai': 40}
]

hasil_lulus = [siswa['nama'] for siswa in hasil_akhir if siswa['nilai'] > 65]

print("Hasil Siswa Lulus:", hasil_lulus)

# 2.
buah_input = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

buah_terbalik = []
for a in range(len(buah_input) - 1, -1, -1):
    buah_terbalik.append(buah_input[a])

print("Hasil Yang Dibalik:", buah_terbalik)

# 3.
buah_input = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']

buah_duplikasi = []
for buah in buah_input:
    buah_duplikasi.append(buah)
    buah_duplikasi.append(buah)

print("Hasil Duplikasi:", buah_duplikasi)

# 4.
input_string = "Nurul Fikri"
consonants = 'rlkrNF'

result_string = ''.join(char for char in input_string if char in consonants)

print(f'Input: "{input_string}"')
print(f'Hasil: "{result_string}"')