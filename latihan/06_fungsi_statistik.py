# Input: List nilai mahasiswa.
nilai = [75, 80, 65, 90, 88]

# Proses: Membuat fungsi untuk menghitung rata-rata.
def rata_rata(data):
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

# Output: Menampilkan rata-rata.
print(f"Rata-rata = {rata_rata(nilai):.2f}")
print(f"Rata-rata list kosong = {rata_rata([]):.2f}")
