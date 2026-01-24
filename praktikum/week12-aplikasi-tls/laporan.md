# Laporan Praktikum Kriptografi
Minggu ke-: 12 
Topik: Aplikasi TLS & E-commerce 
Nama: Asadila Haila Hamada 
NIM: 230202801 
Kelas: 5IKRA 

---

## 1. Tujuan
1. Menganalisis penggunaan kriptografi pada email dan SSL/TLS.
2. Menjelaskan enkripsi dalam transaksi e-commerce.
3. Mengevaluasi isu etika & privasi dalam penggunaan kriptografi di kehidupan sehari-hari.

---

## 2. Dasar Teori
Transport Layer Security adalah protokol keamanan yang melindungi komunikasi data di internet melalui enkripsi, autentikasi, dan penjagaan integritas data. Dengan mengenkripsi pertukaran data antara klien dan server, TLS mencegah pihak tidak berwenang mengakses informasi sensitif seperti kredensial login dan data transaksi, serta memastikan keaslian server melalui sertifikat digital

Dalam e-commerce, TLS berperan penting karena seluruh proses transaksi melibatkan data rahasia. Penggunaan TLS melindungi sistem dari serangan seperti penyadapan dan man in the middle, menjamin data tidak diubah selama transisi, serta meningkatkan kepercayaan pengguna dan kredibilitas platform e-commerce 

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
# Langkah 1 — Analisis SSL/TLS pada Email & Web
Gunakan browser (Chrome/Firefox) untuk mengecek sertifikat digital pada website e-commerce (contoh: Tokopedia, Shopee, Bukalapak).
Catat informasi berikut:
Issuer CA (Certificate Authority).
Masa berlaku sertifikat.
Algoritma enkripsi yang digunakan (RSA, AES, dll).
Bandingkan perbedaan antara website dengan HTTPS dan tanpa HTTPS.

# Langkah 2 — Studi Kasus E-commerce
Analisis bagaimana enkripsi digunakan untuk melindungi transaksi online (misalnya saat login atau melakukan pembayaran).
Diskusikan potensi ancaman jika TLS tidak digunakan (contoh: serangan Man-in-the-Middle).

# Langkah 3 — Analisis Etika & Privasi
Identifikasi isu privasi dalam penggunaan email terenkripsi (PGP, S/MIME).
Diskusikan dilema etika:
Apakah perusahaan boleh melakukan dekripsi email karyawan untuk audit?
Bagaimana kebijakan pemerintah dalam pengawasan komunikasi terenkripsi?


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
1. Perbedaanya teletak pada keamaaanya. HTTP mengirimkan data tanpa enkripsi sehingga mudah disadap, sedangkan HTTPS menggunakan TLS untuk mengenkripsi komunikasi sehingga data lebih aman dari akses yang tidak valid atau tidak sah
2. Pentingnya sertifikast digital dalam TLS adalah untuk memverifikasi identitas server yang di akses
3. Peran kriptografi dalam privasi sekaligus tantangan hukum etika adalah kemampuanya melindungi kerahasiaan data dan komunikasi pengguna, namun disisi lain dapat menyulitkan penegak hukum karena data yang terenkripsi sulit untuk diakses, sehingga menimbulkan dilema antara perlindungan privasi dan kepentingan keamanan publik
---

## 8. Kesimpulan
Enkripsi seperti TLS membuat data login dan transaksi terlindungi dari penyadapan dan manipulasi. Tanpa enkripsi, komunikasi rentan terhadap serangan man in the middle. Oleh karena itu, TLS penting untuk menjaga keamanan transaksi online dan meningkatkan kepercayaan pengguna

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
