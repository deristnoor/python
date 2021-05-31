# soal exercise 2 session 04

# menghitung Indeks Massa Tubuh
# IMT = massa(kg) / tinggi(meter)^2
# a. IMT < 18.5 artinya berat badan kurang,
# b. 18.5 - 24.9 artinya berat badan ideal,
# c. 25.0 - 29.9 artinya berat badan berlebih,
# d. 30.0 - 39.9 artinya berat badan sangat berlebih,
# e. IMT > 39.9 artinya obesitas
 
massa = int(input("Masukkan berat badan dalam kilogram: "))
tinggi = int(input("Masukkan tinggi dalam cm: ")) 

imt = massa / (tinggi / 100) ** 2

if imt > 0 and imt <= 18.5:
    print("IMT anda adalah " + str(imt))
    print("BERAT BADAN KURANG")
elif imt > 18.5 and imt <= 24.9:
    print("IMT anda adalah " + str(imt))
    print("BERAT BADAN IDEAL")
elif imt > 25.0 and imt <= 29.9:
    print("IMT anda adalah " + str(imt))
    print("BERAT BADAN BERLEBIH")
elif imt > 30.0 and imt <=39.9:
    print("IMT anda adalah " + str(imt))
    print("BERAT BADAN SANGAT BERLEBIH")
elif imt > 39.9:
    print("IMT anda adalah " + str(imt))
    print("OBESITAS")
else:
    print("Mohon masukkan berat badan dan tinggi dengan benar")