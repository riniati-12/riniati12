pasien = []

def tambah_pasien(nama, darurat, poli, dokter):
    nomor_antrian = len(pasien) + 1 
    status = "Menunggu"
    pasien.append({
        "nama": nama,
        "nomor_antrian": nomor_antrian,
        "darurat": darurat,
        "poli": poli,
        "dokter": dokter,
        "status": status
    })

waktu_layanan_per_pasien = 10  

while True:
    nama_pasien = input("Masukkan nama pasien darurat (atau ketik 'selesai' untuk mengakhiri): ")
    if nama_pasien.lower() == 'selesai':
        break
    poli = input("Masukkan poli (misalnya 'Umum' atau 'Kandungan'): ")
    dokter = input("Masukkan nama dokter: ")

    tambah_pasien(nama_pasien, True, poli, dokter)


antrian_darurat = [p for p in pasien if p["darurat"]]
antrian_biasa = [p for p in pasien if not p["darurat"]]
    
daftar_antrian = antrian_darurat + antrian_biasa
    
daftar_string_antrian = []
total_waktu_tunggu = 0

for i, p in enumerate(daftar_antrian):
    
    waktu_tunggu = total_waktu_tunggu
    
    total_waktu_tunggu += waktu_layanan_per_pasien


    if waktu_tunggu == 0:
        p['status'] = "Sedang Dilayani"
    else:
        p['status'] = "Menunggu"

    daftar_string_antrian.append(
        f"{p['nama']} - Nomor Antrian: {p['nomor_antrian']} - {'Darurat' if p['darurat'] else 'Biasa'} - "
        f"Waktu Tunggu: {waktu_tunggu} menit - Poli: {p['poli']} - Dokter: {p['dokter']} - Status: {p['status']}"
    )


for p in daftar_antrian:
    if p['status'] == "Sedang Dilayani":
        p['status'] = "Selesai"

print("\nDaftar Antrian Pasien:")
for antrian in daftar_string_antrian:
    print(antrian)
    
print("\nStatus Akhir Pasien:")
for p in daftar_antrian:
    print(f"{p['nama']} - Status: {p['status']}")
    
    
    
