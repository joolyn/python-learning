import random

# tebak = int(input("Tebak Angka: "))
# number = [i for i in range(1,101)]
# random_number = random.choice(number)
# if random_number == tebak :
# 	print("Tebakan Anda Benar")
# elif random_number > tebak:
# 	print("Tebakan Anda Terlalu Kecil")
# elif random_number < tebak:
# 	print("Tebakan Anda Terlalu Besar")

# print(random_number)

# Komputer memilih angka acak antara 1 dan 100
random_number = random.randint(1, 100)

# Memulai loop tebakan
while True:
    tebak = int(input("Tebak Angka (1-100): "))

    if tebak == random_number:
        print("Selamat! Tebakan Anda Benar.")
        break  # Keluar dari loop jika tebakannya benar
    elif tebak < random_number:
        print("Tebakan Anda Terlalu Kecil.")
    else:
        print("Tebakan Anda Terlalu Besar.")
