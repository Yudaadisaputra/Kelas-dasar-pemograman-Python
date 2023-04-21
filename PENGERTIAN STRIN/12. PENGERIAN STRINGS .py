# Pengertian String
# String dalam bahasa pemrograman Python disebut sebagai kumpulan karakter yang dikelilingi oleh tanda kutip tunggal,
# tanda kutip ganda bahkan tanda kutip tiga.
# Komputer tidak memahami karakter. Secara internal, tipe string ini menyimpan karakter yang dimanipulasi sebagai kombinasi dari 0 dan 1.

data = "ini adalah string"
print(data)
print(type(data))
# data merupaka variable
# tanda baca ("") tersebut adalah String
# Print merupakan Fungsi


# cara membuat string menggunakan tanda baca ('')

'''
    1. dengan menggunakan single quote '...'
    2. dengan menggunakan double quote "..."
'''

#Contoh String menggunakan tanda baca ('')

data = 'Menggunakan single quote'
print(data)

data = "Menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

#===========================================================

# Cara membuat string menggunakan tanda baca (\)

# membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day, isn\'t it?')

# menggunakan backlash atau double (\\)
print("C:\\user\\Ucup")

# menggunakan tab atau (\t)
print("ucup\t\t\totong, semakin jauhan")

# menggunakan backspace (\b)
print("ucup \botong, jadi deketan")

# newline
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp 
print("baris pertama.\r\nbaris kedua.") # CRLF -> line feed carriage return -> dipakai oleh windows

#===========================================================

# String literal atau raw

# hati-hati
print('C:\new folder') # akan salah pathnya

# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Yuda Adi Saputra
Status : Mahasiswa
""")

# multiline literal string dan RAW
print(r"""
Nama : Yuda Adi Saputra
Status : Mahasiswa
""")

# Di buat oleh Yuda Adi Saputra
# Github : https://github.com/Yudaadisaputra