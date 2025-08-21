# void function yang tidak memiliki hasil kegitan
def format_cetak(nama , pekerjaan , gaji):
    print("==================")
    print(f"Nama : {nama}")
    print(f"Pekerjaan : {pekerjaan}")
    print(f"Gaji : Rp.{gaji}")
    print("==================")

# non void
# function di mana function nya menghasilkan nilai tertentu
def check_ganjil(nilai):
    kalkulasi = nilai % 2
    if(kalkulasi == 0):
        return "Genap"
    return "Ganjil" # ini di sebutnya hasil yang di tandai dengan return dan hasil yang di inginkan

# contoh non void
kalkulasi = check_ganjil(99)
print(f"Apakah Ganji ? {kalkulasi}")


profile= [
    {
        "nama" : "toni",
        "pekerjaan" : "Programming",
        "gaji" : 7000000
    },
    {
        "nama" : "siska",
        "pekerjaan" : "Programming",
        "gaji" : 7000000
    },
    {
        "nama" : "albert",
        "pekerjaan" : "Programming",
        "gaji" : 7000000
    },
    {
        "nama" : "toni",
        "pekerjaan" : "Programming",
        "gaji" : 7000000
    },
]

format_cetak(profile[0]['nama'],profile[0]['pekerjaan'],profile[0]['gaji'])
format_cetak(profile[1]['nama'],profile[1]['pekerjaan'],profile[1]['gaji'])
format_cetak(profile[2]['nama'],profile[2]['pekerjaan'],profile[2]['gaji'])

# print("==================")
# print(f"Nama : {profile[1]['nama']}")
# print(f"Pekerjaan : {profile[1]['pekerjaan']}")
# print(f"Gaji : Rp.{profile[1]['gaji']}")
# print("==================")
# print("==================")
# print(f"Nama : {profile[2]['nama']}")
# print(f"Pekerjaan : {profile[2]['pekerjaan']}")
# print(f"Gaji : Rp.{profile[2]['gaji']}")
# print("==================")