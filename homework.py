nama = str(input("Masukan Nama Pembeli: "))
jumlah = int(input("Masukan Jumlah yang di beli : "))
harga =int(input("Masukan harga ayam :"))
jumlah_bayar = jumlah * harga

if jumlah >= 5 :
    potongan = 0.05 * harga

else :
    jumlah < 5 
    potongan = 0.00 * harga

total_bayar = jumlah_bayar + potongan

print(f"potongan harga :" , potongan)
print(f"total bayar :" , total_bayar)

