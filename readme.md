# Stock Checker Bot

Bu proje, kullanıcıdan alınan bir ürün URL'si ile belirli bir Gratis sitesinde ürün stok kontrolü yapar. Belirtilen ürün stokta mevcutsa kullanıcıya bildirim verir. İlerleyen aşamalarda, URL'lerin veritabanına eklenmesi, stok kontrolünün belirli aralıklarla otomatik olarak yapılması ve stok durumu değiştiğinde bildirim gönderilmesi planlanmaktadır.

## 🚀 Özellikler

- **Manuel Stok Kontrolü**: Kullanıcıdan alınan URL üzerinden stok kontrolü yapar.


🛠 **Geliştirilmesi Planlanan Özellikler**:

- **URL'lerin Veritabanına Kaydedilmesi**: Kullanıcı tarafından girilen URL'lerin saklanması.
- **Otomatik Stok Kontrolü**: Belirlenen periyotlarla stok durumunun otomatik kontrol edilmesi.
- **Bildirim Gönderme**: Ürün stoğa girdiğinde kullanıcıya e-posta veya anlık bildirim gönderilmesi.

---

## 🛠 Gereksinimler

Bu projeyi çalıştırmak için aşağıdaki Python paketlerini yüklemeniz gerekmektedir:

```bash
pip install requests beautifulsoup4
