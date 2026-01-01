# Laporan Praktikum Kriptografi
Minggu ke-: 10 
Topik: Public Key Infrastructure (PKI & Certificate Authority)
Nama: Asadila Haila Hamada 
NIM: 23002801
Kelas: 5 IKRA

---

## 1. Tujuan
1. Membuat sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).
---

## 2. Dasar Teori
Public Key Infrastructure (PKI) merupakan kerangka kerja yang mengatur pengelolaan sertifikat digital, mulai dari penerbitan hingga pencabutan, guna menjamin keamanan komunikasi. Sistem ini memanfaatkan pasangan kunci publik dan privat, di mana sertifikat digital digunakan untuk mengaitkan identitas dengan kunci publik dan dikeluarkan oleh pihak tepercaya.

Certificate Authority (CA) berperan sebagai lembaga yang memverifikasi identitas dan menandatangani sertifikat digital. Kepercayaan terhadap CA ditanamkan pada browser dan sistem operasi melalui daftar root CA, sehingga komunikasi seperti HTTPS/TLS dapat memastikan keaslian server dan melindungi pengguna dari serangan perantara seperti Man-in-the-Middle.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
```python
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from datetime import datetime, timedelta

# Generate key pair
key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Buat subject & issuer (CA sederhana = self-signed)
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"ID"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"UPB Kriptografi"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"example.com"),
])

# Buat sertifikat
cert = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.utcnow())
    .not_valid_after(datetime.utcnow() + timedelta(days=365))
    .sign(key, hashes.SHA256())
)

# Simpan sertifikat
with open("cert.pem", "wb") as f:
    f.write(cert.public_bytes(serialization.Encoding.PEM))

print("Sertifikat digital berhasil dibuat: cert.pem")
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
1. Fungsi utama Certificate Authority (CA)
Certificate Authority berperan sebagai lembaga tepercaya yang melakukan verifikasi identitas pemilik kunci publik dan menerbitkan sertifikat digital, sehingga kunci tersebut dapat digunakan secara aman dalam komunikasi.

2. Alasan self-signed certificate tidak sesuai untuk sistem produksi
Self-signed certificate tidak melalui proses validasi oleh CA resmi, sehingga keaslian identitasnya tidak dapat dipastikan. Hal ini menyebabkan munculnya peringatan keamanan pada browser dan membuatnya kurang aman untuk digunakan di lingkungan produksi.

3. Peran PKI dalam mencegah serangan MITM pada TLS/HTTPS
PKI melindungi komunikasi TLS/HTTPS dengan memastikan sertifikat server divalidasi oleh CA yang dipercaya. Dengan demikian, kunci publik yang digunakan benar-benar milik server yang sah dan penyerang tidak dapat menyamar sebagai pihak lain.
---

## 8. Kesimpulan
Dalam praktikum ini, mahasiswa berhasil mengimplementasikan pembuatan sertifikat digital sederhana menggunakan Python. Percobaan tersebut membantu memahami peran Certificate Authority dalam membangun kepercayaan, serta bagaimana PKI mendukung komunikasi aman seperti HTTPS. Hasilnya menunjukkan bahwa PKI sangat penting dalam menjaga integritas, keaslian, dan kerahasiaan data.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
