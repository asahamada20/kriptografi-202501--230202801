# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik:= Digital Signature (RSA/DSA)
Nama: Asadila Haila Hamada 
NIM: 230202801  
Kelas: 5 IKRA 

---

## 1. Tujuan
Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
Memverifikasi keaslian tanda tangan digital.
Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---

## 2. Dasar Teori
Tanda tangan digital merupakan teknik kriptografi yang digunakan untuk menjamin keaslian pengirim dan keutuhan sebuah pesan. Berbeda dengan proses enkripsi, mekanisme ini memanfaatkan kunci privat untuk membuat tanda tangan dan kunci publik untuk memeriksanya, sehingga pihak penerima dapat memastikan bahwa pesan benar berasal dari pengirim yang sah dan tidak mengalami perubahan.

Pada skema tanda tangan digital berbasis RSA, pesan tidak ditandatangani secara langsung, melainkan terlebih dahulu diproses menggunakan fungsi hash kriptografis seperti SHA-256 untuk menghasilkan ringkasan pesan. Nilai hash ini kemudian dienkripsi dengan kunci privat pengirim. Proses verifikasi dilakukan dengan kunci publik, yang memungkinkan penerima memeriksa integritas pesan sekaligus mengautentikasi identitas pengirim.

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


```
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())
```
```
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
```
```
# Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
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
1. Perbedaan enkripsi RSA dan tanda tangan digital RSA
Enkripsi RSA berfungsi melindungi kerahasiaan data dengan menggunakan kunci publik milik penerima, sedangkan proses dekripsinya dilakukan dengan kunci privat. Sementara itu, tanda tangan digital RSA digunakan untuk membuktikan identitas pengirim dan keutuhan pesan, di mana pesan ditandatangani dengan kunci privat pengirim dan diverifikasi menggunakan kunci publiknya.

2. Alasan tanda tangan digital menjamin integritas dan keaslian pesan
Tanda tangan digital memastikan integritas karena perubahan sekecil apa pun pada pesan akan membuat hasil verifikasi gagal. Keaslian pengirim juga terjamin karena hanya pemilik kunci privat yang dapat menghasilkan tanda tangan yang valid.

3. Peran Certificate Authority (CA)
Certificate Authority bertindak sebagai pihak tepercaya yang memvalidasi identitas pemilik kunci dan menerbitkan sertifikat digital, sehingga kunci publik dapat dipercaya dan komunikasi terlindungi dari pemalsuan identitas.
---

## 8. Kesimpulan
Praktikum ini memperlihatkan penerapan tanda tangan digital berbasis RSA secara berhasil. Hasil pengujian menunjukkan bahwa proses verifikasi hanya valid jika pesan tetap utuh tanpa perubahan. Hal ini menegaskan bahwa tanda tangan digital berperan penting dalam memastikan keaslian dan keutuhan data pada sistem komunikasi modern.
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
