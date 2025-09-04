#data siswa
# inisialisaisi
profile = {
    # key : value
    "kelas" : 12,
    "juruan" : ["IPA", "IPS"],
    "nama_ketua_kelas" : "Tono"
}

# Read
print(f"Seluruh  Data : {profile}")
#Read spesifik
print(f"Kelas : {profile['kelas']}")
print(f"Jurusan : {profile['juruan'][1]}")

# update
profile["nama_ketua_kelas"] = "Toni"
print(f"Seluruh  Data : {profile}")

del profile["nama_ketua_kelas"]
print(f"Seluruh  Data : {profile}")


print("Halaman maestro")
print("Halaman maestro 2")