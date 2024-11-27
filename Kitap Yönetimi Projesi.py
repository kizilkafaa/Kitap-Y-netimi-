class Kitap:
    def __init__(self, baslik, yazar, yil):
        self.baslik = baslik
        self.yazar = yazar
        self.yil = yil

    def __str__(self):
        return f"{self.baslik} - {self.yazar} ({self.yil})"


class KitapYonetimi:
    def __init__(self):
        self.kitaplar = []

    def kitap_ekle(self, kitap):
        self.kitaplar.append(kitap)
        print(f"{kitap.baslik} kütüphaneye eklendi.")

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("Kütüphane boş!")
        else:
            print("Kütüphanedeki Kitaplar:")
            for index, kitap in enumerate(self.kitaplar, start=1):
                print(f"{index}. {kitap}")

    def kitap_sil(self, baslik):
        for kitap in self.kitaplar:
            if kitap.baslik.lower() == baslik.lower():
                self.kitaplar.remove(kitap)
                print(f"{baslik} kütüphaneden silindi.")
                return
        print(f"{baslik} bulunamadı.")


def main():
    yonetim = KitapYonetimi()

    while True:
        print("\nKitap Yönetim Sistemi")
        print("1. Kitap Ekle")
        print("2. Kitapları Listele")
        print("3. Kitap Sil")
        print("4. Çıkış")

        secim = input("Bir seçenek seçin: ")
        
        if secim == "1":
            baslik = input("Kitap başlığı: ")
            yazar = input("Kitap yazarı: ")
            yil = input("Basım yılı: ")
            yeni_kitap = Kitap(baslik, yazar, yil)
            yonetim.kitap_ekle(yeni_kitap)
        
        elif secim == "2":
            yonetim.kitaplari_listele()
        
        elif secim == "3":
            baslik = input("Silmek istediğiniz kitabın başlığı: ")
            yonetim.kitap_sil(baslik)
        
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz bir seçim yaptınız!")


if __name__ == "__main__":
    main()