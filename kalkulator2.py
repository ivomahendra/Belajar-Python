def kalkulator():
    while True:
        print("\npilih operasi kalkulator")
        print('1. Penjumlahan')
        print('2. Pengurangan')
        print('3. Perkalian')
        print('4. Pembagian')
        print('5. Keluar')

        operasi = input('masukkan pilihan operasi 1/2/3/4/5 : ')

        if operasi == '5':
            print('Terimakasih telah menggunakan kalkulator ini')
            break
        if operasi in ['1','2','3','4']:
            try:
                angka1 = float(input('masukkan angka 1 : '))
                angka2 = float(input('masukkah angka 2 : '))
            except ValueError:
                print('Masukkan angka')
                continue

            if operasi == '1':
                hasil = angka1 + angka2
                print(f"{angka1} + {angka2} = {hasil}")
            elif operasi == '2':
                hasil = angka1 - angka2
                print(f"{angka1} - {angka2} = {hasil}")
            elif operasi == '3':
                hasil = angka1 * angka2
                print(f"{angka1} X {angka2} = {hasil}")
            elif operasi == '4':
                if angka2 == 0:
                    print('pembagian nilai 0 tidak di perbolehkan')
                else:
                    hasil = angka1 / angka2
                    print(f"{angka1} / {angka2} = {hasil}")
        else:
            print('pilihan tidak tersedia !!! ')
            
if __name__ == "__main__":
    kalkulator()