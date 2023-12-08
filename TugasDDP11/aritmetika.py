import math
# 1.Penjumlahan
def tambah(bil1, bil2): 
    hasil = bil1 + bil2
    print("Hasil tambah dari", bil1, "+", bil2, "=", hasil)

# 2.Pengurangan
def kurang(bil1, bil2): 
    hasil = bil1 - bil2
    print("Hasil pengurangan dari", bil1, "-", bil2, "=", hasil)

# 3.Perkalian
def kali(bil1, bil2): 
    hasil = bil1 * bil2
    print("Hasil perkalian dari", bil1, "*", bil2, "=", hasil)

# 4.Pembagian
def bagi(bil1, bil2): 
    hasil = bil1 / bil2
    print("Hasil pembagian dari", bil1, "/", bil2, "=", hasil)

# 5.Pangkat
def pangkat(bil1, bil2): 
    hasil = math.pow (bil1, bil2)
    print("Hasil pangkat dari", bil1, "^", bil2, "=", hasil)

# 6.Modulus
def modulus (bil1, bil2 ) :
    hasil = bil1 % bil2
    print ("Hasil modulus dari", bil1, "&", bil2, "=", hasil)

# 7.Akar
def akar (bil1, bil2 ) :
    bil2 = 0.5
    hasil = bil1 ** bil2
    print ("Hasil akar dari", bil1, "=", hasil)

# 8.Lagoritma
def logaritma_dasar10(bil1):
    hasil = math.log10(bil1)
    print(f"Hasil Logaritma dasar 10 dari {bil1} = {hasil}")

# 9.Akar Kompleks
def akar_kompleks(bil1):
    hasil = math.sqrt(bil1)
    print(f"Hasil akar kompleks dari {bil1} = {hasil}")

# 10.bulatan
def bulatan (bil1) :
    hasil = math.ceil(bil1)
    print ("Hasil bulatkan keatas dari", bil1, "=", hasil)