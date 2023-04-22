# Contoh format string

# Contoh format generic pada string :
nama = "Yuda Adi Saputra"
format_str = f"hello {nama}"
print(format_str)

#===========================================

# Contoh format boolean pada string :
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

#===========================================

# Contoh format angka pada string :
angka = 2003.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 14
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 1400000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2005.54321
format_str = f"desimal = {angka:.3f}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 1400000
format_str = f"jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 2003.14030
format_str = f"desimal = {angka:.3f}"
print(format_str)

# Cara menampilkan leading zero :
angka = 2005.54321
format_str = f"desimal = {angka:010.3f}"
print(format_str)

# Cara menampilkan tanda (+) atau tanda (-) :
angka_minus = -14
angka_plus = +14.0303
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# Contoh memformat persen :
persentase = 0.014
format_persen = f"persen = {persentase:.2%}"

print(format_persen)

# Contoh  operasi aritmatika di dalam placeholder :
harga = 14000
jumlah = 3

format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# Contoh format angka lain binary, octal dan hexadecimal :

angka = 140
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)

# Di buat oleh Yuda Adi Saputra
# Github : https://github.com/Yudaadisaputra