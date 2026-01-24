# Laporan Praktikum Kriptografi
Minggu ke-: 14 
Topik: Analisis Serangan Kriptografi
Nama: Asadila Haila Hamada  
NIM: 230202801  
Kelas: 5IKRA  

---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.


---

## 2. Dasar Teori
Serangan kriptografi adalah upaya memanfaatkan kelemaahan dalam algortima, implementasi atau pengelolaan kunci untuk mengakses data rahasia secara ilegal. Jenis serangan yang umum anatara lain adalah brute force yang mencoba satu satu hingga menemukan kunci nya, kemudian ada man in the middle dan replat attack.

Analisis keamanan kriptografi harus memperhatikan tidak hanya algoritma, tetapi juga bagaimana sistem diimplementasikan dan dikelola

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
# Langkah 1 — Identifikasi Serangan
Pilih salah satu kasus nyata serangan kriptografi (contoh: serangan brute force pada hash MD5, kebocoran SSL/TLS, serangan dictionary password).
Identifikasi vektor serangan dan penyebab kelemahan.

# Langkah 2 — Evaluasi Kelemahan
Analisis kelemahan algoritma yang digunakan.
Apakah kelemahan ada pada algoritma kriptografi, implementasi, atau konfigurasi sistem?

# Langkah 3 — Rekomendasi Solusi
Usulkan algoritma atau mekanisme yang lebih aman.
Contoh: mengganti MD5 → SHA-256, RSA lama → ECC, password plaintext → bcrypt/scrypt/Argon2.
Jelaskan alasan pemilihan algoritma dan dampaknya terhadap keamanan sistem

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
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
1. Sistem lama rentan terhadap brute force atau dictionary attack karena menggunakan kunci yang pendek, algortima lemaha atau protokol yang mudah untuk ditebak atau dipecahkan
2. Kelamahan algortima adalah celah pada desain matematis metode kriptografi itu sendiri, sedangkan kelemahan implementasi adalah kesalahan dalam penerapan algortima, seperti pengelolaan kunci yang buruk atau penggunaan random generator yang tidak aman
3. Organisasi dapat menjaga keamanan sistem kriptografi dengan rutin memperbarui algoritma dan protokol, melakukan audit keamanan, mengelola kunci dengan baik serta mengikuti standar dan praktik terbaik keamanan terbaru 
---

## 8. Kesimpulan
Percobaan brute force dan dictionary attack pada hash MD5 menunjukkan bahwa algoritma hash yang cepat dan tanpa proteksi tambahan sangat mudah diserang secara offline. Password atau PIN dengan kemungkinan terbatas bisa dengan cepat ditemukan. Oleh karena itu, sistem modern disarankan menggunakan algoritma pengamanan password seperti bcrypt atau Argon2 untuk meningkatkan keamanan.

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
