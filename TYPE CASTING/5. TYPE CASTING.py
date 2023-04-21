# Pengertian Type Casting :
# Type casting atau pengubahan suatu tipe data ke tipe lainnya biasa dilakukan dalam suatu bahasa pemrograman manakala, data yang diinginkan terbentuk dari tipe data lain.
# Misal ketika kamu menginginkan suatu bilangan float dari formdata yang dikirimkan client malah diterima dalam bentuk string.
# Tentu saja hal ini akan mengakibatkan masalah bila tidak melakukan type casting terlebih dahulu sebelum diproses ke suatu kode selanjutnya.

# Berikut contoh type casting :

# Contoh Type data Integer
print("INTEGER")
data_int = 9;
print("data = ", data_int, ",type =",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
# akan false apabila nilai integer tersebut adalah angka 0
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

#====================================================

# Contoh Type data Floating
print("FLOAT")
data_float = 0;
print("data = ", data_float, ",type =",type(data_float))

data_int = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float)
# akan dibulatkan ke bawah jika Variabel Float
# akan false apabila nilai Floating tersebut adalah angka 0
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_bool, ",type =",type(data_bool))

#====================================================

# Contoh Type data Boolean
print("BOOLEAN")
data_bool = False;
print("data = ", data_bool, ",type =",type(data_bool))

data_int = int(data_bool)
data_str   = str(data_bool)
data_float  = float(data_bool)
# akan dibulatkan ke bawah jika Variabel Boolean
# akan false apabila nilai Boolean tersebut adalah angka 0
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_str, ",type =",type(data_str))
print("data = ", data_float, ",type =",type(data_float))

#====================================================

# Contoh Type data String
print("STRING")
data_str = "10";
print("data = ", data_str, ",type =",type(data_str))

data_int    = int(data_str)
data_float  = float(data_str)
data_bool   = bool(data_str)
# jika data string bertemu variabel Intergal maka string tersebut harus menggunakan angka
# jika data string bertemu Floating Intergal maka string tersebut harus menggunakan angka
# false jika string kosong
print("data = ", data_int, ",type =",type(data_int))
print("data = ", data_float, ",type =",type(data_float))
print("data = ", data_bool, ",type =",type(data_bool))

# Di buat oleh Yuda Adi Saputra
# Github : https://github.com/Yudaadisaputra