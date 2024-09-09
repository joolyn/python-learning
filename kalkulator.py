while True:
	angka1 = float(input("Masukkan Angka 1: "))
	angka2 = float(input("Masukkan Angka 2: "))

	if angka2 == null:
		pass

	operasi = input("Pilih Operasi (+, *, /, -): ")

	if operasi == "+":
		hasiltambah = angka1 + angka2
		print(hasiltambah)
	elif operasi == "-":
		hasiltambah = angka1 - angka2
		print(hasiltambah)
	elif operasi == "*":
		hasiltambah = angka1 * angka2
		print(hasiltambah)
	elif operasi == "/":
		hasiltambah = angka1 / angka2
		print(hasiltambah)
	else:
		print("Masukkan Angka yang tepat")