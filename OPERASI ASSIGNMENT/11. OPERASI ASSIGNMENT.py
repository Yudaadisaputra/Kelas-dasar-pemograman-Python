# Pengertian Operasi assignment
# Operator assignment adalah operator untuk memasukkan suatu nilai ke dalam variabel.
# Operator ini sebenarnya sudah sering kita pakai sepanjang tutorial bahasa Python di Duniailkom.
# Dalam bahasa Python, operator assignment menggunakan tanda sama dengan (=).

# Contoh Operasi assignment

a = 5 # adalah assignment
print("nilai a =",a)

a += 1
print("nilai a += 1, nilai a menjadi",a)
# artinya adalah a = a + 1

a -= 2 
print("nilai a -= 2, nilai a menjadi",a)
# artinya adalah a = a - 2

a *= 5 
print("nilai a *= 5, nilai a menjadi",a)
# artinya adalah a = a * 5

a /= 2
print("nilai a /= 2, nilai a menjadi",a)
# artinya adalah a = a / 2

b = 10
print("\nnilai b =",b)

#========================================================

# modulus dan floor division
b %= 3
print("nilai b %= 3, nilai b menjadi",b)

b = 10
print("\nnilai b =",b)

b //= 3
print("nilai b //= 3, nilai b menjadi",b)

#========================================================

# pangkat atau eksponen
a = 5
print("\nnilai a =",a)
a **= 3
print("nilai a **= 3, nilai a menjadi",a)

#========================================================

# Contoh Operasi Bitwes menggunakan Operasi assignment

# OR
c = True
print("\nnilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)
c = False
print("nilai c =",c)
c |= False
print("nilai c |= False, nilai c menjadi",c)

# AND
c = True
print("\nnilai c =",c)
c &= False
print("nilai c &= False, nilai c menjadi",c)
c = True
print("nilai c =",c)
c &= True
print("nilai c &= True, nilai c menjadi",c)

# XOR
c = True
print("\nnilai c =",c)
c ^= False
print("nilai c ^= False, nilai c menjadi",c)
c = True
print("nilai c =",c)
c ^= True
print("nilai c ^= True, nilai c menjadi",c)

# geser geser
d = 0b0100
print("\nnilai d =",format(d,'04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi",format(d,'04b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi",format(d,'04b'))

# Di buat oleh Yuda Adi Saputra
# Github : https://github.com/Yudaadisaputra