# DDP LAB-2

# SOAL 1 - Mencetak bilangan
# Tuliskan program untuk Soal 1 di bawah ini
for i in range(100, 1, -2):
  print(i)





# SOAL 2 - Menghitung rata-rata
# Tuliskan program untuk Soal 2 di bawah ini
nilai =eval(input("masukan banyaknya nilai:"))

for i in range (0, nilai):
  A =eval(input("masukan nilai:"))
  A += A
  rata_rata = A / nilai
print("rata rata nilai tersebut" , rata_rata)


# SOAL 3 - Mencetak persegi
# Tuliskan program untuk Soal 3 di bawah ini
for i in range(4):
    for j in range(4):
        print('#', end=' ')
    print()

