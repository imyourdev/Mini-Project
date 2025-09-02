from konversi_suhu import (C_from_F, C_from_K, F_from_C, F_from_K, K_from_C, K_from_F)

garis = "="*3
print (f"{garis} Kalkulator Suhu {garis}")
print()

nilai = float(input("Masukkan nilai suhu = "))
satuan_awal = (input("Dari suhu (C/F/K): ")).upper()
satuan_akhir = (input("Ke Satuan (C/F/K): ")).upper()
print()

if satuan_awal == "C":
  C = nilai
  if satuan_akhir == "F":
    print (f"Hasil: {nilai}°C =", F_from_C (nilai), "°F")
  elif satuan_akhir == "K":
    print (f"Hasil: {nilai}°C =", K_from_C (nilai), "K")

elif satuan_awal == "F":
  F = nilai
  if satuan_akhir == "C":
    print (f"Hasil: {nilai}°F =", C_from_F (nilai), "°C")
  elif satuan_akhir == "K":
    print (f"Hasil: {nilai}°F =", K_from_F (nilai), "K")

else:
  K = nilai
  if satuan_akhir == "C":
    print (f"Hasil: {nilai} K =", C_from_K (nilai), "°C")
  elif satuan_akhir == "F":
    print (f"Hasil: {nilai} K =", F_from_K (nilai), "°F")
''''''

