teks = input("Masukkan teks anda: ")

vokala = teks.count('a')
vokali = teks.count('i')
vokalu = teks.count('u')
vokale = teks.count('e')
vokalo = teks.count('o')

vokalA = teks.count('A')
vokalI = teks.count('I')
vokalU = teks.count('U')
vokalE = teks.count('E')
vokalO = teks.count('O')

hitungVokal = vokala + vokali + vokalu + vokale + vokalo + vokalA + vokalI + vokalU + vokalE + vokalO

print(hitungVokal)


# Versi Singkat
# teks = input("Masukkan teks anda: ")

# # Menghitung jumlah huruf vokal menggunakan list comprehension
# hitungVokal = sum(1 for char in teks if char.lower() in 'aeiou')

# print(hitungVokal)