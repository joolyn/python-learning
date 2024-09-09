print("Test Palindrom")
teks = input("Masukkan Kata: ")
teks_convert = teks.lower()
balik_teks = teks_convert[::-1]
final_teks = balik_teks.lower()
if teks_convert == final_teks:
	print("Teks Terdeteksi Palindrom")
else:
	print("Teks Bukan Palindrom")