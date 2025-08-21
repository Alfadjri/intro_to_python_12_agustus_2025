# Example buah
# Dalam programming Konsep Dasarnya Sebutahnya CRUD
# C = Create (Membuat)
# R = Read (Membaca)
# U = Update (Merubah)
# D = Delete (Menghapus)
buah = ["Salak pondo"] #ini sebutahnya instansiasi

# Add (Create)
buah.append("Satu")
buah.append("Dua")
buah.append("Tiga")
buah.append("Empat")

# Read
print(f"Memanggil Semua list :{buah}")
# Read Spesifik nilai 
print(f"Index ke 3 : {buah[-1]}")

# Update
buah[0] = "Nol"
print(f"Memanggil Semua list :{buah}")

# Delete
del buah[0]
print(f"Memanggil Semua list :{buah}")