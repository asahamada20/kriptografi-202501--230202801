# Laporan Praktikum Kriptografi
Minggu ke-: 4
Topik: Entropy & Unicity Distance (Evaluasi Kekuatan Kunci dan Brute Force)
Nama: Asadila Haila Hamada
NIM: 230202801
Kelas: 5 IKRA
---

## 1. Tujuan
1. Menyelesaikan perhitungan sederhana terkait entropi kunci.
2. Menggunakan teorema Euler pada contoh perhitungan modular & invers.
3. Menghitung unicity distance untuk ciphertext tertentu.
4. Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
5. Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.

---

## 2. Dasar Teori
ENTROPHY
Entrophy adalah ukuran sebearapa bagus dan buruknya suatu kunci kriptografi. Semakin tinggi entropi maka hasilnya akan semakin sulit untuk di tebak. Pada keamanan entropi penting karena dapat menentukan seberapa kuat kunci tersebut bertahan terhadap serangan 

Uncity Distance 
adalah jumlah minimum chiptertext agar serangan brute force dapat menentukan suatu kunci yang benar tanpa keraguan. Nilai unicity dapat menunjukan chiper lebih tahan terhadap analisis kunci berdasarkan data yang tersedia 

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Buat folder berikut:
praktikum/week4-entropy-unicity/
├─ src/
├─ screenshots/
└─ laporan.md
Gunakan Python 3.11 atau lebih baru.
Materi rujukan: Stallings (2017), Bab 3.
Panduan Langkah demi Langkah
Langkah 1 — Perhitungan Entropi
Gunakan rumus:
[ H(K) = \log_2 |K| ]
dengan (|K|) adalah ukuran ruang kunci.

Contoh implementasi Python:

import math

def entropy(keyspace_size):
    return math.log2(keyspace_size)

print("Entropy ruang kunci 26 =", entropy(26), "bit")
print("Entropy ruang kunci 2^128 =", entropy(2**128), "bit")
Langkah 2 — Menghitung Unicity Distance
Gunakan rumus:
[ U = \frac{H(K)}{R \cdot \log_2 |A|} ]
dengan:

(H(K)): entropi kunci,
(R): redundansi bahasa (misal bahasa Inggris (R \approx 0.75)),
(|A|): ukuran alfabet (26 untuk A–Z).
Contoh implementasi Python:

def unicity_distance(HK, R=0.75, A=26):
    return HK / (R * math.log2(A))

HK = entropy(26)
print("Unicity Distance untuk Caesar Cipher =", unicity_distance(HK))
Langkah 3 — Analisis Brute Force
Simulasikan waktu brute force dengan asumsi kecepatan komputer tertentu.

def brute_force_time(keyspace_size, attempts_per_second=1e6):
    seconds = keyspace_size / attempts_per_second
    days = seconds / (3600*24)
    return days

print("Waktu brute force Caesar Cipher (26 kunci) =", brute_force_time(26), "hari")
print("Waktu brute force AES-128 =", brute_force_time(2**128), "hari")
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
- Pertanyaan 1:Nilai entrophy menunjukan tingkat kesulitan dan banyaknya penebakan kunci yang dapat digunakan, semakin besar nilai entrhopy maka dihitung semakin sulit untuk di tebak
   
- Pertanyaan 2: Unity Distance sangat penting karena dapat menunjukan seberapa banayak chipertext yang diperlukan agar penyerang dapat menemukan kunci yang pasti. Artinya chiper tersebut lebih aman karena hanya dengan menganalisis data yang terenkripsi

- Pertanyaan 3: Brute Force masih berbahaya karean beberapa kasus memiliki kunci yang lemah, implementasi yang buruk, tertinggalnya perkembangan komputasi modern
)
---

## 8. Kesimpulan
Entrophy dan Unicty Distance merupakan 2 konsep yang penting dalam menilai suatu kekuatan pada sistem kriptografi

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
commit f0fff3256cfd82ec4155ff64d2eacbe64ad2e1e9 (HEAD -> main, origin/main, origin/HEAD)
Author: asahamada20 <164310674+asahamada20@users.noreply.github.com>
Date:   Mon Nov 17 00:24:58 2025 +0700

    Add files via upload

commit 608bfbf3c2164fcdae12298889635039290c6b9c
Author: asahamada20 <164310674+asahamada20@users.noreply.github.com>
Date:   Mon Nov 17 00:24:36 2025 +0700

    Create .png

commit 66875f937758622560e9fcf974b5297ce79c8bae
Author: asahamada20 <164310674+asahamada20@users.noreply.github.com>
Date:   Mon Nov 17 00:24:06 2025 +0700

    Delete praktikum/week4-entropy-unicity/src directory

commit 97dc03e566f36f9af782fe957c8e1e02a92530aa
Author: asahamada20 <164310674+asahamada20@users.noreply.github.com>
Date:   Mon Nov 17 00:22:29 2025 +0700

```
