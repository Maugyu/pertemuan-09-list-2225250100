# Input: Nilai mahasiswa dan batas kelulusan.
nilai = [75, 55, 80, 60, 45, 90]
batas = 60

# Proses: Menyeleksi nilai yang memenuhi batas kelulusan.
lulus = []
for x in nilai:
    if x >= batas:
        lulus.append(x)

# Output: Menampilkan nilai yang lulus dan jumlahnya.
print(f"Nilai lulus = {lulus}")
print(f"Jumlah lulus = {len(lulus)}")
