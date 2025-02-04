numb1=float(input("Masukkan angka 1 : "))
op=input("operasi +,-,*,/: ")
numb2=float(input("Masukkan angka 2 : "))
if op == "+" :
   print("hasil penjumlahan : ",numb1+numb2)
elif op == "-" :
    print("Hasil pengurangan : ",numb1-numb2)
elif op == "*" :
    print("hasil perkalian : ",numb1*numb2)
elif op == "/" :
    print("Hasil pembagian : ",numb1/numb2)
else :
    print("masukkan operasi sesuai format")

except ValueError:
print("Invalid Input, please input only numbers")

restart = input("Do you want to CALCULATE again? : ")


if restart == "yes":

    main()

else:
    print("Thanks! for calculating keep learning! hope you have a good day :)")


    exit()