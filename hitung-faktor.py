angka = int(input("Masukkan Angka: "))
faktor = []
for i in range(1, 1+angka):
	if ((angka % i) == 0):
		faktor.append(i)

print(f"Faktor dari angka {angka} adalah: ", (faktor))
# Mencoba membedakan branch
