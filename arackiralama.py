from tkinter import *
from tkinter import messagebox
from datetime import datetime


class AracKiralamaSistemi:
    def __init__(self,ekran):
        self.ekran=ekran
        self.ekran.title("ARAC KIRALA")

        self.Araclar=[]
        self.musteriler=[]
        self.kiralamalar=[]

        self.ekrani_olustur()

    def ekrani_olustur(self):
        Label(self.ekran,text="ARAC EKLE").grid(row=0,column=0,pady=10)
        Label(self.ekran,text="Marka").grid(row=1,column=0)
        self.arac_marka=Entry(self.ekran)
        self.arac_marka.grid(row=1,column=1)

        Label(self.ekran, text="Model").grid(row=2, column=0)
        self.arac_model = Entry(self.ekran)
        self.arac_model.grid(row=2, column=1)
        
        Label(self.ekran, text="Plaka").grid(row=3, column=0)
        self.arac_plaka = Entry(self.ekran)
        self.arac_plaka.grid(row=3, column=1)

        Label(self.ekran, text="Kiralama Ücreti").grid(row=4, column=0)
        self.arac_ucret = Entry(self.ekran)
        self.arac_ucret.grid(row=4, column=1)

        Button(self.ekran,text="Arac Ekle",command=self.aracEkle).grid(row=5,column=1,pady=10)

        # Müşteri Ekleme ekranı
        Label(self.ekran, text="Müşteri Ekle").grid(row=0, column=2, pady=10)
        Label(self.ekran, text="Ad").grid(row=1, column=2)
        self.musteri_ad = Entry(self.ekran)
        self.musteri_ad.grid(row=1, column=3)
        
        Label(self.ekran, text="Soyad").grid(row=2, column=2)
        self.musteri_soyad =Entry(self.ekran)
        self.musteri_soyad.grid(row=2, column=3)
        
        Label(self.ekran, text="Müşteri No").grid(row=3, column=2)
        self.musteri_no = Entry(self.ekran)
        self.musteri_no.grid(row=3, column=3)
        
        Label(self.ekran, text="Ehliyet Bilgileri").grid(row=4, column=2)
        self.musteri_ehliyet = Entry(self.ekran)
        self.musteri_ehliyet.grid(row=4, column=3)

        Button(self.ekran,text="Müsteri Ekle",command=self.musteriEkle).grid(row=5,column=3)

        # Kiralama işlem ekranı
        Label(self.ekran, text="Kiralama İşlemi").grid(row=6, column=0, pady=10)
        Label(self.ekran, text="Araç Plakası").grid(row=7, column=0)
        self.kiralama_arac = Entry(self.ekran)
        self.kiralama_arac.grid(row=7, column=1)
        
        Label(self.ekran, text="Müşteri No").grid(row=8, column=0)
        self.kiralama_musteri = Entry(self.ekran)
        self.kiralama_musteri.grid(row=8, column=1)
        
        Label(self.ekran, text="Kiralama Tarihi (YYYY-MM-DD)").grid(row=9, column=0)
        self.kiralama_tarih = Entry(self.ekran)
        self.kiralama_tarih.grid(row=9, column=1)
        
        Label(self.ekran, text="İade Tarihi (YYYY-MM-DD)").grid(row=10, column=0)
        self.iade_tarih = Entry(self.ekran)
        self.iade_tarih.grid(row=10, column=1)

        Button(self.ekran,text="Kiralama Yap",command=self.kiralama).grid(row=11,column=1)

        self.foto=PhotoImage(file="Car-Hero_1920x800.png")
        Label(ekran,image=self.foto).grid(row=14,column=0,columnspan=26)

    def aracEkle(self):
        marka=self.arac_marka.get()
        model=self.arac_model.get()
        plaka=self.arac_plaka.get()
        Ucret=self.arac_ucret.get()

        if not marka:
            messagebox.showerror("Eksik bilgi","bütüm bilgileri girdignizden emin olun")
        elif not model:
            messagebox.showerror("Eksik bilgi","bütüm bilgileri girdignizden emin olun")
        elif not plaka:
            messagebox.showerror("Eksik bilgi","bütüm bilgileri girdignizden emin olun")
        elif not Ucret:
            messagebox.showerror("Eksik bilgi","bütüm bilgileri girdignizden emin olun")
        else:

            yeniArar=Arac(marka,model,plaka,Ucret)
            self.Araclar.append(yeniArar)
            print(marka,model,plaka,Ucret)


            messagebox.showinfo("Basarili islem","Araciniz basariyla kaydedildi")

    def musteriEkle(self):
        ad=self.musteri_ad.get()
        soyad=self.musteri_soyad.get()
        musterino=self.musteri_no.get()
        ehliyet=self.musteri_ehliyet.get()

        if not ad:
            messagebox.showerror("Eksik bilgi","bütün bilgileri dogru girdignizden emin olun")
        elif not soyad:
            messagebox.showerror("Eksik bilgi","bütün bilgileri dogrugirdignizden emin olun")
        elif not musterino:
            messagebox.showerror("Eksik bilgi","bütün bilgileri dogru girdignizden emin olun")
        elif not ehliyet:
            messagebox.showerror("Eksik bilgi","bütün bilgileri dogru girdignizden emin olun")
        elif not musterino.isdigit():
            messagebox.showerror("Eksik bilgi","Lütfen Müsteri numaraniz icin sayi kullaniniz")

        else:
        

            yeni_musteri= Musteri(ad,soyad,musterino,ehliyet)
            self.musteriler.append(yeni_musteri)
            print(ad,soyad,musterino,ehliyet)
            messagebox.showinfo("Basarili islem","musteriniz basariyla kaydedildi")
    
    def kiralama(self):
        kiralanacakArac=self.kiralama_arac.get()
        kiralayacakMusteri=self.kiralama_musteri.get()
        alinantarih=self.kiralama_tarih.get()
        teslimtarihi=self.iade_tarih.get()

        for arac in self.Araclar:
            if arac.plaka==kiralanacakArac:
                for musteri in self.musteriler:
                    if musteri.musterino ==kiralayacakMusteri:
                        messagebox.showinfo("Basarili islem","Kiralama Islemi basariyla gerceklesti")






class Arac:
    def __init__(self,marka,model,plaka,ucret):
        self.marka=marka
        self.model=model
        self.plaka=plaka
        self.ucret=ucret


class Musteri:
    def __init__(self,ad,soyad,musterino,ehliyetbilgileri):
        self.ad=ad
        self.soyad=soyad
        self.musterino=musterino
        self.ehliyetbilgileri=ehliyetbilgileri


class Kiralama:
    def __init__(self,aracplaka,musterino,kiralamatarihi,iadetarihi):
        self.aracplaka=aracplaka
        self.musterino=musterino
        self.kiralamatarihi=kiralamatarihi
        self.iadetarihi=iadetarihi
        
ekran=Tk()
app=AracKiralamaSistemi(ekran)

ekran.mainloop()