def main():
    print('======Kalkulator======\nctrl + c untuk keluar\n')
    

while True:
    main()
    try :
        numb1=float(input("Masukkan angka 1 : "))
        op=input("operasi +,-,*,/: ")
        numb2=float(input("Masukkan angka 2 : "))
    except ValueError:
        print("masukkan angka dengan benar\n")
        continue
    if op == "+" :
        hasil = numb1 + numb2
        print(f'{numb1} + {numb2} = {hasil}\n')
    elif op == "-" :
        hasil = numb1 - numb2
        print(f'{numb1} - {numb2} = {hasil}\n')
    elif op == "*" :
        hasil = numb1 * numb2
        print(f'{numb1} x {numb2} = {hasil}\n')
    elif op == "/" :
        hasil = numb1 / numb2
        if numb2 == 0:
            print('pembagian 0 tidak diperbolehkan')
        else:
            print(f'{numb1} / {numb2} = {hasil}\n')
    else :
        print("masukkan operasi sesuai format")