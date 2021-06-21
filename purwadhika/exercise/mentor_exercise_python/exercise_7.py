# 7
# Buatlah sebuah perhitungan untuk mengkonversi suhu Fahrenheit ke dalam bentuk Celsius. 
# Kemudian, jika hasil konversinya diantara 36.5 – 37.2 derajat maka tampilkan pesan suhu badan normal; 
# jika di bawah suhu tersebut, tampilkan hipotermia; dan jika di atas tampilkan hipertermia.

def f_to_c(num):
    return round(((num - 32) * 5/9),1)
    

measure = int(input("masukkan suhu badan dalam fahrenheit: "))

degree_celcius = f_to_c(measure)

if degree_celcius < 36.5:
    print("Suhu badan ada {} derajat celcius,".format(degree_celcius), "anda mengalami hipotermia")

if degree_celcius >= 36.5 and degree_celcius <= 37.2:
    print("Suhu badan ada {} derajat celcius,".format(degree_celcius), "suhu badan normal")

if degree_celcius > 37.2:
    print("Suhu badan ada {} derajat celcius,".format(degree_celcius), "anda mengalami hipertermia")