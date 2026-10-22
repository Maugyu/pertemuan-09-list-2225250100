
# Input: Daftar nilai mahasiswa dan batas kelulusan.
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]


# Proses 1: Menghitung rata-rata dengan aman.
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)


# Proses 2: Memilih nilai yang memenuhi batas kelulusan.
def nilai_lulus(data, batas=60):
    lulus = []
    for x in data:
        if x >= batas:
            lulus.append(x)
    return lulus


# Proses 3: Menghitung statistik dan jumlah kelulusan.
jumlah_data = len(nilai)
total = sum(nilai)
lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = jumlah_data - jumlah_lulus

# Output: Menampilkan ringkasan analisis nilai.
print("=== ANALISIS NILAI MAHASISWA ===")
print(f"Seluruh nilai       : {nilai}")
print(f"Banyak data         : {jumlah_data}")
print(f"Total nilai         : {total}")

if jumlah_data > 0:
    print(f"Rata-rata           : {rata_rata(nilai):.2f}")
    print(f"Nilai minimum       : {min(nilai)}")
    print(f"Nilai maksimum      : {max(nilai)}")
else:
    print(f"Rata-rata           : {rata_rata(nilai):.2f}")
    print("Nilai minimum       : Tidak tersedia")
    print("Nilai maksimum      : Tidak tersedia")

print(f"Batas kelulusan     : 60")
print(f"Nilai yang lulus    : {lulus}")
print(f"Jumlah mahasiswa lulus       : {jumlah_lulus}")
print(f"Jumlah belum lulus  : {jumlah_belum_lulus}")


# Pengujian fungsi sesuai test case wajib.
assert rata_rata([60, 70, 80]) == 70
assert min([60, 70, 80]) == 60
assert max([60, 70, 80]) == 80
assert len(nilai_lulus([60, 70, 80])) == 3
assert len(nilai_lulus([59, 60, 61])) == 2
assert rata_rata([]) == 0

print("Semua test case berhasil!")
