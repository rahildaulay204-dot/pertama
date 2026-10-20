print("=" * 45)
print("      REGISTRASI BIODATA PENDUDUK")
print("=" * 45)

# Input biodata
nik = input("Masukkan NIK (16 angka) : ")
nama = input("Nama lengkap            : ")
tempat = input("Tempat lahir             : ")
tanggal = input("Tanggal lahir            : ")
hobi = input("H122obi            : ")
jenis_kelamin = input("Jenis kelamin             : ")
alamat = input("Alamat                   : ")
agama = input("Agama                    : ")
status = input("Status perkawinan         : ")
pekerjaan = input("Pekerjaan                : ")
kewarganegaraan = input("Kewarganegaraan           : ")

# Validasi data
if not nik.isdigit() or len(nik) != 16:
    print("\nERROR: NIK harus terdiri dari 16 angka!")
else:
    # Menampilkan profil
    print("\n")
    print("=" * 45)
    print("          PROFIL BIODATA PENDUDUK")
    print("=" * 45)
    print("NIK               :", nik)
    print("Nama Lengkap      :", nama)
    print("Tempat Lahir      :", tempat)
    print("Hobi              :", hobi)
    print("Tanggal Lahir     :", tanggal)
    print("Jenis Kelamin     :", jenis_kelamin)
    print("Alamat            :", alamat)
    print("Agama             :", agama)
    print("Status Perkawinan :", status)
    print("Pekerjaan         :", pekerjaan)
    print("Kewarganegaraan   :", kewarganegaraan)
    print("=" * 45)
    print("   REGISTRASI BERHASIL!")
    print("=" * 45)
  