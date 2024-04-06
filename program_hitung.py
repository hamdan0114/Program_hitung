def Luas_segitiga():
    print("hitung luas segitiga")
    alas = float(input("masukan alas: "))
    tinggi = float(input("masukan tinggi: "))
    luas = 0.5 * alas * tinggi
    print ("luas segitiga adalah:", luas)
    
def Luas_persegi_panjang():
    print("hitung luas persegi panjang")
    panjang = float(input("masukan panjang: "))
    lebar = float(input("masukan lebar: "))
    luas = panjang * lebar
    print ("luas persegi panjang adalah:", luas)
    
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"
        
while True:
    userinput = int(input("pilih rumus yang akan di pakai\n\n1.hitung luas segitiga\n2.hitung luas persegi\n3.hitung ganjil genap\n4.quit\n\npilih nomor berapa: "))
    if(userinput == 1):
        Luas_segitiga()
    elif(userinput == 2):
        Luas_persegi_panjang()
    elif(userinput == 3):
        try:
            angka = int(input("Masukkan angka: "))
            hasil = cek_ganjil_genap(angka)
            print(f"Angka {angka} adalah {hasil}.")
        except ValueError:
            print("Mohon masukkan bilangan bulat.")
    elif(userinput == 4):
        print("selesai")
        break
    else:
        print("pilih menu yang tersedia")