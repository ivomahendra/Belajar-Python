def main():
    print('======Kalkulator======\nctrl + c untuk keluar\n')
    

while True:
    main()
    numb1=float(input("Masukkan angka 1 : "))
    op=input("operasi +,-,*,/: ")
    numb2=float(input("Masukkan angka 2 : "))
    if op == "+" :
        print("hasil penjumlahan : ",numb1+numb2,'\n')
    elif op == "-" :
        print("Hasil pengurangan : ",numb1-numb2,'\n')
    elif op == "*" :
        print("hasil perkalian : ",numb1*numb2,'\n')
    elif op == "/" :
        print("Hasil pembagian : ",numb1/numb2,'\n')
    else :
        print("masukkan operasi sesuai format")