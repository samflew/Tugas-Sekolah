# Author: samflew (raiyan)
# Date: 09/20/24 (September 20 2024)
# Description: Program ini akan menilai berapa nilai rata-rata dari semua mata pelajaran user

# https://github.com/samflew
# https://instagram.com/samflew

nilai_siswa = {}

while True:
    mata_pelajaran = input("Mata Pelajaran? :")
    nilai_mata_pelaran = float(input(f"Nilai Kamu Di Mapel {mata_pelajaran}?:"))
    if nilai_mata_pelaran < 0.0 or nilai_mata_pelaran > 100.0:
        print("Nilai mata pelajaran minimal adalah 1 dan maksimal adalah 100!")
    else:
        nilai_siswa[mata_pelajaran] = nilai_mata_pelaran

    jawaban = input("Apakah kamu ingin menambahkan mata pelajaran lain? (y/n)")
    if len(jawaban) < 1 or jawaban == "n":
        break


total_nilai_siswa = 0.0
for mapel in nilai_siswa:
    total_nilai_siswa += nilai_siswa[mapel]


print(f"Rata-rata nilai kamu: {total_nilai_siswa / len(nilai_siswa)}")