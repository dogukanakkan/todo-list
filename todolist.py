import os

# Görevleri dosyadan okuma
def gorevleri_yukle(dosya_adi):
    gorevler = []
    if os.path.exists(dosya_adi):
        with open(dosya_adi, 'r') as file:
            for line in file:
                isim, durum = line.strip().split(',')
                gorevler.append({"isim": isim, "tamamlandi": durum == "True"})
    return gorevler

# Görevleri dosyaya kaydetme
def gorevleri_kaydet(dosya_adi, gorevler):
    with open(dosya_adi, 'w') as file:
        for gorev in gorevler:
            file.write(f"{gorev['isim']},{gorev['tamamlandi']}\n")

# Görev ekleme
def gorev_ekle(gorevler):
    isim = input("Yeni görevin adı: ")
    gorevler.append({"isim": isim, "tamamlandi": False})
    print(f"'{isim}' görevi listeye eklendi.")

# Görev listeleme
def gorevleri_listele(gorevler):
    if not gorevler:
        print("Henüz eklenmiş bir görev yok.")
    else:
        print("\nYapılacak Görevler:")
        for i, gorev in enumerate(gorevler, start=1):
            durum = "Tamamlandı" if gorev["tamamlandi"] else "Tamamlanmadı"
            print(f"{i}. {gorev['isim']} - {durum}")

# Görev güncelleme (tamamlanma durumu değiştirme)
def gorev_guncelle(gorevler):
    gorevleri_listele(gorevler)
    try:
        secim = int(input("Tamamlandığını işaretlemek istediğiniz görevin numarasını girin: "))
        gorevler[secim - 1]["tamamlandi"] = not gorevler[secim - 1]["tamamlandi"]
        durum = "Tamamlandı" if gorevler[secim - 1]["tamamlandi"] else "Tamamlanmadı"
        print(f"'{gorevler[secim - 1]['isim']}' görevi {durum} olarak güncellendi.")
    except (IndexError, ValueError):
        print("Geçersiz seçim.")

# Görev silme
def gorev_sil(gorevler):
    gorevleri_listele(gorevler)
    try:
        secim = int(input("Silmek istediğiniz görevin numarasını girin: "))
        silinen_gorev = gorevler.pop(secim - 1)
        print(f"'{silinen_gorev['isim']}' görevi silindi.")
    except (IndexError, ValueError):
        print("Geçersiz seçim.")

# Ana menü
def menu():
    print("\n--- Yapılacaklar Listesi Uygulaması ---")
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Görev Durumunu Güncelle")
    print("4. Görev Sil")
    print("5. Çıkış ve Kaydet")
    return input("Bir seçenek girin: ")

# Uygulamanın ana fonksiyonu
def todo_list():
    dosya_adi = "gorevler.txt"
    gorevler = gorevleri_yukle(dosya_adi)

    while True:
        secim = menu()
        if secim == "1":
            gorev_ekle(gorevler)
        elif secim == "2":
            gorevleri_listele(gorevler)
        elif secim == "3":
            gorev_guncelle(gorevler)
        elif secim == "4":
            gorev_sil(gorevler)
        elif secim == "5":
            gorevleri_kaydet(dosya_adi, gorevler)
            print("Görevler kaydedildi. Çıkış yapılıyor.")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

# Uygulamayı başlat
todo_list()
