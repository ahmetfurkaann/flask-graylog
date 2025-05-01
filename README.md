# Flask-Graylog Login Uygulaması

Bu proje, Flask web framework'ü kullanılarak geliştirilmiş, Graylog entegrasyonlu basit bir login uygulamasıdır.

## 🚀 Özellikler

- Modern ve kullanıcı dostu arayüz
- Responsive tasarım
- Güvenli şifre hashleme (SHA-256)
- Graylog entegrasyonu ile loglama
- Form doğrulama
- Hata mesajları gösterimi

## 🛠️ Kurulum

1. Gerekli paketleri yükleyin:
```bash
pip install flask graypy
```

2. Graylog sunucunuzun çalıştığından emin olun (varsayılan: localhost:12201)

3. Uygulamayı çalıştırın:
```bash
python graylog.py
```

## 📁 Proje Yapısı

```
flask-graylog/
├── graylog.py          # Ana uygulama dosyası
├── templates/
│   └── login.html      # Login sayfası template'i
└── README.md           # Bu dosya
```

## 🔐 Varsayılan Kullanıcı Bilgileri

- Kullanıcı adı: `testuser`
- Şifre: `testpassword`

veya

- Kullanıcı adı: `admin`
- Şifre: `admin1234`

## 📝 Kullanım

1. Tarayıcınızda `http://localhost:5000/login` adresine gidin
2. Kullanıcı adı ve şifrenizi girin
3. Giriş yapın

## 🔍 Graylog Entegrasyonu

Uygulama, aşağıdaki olayları Graylog'a loglar:
- Başarılı girişler
- Hatalı şifre girişleri
- Var olmayan kullanıcı girişleri

