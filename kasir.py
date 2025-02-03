def menu():
    print("="*10,"MENU","="*10)
    print("""
    1. Nasi goreng  Rp. 7.000,-
    2. Nasi rames   Rp. 8.000,-
    3. Es Teh       Rp. 4.000,-
    4. Es Jeruk     Rp. 4.000,-
    5. Selesai 
    """)

def hitung_total(keranjang):
    total=0
    for item in keranjang:
        total += item['harga']* item["jumlah"]
    return total

def main ():
    keranjang = []
    while True:
        menu()
        pilih = input("Pilih menu (1-5) : ")

        if pilih == '1':
            jumlah = int(input('Berapa Porsi Nasi Goreng ? '))
            keranjang.append({'nama': 'Nasi Goreng', 'harga': 7000, 'jumlah': jumlah})
        elif pilih == '2':
            jumlah = int(input('Berapa Porsi Nasi rames ? '))
            keranjang.append({'nama': 'Nasi rames', 'harga': 8000, 'jumlah': jumlah})
        elif pilih == '3':
            jumlah = int(input('Berapa Gelas Es Teh ? '))
            keranjang.append({'nama': 'Es teh','harga': 4000, 'jumlah': jumlah})
        elif pilih == '4':
            jumlah = int(input('Berapa Gelas Es Jeruk ? '))
            keranjang.append({'nama': 'Es Jeruk','harga': 4000, 'jumlah': jumlah})
        elif pilih == '5':
            break
        else :
            print("Pilihan yang anda masukkan tidak terdaftar pada menu, ulangi kembali!!!")

    while True:
        print("\n=========STRUK===========")
        total_harga = 0
        mbayar = 0
        for item in keranjang:
            subtotal = item['harga'] * item['jumlah']
            print(f"{item['nama']} - {item['jumlah']} X Rp. {item['harga']}")
            total_harga += subtotal
        print(f"\nTotal harga : Rp. {total_harga}")
        bayar = int(input("Bayar Rp "))
        mbayar += bayar
        susok = mbayar - total_harga
        if mbayar < total_harga:
            print('\nUang lebih kecil dari harga!!!')
        else:
            break
        
    print('Pengembalian Rp. ',susok)
    print("Terimakasih\n")

if __name__=="__main__":
    main()