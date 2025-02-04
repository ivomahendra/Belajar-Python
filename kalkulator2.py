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
            if operasi == '2':
                hasil = angka1 - angka2
                print(f"{angka1} - {angka2} = {hasil}")
            if operasi == '3':
                hasil = angka1 * angka2
                print(f"{angka1} X {angka2} = {hasil}")
            if operasi == '4':
                if angka2 == '0':
                    print('pembagian nilai 0 tidak di perbolehkan')
                else:
                    hasil = angka1 / angka2
                    print(f"{angka1} / {angka2} = {hasil}")
        else:
            print('pilihan tidak tersedia !!! ')
            
if __name__ == "__main__":
    kalkulator()
## Logic
#1 membuat definisi pilihan operasi, isinya :














# def kalkulator():
#     while True:
#         print("\nPilih operasi:")
#         print("1. Penjumlahan")
#         print("2. Pengurangan")
#         print("3. Perkalian")
#         print("4. Pembagian")
#         print("5. Keluar")

#         pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

#         if pilihan == '5':
#             print("Terima kasih telah menggunakan kalkulator. Sampai jumpa!")
#             break

#         if pilihan in ['1', '2', '3', '4']:
#             try:
#                 angka1 = float(input("Masukkan angka pertama: "))
#                 angka2 = float(input("Masukkan angka kedua: "))
#             except ValueError:
#                 print("Input tidak valid. Harap masukkan angka.")
#                 continue

#             if pilihan == '1':
#                 hasil = angka1 + angka2
#                 print(f"Hasil penjumlahan: {angka1} + {angka2} = {hasil}")
#             elif pilihan == '2':
#                 hasil = angka1 - angka2
#                 print(f"Hasil pengurangan: {angka1} - {angka2} = {hasil}")
#             elif pilihan == '3':
#                 hasil = angka1 * angka2
#                 print(f"Hasil perkalian: {angka1} * {angka2} = {hasil}")
#             elif pilihan == '4':
#                 if angka2 == 0:
#                     print("Error: Pembagian dengan nol tidak diperbolehkan.")
#                 else:
#                     hasil = angka1 / angka2
#                     print(f"Hasil pembagian: {angka1} / {angka2} = {hasil}")
#         else:
#             print("Pilihan tidak valid. Silakan coba lagi.")

# if __name__ == "__main__":
#     kalkulator()