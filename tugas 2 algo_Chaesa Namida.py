ulang = "y"
listA = []
listB = []
while ulang == "y":
    x = int(input("Masukkan Angka: "))
    b=x
    a=x


    for i in range(10):
        a += 1
        listA.append(a)
    
    for i in range(10):
        b -= 1
        listB.append(b)
        
    print("10 angka setelah",x,"yaitu", listA)   
    print("10 angka sebelum",x,"yaitu", listB)
    ulang = input("Ketik y untuk ulang, ketik n untuk berhenti ")
    if ulang == "n":
        print("Terimakasih Sudah Menggunakan Program Ini.")
        print("Chaesa Namida Arumdapta - 064002200008")
        break