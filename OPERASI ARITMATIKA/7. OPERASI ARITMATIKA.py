# Pengetian Operator Aritmatika
# Operator aritmatika adalah jenis operasi matematis seperti penjumlahan, pengurangan, pembagian, perkalian, sisa bagi dan juga pemangkatan.
# Operator aritmatika ini juga merupakan operator yang paling sering digunakan dalam bahasa pemrograman manapun termasuk python.

# Berikut contoh Operator Aritmatika :

a = 14
b = 3
# Berikut Variabel a dan b

# contoh operasi aritmatika pertambahan
hasil = a + b
print(a,'+',b,'=',hasil)

# contoh operasi aritmatika perngurangan
hasil = a - b
print(a,'-',b,'=',hasil)

# contoh operasi aritmatika perkalian
hasil = a * b
print(a,'*',b,'=',hasil)

# contoh operasi aritmatika pembagian
hasil = a / b
print(a,'/',b,'=',hasil)

# contoh operasi aritmatika pengkat
hasil = a ** b
print(a,'**',b,'=',hasil)

# contoh operasi aritmatika modulus
hasil = a % b
print(a,'%',b,'=',hasil)

#contoh operasi floor division
hasil = a // b
print(a,'//',b,'=',hasil)

#=================================================================

# Contoh prioritas operasi, operational precedence
'''
    1. ()
    2. exponen **
    3. perkalian dan teman-teman * / ** % //
    4. pertambahan dan pengurangan + -
'''
x = 1
y = 2
z = 3
# Berikut Variabel x, y, dan z

hasil = x ** y * (z + x) / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)

hasil = x + y * z
print(x,'+',y,'*',z,'=',hasil)
# kurung akan mengambil langkah paling pertama
hasil = (x + y) * z 
print('(',x,'+',y,') *',z,'=',hasil)

# Di buat oleh Yuda Adi Saputra
# Github : https://github.com/Yudaadisaputra