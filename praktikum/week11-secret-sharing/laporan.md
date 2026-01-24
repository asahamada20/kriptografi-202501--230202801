# Laporan Praktikum Kriptografi
Minggu ke-: 11
Topik: Secret Sharing 
Nama: Asadila Haila Hamada 
NIM: 230202801  
Kelas: 5IKRA

---

## 1. Tujuan
1. Menjelaskan konsep Shamir Secret Sharing (SSS).
2. Melakukan simulasi pembagian rahasia ke beberapa pihak menggunakan skema SSS.
3. Menganalisis keamanan skema distribusi rahasia.

---

## 2. Dasar Teori
Secret sharing adalah salah satu teknik kriptografi yang digunakan untuk membagi suatu rahasia, seperti kunci enkripsi, ke dalam beberapa bagian yang disebut shares dan dikirimkan kepada beberapa pihak. Rahasia tersebut hanya dapat dipulihkan apabila minimal sejumlah shares tertentu, sesuai dengan nilai ambang batas, digabungkan bersama. Sebaliknya jumlah shares yang kurang dari ambang batas tidak akan memberikan informasi apa pun mengenai rahasia yang dilindungi. 

Cara ini diperkenalkan oleh Adi Shamir dan memanfaatkan prinsip matematika polinomial, dimana sebuah polinomial berderajat hanya dapat ditentukan secara unik olek k titik. Berdasarkan prinsip tersebut, Shamir Secret Sharing memberikan tingkat keamanan yang bersifat informasi - teoritis, hanya bergantung pada kompleksitas komputasi. Oleh karena itu, metode ini sangat seuai untuk pengamanan rahasia penting pada sistem terdistribusi, pengelolaan kunci kriptografi, serta mekanisme toleransi kegagalan

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
# Langkah 1 — Implementasi Shamir Secret Sharing
Contoh sederhana dengan library secretsharing:

from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)
Langkah 2 — Simulasi Manual (Tanpa Library)
Mahasiswa juga dapat mencoba membuat implementasi manual berbasis polinomial modulo p untuk memahami konsep matematis.

Pilih bilangan prima p yang cukup besar.
Bangun polinomial f(x) = a0 + a1x + … + ak-1x^(k-1) mod p, dengan a0 = secret.
Bagikan (x, f(x)) sebagai share.
Rekonstruksi menggunakan Lagrange Interpolation.
Langkah 3 — Analisis Keamanan
Diskusikan:

Mengapa skema (k, n) aman meskipun sebagian share bocor?
Apa risiko jika threshold k terlalu kecil atau terlalu besar?
Bagaimana penerapan SSS di dunia nyata (contoh: manajemen kunci cryptocurrency, recovery password)?

---

## 5. Source Code
from secretsharing import SecretSharer

# Rahasia yang ingin dibagi
secret = "KriptografiUPB2025"

# Bagi menjadi 5 shares, ambang batas 3 (minimal 3 shares untuk rekonstruksi)
shares = SecretSharer.split_secret(secret, 3, 5)
print("Shares:", shares)

# Rekonstruksi rahasia dari 3 shares
recovered = SecretSharer.recover_secret(shares[:3])
print("Recovered secret:", recovered)


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
1. Keutunganya adalah rahasi dapat disimpan dalam satu salinan utuh, sehingga risiko kebocoran dapat minimalkan
2. Peran Threshold adalah untuk menentukan jumlah minimum shares yang harus digabungkan untuk memperoleh kembali rahasia, sehingga memastikan bahwa pihak dengan shares di bawah ambang batas tidak memperoleh informasi apapun
3. Contoh penerapan nyata adalah pada saat pengelolaan kunci enkripsi server, dimana kunci hanya dapat diakses jika beberapa administrator yang berwenang bekerja sama, meningkatkan keamanan dan toleransi kegagalan
---

## 8. Kesimpulan
Shamir Secret Sharing membagi sebuah rahasia ke dalam beberapa share sehingga rahasia hanya dapat direkontruksi jika jumlah minimum terpenuhi. Berbeda dengan pembagian salinan kunci utuh, SSS mencegah kebocoran dari satu pihak karena shar di bawah ambang batas tidak mengungkapkan informasi apa pun. Dengan penentukan nilai k yang tepat, SSS memberikan keamanan lebih tinggi sekaligus menjaga ketersediaan, sehingga cocok untuk melindungi kunci bernilai tinggi seperti kunci private CA, akses cadangan kritis dan recovery key cold wallet

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
