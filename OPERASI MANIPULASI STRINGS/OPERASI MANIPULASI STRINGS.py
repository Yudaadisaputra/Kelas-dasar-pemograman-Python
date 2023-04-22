# Fungsi manipulasi string pada bahasa pemrograman Python dipakai untuk membelah string yang lebih besar
# menjadi bagian-bagian string yang lebih kecil dan biasanya disebut sebagai fungsi split().
# Fungsi split() akan mengubah string menjadi list.


# contoh operator dalam bentuk methods

salam = "HALO NGAB"
print("normal " + salam)
salam = salam.upper()
print("upper " + salam)
# merubah case pada string
# merubah semua ke upper case


alay = "SAYA GANTENG"
print("normal " + alay)
alay = alay.lower()
print("lower " + alay)
# merubah semua ke lower case

#===============================================

# contoh dalam bentuk isupper()
salam = "SIST"
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))
salam = salam.lower()
apakah_upper = salam.isupper()
print(salam + " is upper? " + str(apakah_upper))

# islower() untuk pengecekan apakah lower case semua
# isalpha() untuk mengecek apakah huruf semua
# isalnum() apakah huruf dan angka
# isdecimal() apakah numeric
# isspace() apakah isinya spasi, tab dan enter (newline \n)
# istitle() huruf pertama setiap kata upper case

judul = "It Is Okay To Not Be Orkay"
cek_judul = judul.istitle()
print(judul + " is title? " + str(cek_judul))

#===============================================

cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start " + str(cek_start))
cek_end = "Sangjangnim Oppak".endswith("Oppak")
print("end " + str(cek_end))
# startwith() dan endwith() agar terlihat keren

#===============================================

pisah = ['aku','sayang','kamu']
gabungan = ' ehm '.join(pisah)
print(pisah)
print(gabungan)

gabungan = "Tapi kamu sayang sama dia"
pisah = gabungan.split()
print(gabungan)
print(pisah)

gabungan = "Yah NT Lagi :)"
pisah = gabungan.split("ehm")
print(gabungan)
print(pisah)
# join() dan split() buat orang malas ketik

#===============================================

# alokasi karakter

print("'kiri      '")

kanan = "kanan".rjust(20)
print("'" + kanan + "'")
# rata kanan dengan 20 karakter

kiri = "kiri".ljust(20)
print("'" + kiri + "'")
# rata kiri dengan 20 karakter

tengah ="tengah".center(20)
print("'" + tengah + "'")
# rata tengah dengan 20 karakter

tengah ="tengah".center(20,'-')
print("'" + tengah + "'")
# rata tengah dengan 20 karakter

#===============================================

# kebalikan dari alokasi karakter
kanan = kanan.strip()
print("'" + kanan + "'")
tengah = tengah.strip('-')
print("'" + tengah + "'")

# Di buat oleh Yuda Adi Saputra
# Github : https://github.com/Yudaadisaputra