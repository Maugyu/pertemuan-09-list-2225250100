# Input: Lima nilai mahasiswa.
nilai = [75, 80, 65, 90, 88]

# Proses: Menghitung statistik data.
total = sum(nilai)
rata_rata = total / len(nilai)
minimum = min(nilai)
maksimum = max(nilai)

# Output: Menampilkan hasil statistik.
print(f"Total = {total}")
print(f"Rata-rata = {rata_rata:.2f}")
print(f"Minimum = {minimum}")
print(f"Maksimum = {maksimum}")
