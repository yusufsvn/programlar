#5 öğrenciden isimlerini ve notlarını girip en yüksek ortalama alanı tebrik eden program
isimler=[]
di={}

for i in range(5):
    x=input("adı girin")
    isimler.append(x)
    for l in range(5):
        y=int(input("1. notu gir"))
        z=int(input("2. notu gir"))
        w=int(input("3. notu gir"))
        s=(y+z+w)/3
        di[s]=x
        break

print(isimler)

# print(di) doğruluğu kontrol etmek için

f=list(di.keys())
f.sort()

# print(f)  doğruluğu kontrol etmek için

print("en başarılı olan kişi:",di[f[4]],"tebrikler ve notu da:",f[4])
