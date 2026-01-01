# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: Diffie-Hellman Key Exchange
Nama: Asadila Haila Hamada  
NIM: 230202801
Kelas: 5 IKRA

---

## 1. Tujuan
1. Melakukan simulasi protokol Diffie-Hellman untuk pertukaran kunci publik.
2. Menjelaskan mekanisme pertukaran kunci rahasia menggunakan bilangan prima dan logaritma diskrit.
3. Menganalisis potensi serangan pada protokol Diffie-Hellman (termasuk serangan Man-in-the-Middle / MITM).


---

## 2. Dasar Teori
Diffie–Hellman Key Exchange adalah protokol kriptografi yang memungkinkan dua pihak membentuk kunci rahasia bersama melalui saluran publik tanpa mengirimkan kunci tersebut secara langsung. Keamanannya bergantung pada operasi eksponensial modular dan sulitnya Discrete Logarithm Problem, sehingga kunci privat tidak dapat dengan mudah ditebak dari nilai publik. Protokol ini banyak digunakan dalam sistem keamanan modern seperti TLS, namun versi dasarnya tidak menyediakan autentikasi sehingga rentan terhadap serangan Man-in-the-Middle jika tidak disertai mekanisme verifikasi identitas.

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
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)
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
1. Mengapa Diffie–Hellman dapat digunakan di saluran publik?
Diffie–Hellman memungkinkan pertukaran kunci di saluran publik karena kunci rahasia tidak pernah dikirimkan secara langsung. Kedua pihak hanya bertukar nilai publik, sementara kunci bersama dihasilkan secara lokal dan keamanannya dijamin oleh sulitnya Discrete Logarithm Problem.

2. Kelemahan utama Diffie–Hellman murni
Kelemahan utama protokol Diffie–Hellman murni adalah tidak adanya mekanisme autentikasi, sehingga rentan terhadap serangan Man-in-the-Middle, di mana penyerang dapat menyamar sebagai pihak yang sah.

3. Cara mencegah serangan MITM pada Diffie–Hellman
Serangan MITM dapat dicegah dengan menambahkan autentikasi, seperti penggunaan sertifikat digital, tanda tangan digital, atau dengan mengintegrasikan Diffie–Hellman ke dalam protokol yang terautentikasi seperti TLS.
---

## 8. Kesimpulan
Praktikum ini membuktikan bahwa Diffie–Hellman mampu membentuk kunci bersama melalui jaringan publik karena sulitnya menyelesaikan masalah logaritma diskrit. Namun, tanpa mekanisme autentikasi, protokol dasarnya tetap rentan terhadap serangan MITM, sehingga penerapan nyata harus menggunakan Diffie–Hellman yang dilengkapi proses verifikasi identitas.

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
