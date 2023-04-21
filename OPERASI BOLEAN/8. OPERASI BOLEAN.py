# Pengertian Boolean 
# Boolean adalah tipe data Python yang hanya bisa diisi oleh dua nilai, yaitu True dan False.
# Untuk menulis isian boolean, ada dua aturan yang harus dipatuhi.
# Yaitu, pakai kapital untuk huruf pertama dan tanpa tanda petik sama sekali.

# Berikut contoh Boolean:

# NOT
print('NOT')
a = False
c = not a
print('data a =',a)
print('-------------- NOT')
print('data c =',c)

#===================================================

# OR
print('====OR====')
a = False
b = False
c = a or b
print(a,'OR',b,'=',c)
a = False
b = True
c = a or b
print(a,'OR',b,' =',c)
a = True
b = False
c = a or b
print(a,' OR',b,'=',c)
a = True
b = True
c = a or b
print(a,' OR',b,' =',c)
# jika salah satu buah nilai true, maka hasilnya juga akn bernilai true

#===================================================

# AND
print('====AND====')
a = False
b = False
c = a and b
print(a,'AND',b,'=',c)
a = False
b = True
c = a and b
print(a,'AND',b,' =',c)
a = True
b = False
c = a and b
print(a,' AND',b,'=',c)
a = True
b = True
c = a and b
print(a,' AND',b,' =',c)
# jika dua buah nilai true, maka hasilnya juga akn bernilai true

#===================================================

# XOR
print('====XOR====')
a = False
b = False
c = a ^ b
print(a,'XOR',b,'=',c)
a = False
b = True
c = a ^ b
print(a,'XOR',b,' =',c)
a = True
b = False
c = a ^ b
print(a,' XOR',b,'=',c)
a = True
b = True
c = a ^ b
print(a,' XOR',b,' =',c)
# jika nilai true maka salah satu nilai true, sisanya nilai false

# Di buat oleh Yuda Adi Saputra
# Github : https://github.com/Yudaadisaputra