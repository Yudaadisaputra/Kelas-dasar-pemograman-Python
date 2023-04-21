# Pengertian Biner 
# Bilangan biner sendiri merupakan jenis bilangan yang hanya terdiri dari 2 jenis angka, yakni 0 dan 1.
# Jika nilai asal yang dipakai bukan bilangan biner, akan dikonversi secara otomatis menjadi bilangan biner.
# Misalnya 7 desimal = 0111 dalam bilangan biner.

a = 9
b = 5
# a dan b merupakan Type data Variabel

#============================================================

# Nilai OR
c = a | b
print('\n OR')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('----------------------------- (|)')
print('nilai :',c,' , binary :',format(c,'08b'))
# bitwise OR (|)

#============================================================

# Nilai AND
c = a & b
print('\n AND')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('----------------------------- (&)')
print('nilai :',c,' , binary :',format(c,'08b'))
# bitwise AND (&)

#============================================================

# Nilai XOR
c = a ^ b
print('\n XOR')
print('nilai :',a,' , binary :',format(a,'08b'))
print('nilai :',b,' , binary :',format(b,'08b'))
print('----------------------------- (^)')
print('nilai :',c,' , binary :',format(c,'08b'))
# bitwise XOR (^)

#============================================================

# Nilai NOT
c = ~a
print('\n NOT')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (~)')
print('nilai :',c,' , binary :',format(c,'08b'))
print('----------------------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('nilai :',e^d,' , binary :',format(e^d,'08b'))
# bitwise NOT (~)

#============================================================

# Nilai shifting

# shift KANAN (>>)
c = a >> 2
print('\n KANAN')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (>>)')
print('nilai :',c,' , binary :',format(c,'08b'))

# shift KIRI (<<)
c = a << 2
print('\n KIRI')
print('nilai :',a,' , binary :',format(a,'08b'))
print('----------------------------- (<<)')
print('nilai :',c,' , binary :',format(c,'08b'))

# Di buat oleh Yuda Adi Saputra
# Github : https://github.com/Yudaadisaputra