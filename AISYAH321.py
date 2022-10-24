import time
x=input("masukkan nama kamu: ")

print("---PROGRAM KONVERSI BILANGAN---")
print("1 -> Desimal ke biner")
print("2 -> Biner ke Desimal")
print("3 -> Exit")
a=0
while a !=3:
    a = int(input("silahkan masukkan menu: "))
    if a == 1:
        b = int(input("silahkan masukkan desimal: "))
        bineri= bin(b).replace("0b","")
        print("nilai binernya adalah {0}".format(bineri))
    elif a == 2:
        b = int(input("masukkan bilangan biner: "),2)
        print("nilai desimalnya adalah {0}".format(b))
print("terima kasih aisyah")

time.sleep(50)
	