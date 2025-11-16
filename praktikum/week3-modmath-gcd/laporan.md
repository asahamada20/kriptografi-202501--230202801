# Laporan Praktikum Kriptografi
Minggu ke-: 3 
Topik: Modular Math 
Nama: Asadila Haila Hamada
NIM: 230202801
Kelas: 5 IKRA

---

## 1. Tujuan
1. Menyelesaikan operasi aritmetika modular.
2. Menentukan bilangan prima dan menghitung GCD (Greatest Common Divisor).
3. Menerapkan logaritma diskrit sederhana dalam simulasi kriptografi.

---

## 2. Dasar Teori
Aritmetika modular adalah sistem matematika yang bekerja dengan bilangan “berulang” (wrap around) setelah mencapai nilai tertentu yang disebut modulus (n).
Konsep ini menjadi dasar hampir semua algoritma kriptografi modern seperti RSA, Diffie–Hellman, dan ECC.

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
Langkah 1 — Aritmetika Modular
Tuliskan fungsi untuk menghitung operasi modular dasar.

def mod_add(a, b, n): return (a + b) % n
def mod_sub(a, b, n): return (a - b) % n
def mod_mul(a, b, n): return (a * b) % n
def mod_exp(base, exp, n): return pow(base, exp, n)  # eksponensiasi modular

print("7 + 5 mod 12 =", mod_add(7, 5, 12))
print("7 * 5 mod 12 =", mod_mul(7, 5, 12))
print("7^128 mod 13 =", mod_exp(7, 128, 13))
Langkah 2 — GCD & Algoritma Euclidean
Implementasikan fungsi GCD dengan algoritma Euclidean.

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("gcd(54, 24) =", gcd(54, 24))
Langkah 3 — Extended Euclidean Algorithm
Tambahkan fungsi untuk mencari invers modular.

def egcd(a, b):
    if a == 0:
        return b, 0, 1
    g, x1, y1 = egcd(b % a, a)
    return g, y1 - (b // a) * x1, x1

def modinv(a, n):
    g, x, _ = egcd(a, n)
    if g != 1:
        return None
    return x % n

print("Invers 3 mod 11 =", modinv(3, 11))  # hasil: 4
Langkah 4 — Logaritma Diskrit (Discrete Log)
Simulasikan logaritma diskrit sederhana: mencari x sehingga a^x ≡ b (mod n).

def discrete_log(a, b, n):
    for x in range(n):
        if pow(a, x, n) == b:
            return x
    return None

print("3^x ≡ 4 (mod 7), x =", discrete_log(3, 4, 7))  # hasil: 4
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
- Pertanyaan 1: Peran aritmetika modular dalam kriptografi modern
Artimatikan modulatr digunakan pada semua sistem oprasi karna membuat perhitungan bekerja di ruang bilangan terbatas

- Pertanyaan 2: Mengapa invers modular penting dalam RSA?
Karena jika tanpa invers modular, kunci publick dan private tidak bisa bekerja sebagai pasangan yang aman

- Pertanyaan 3: Tantangan utama logaritma diskrit untuk modulus besar
  Tantangan utama nya adalah karena tidak adanya algoritma cepat untuk mencari x pada persamaan gˣ mod p = h oleh karna itu menjadi sangar lambat dan memerlukan sumber daya besar, menjadikanya sulit di selesaikan 

)
---

## 8. Kesimpulan
Modular aritmatika adalah dasar utama pada matematika di dalam kriptografi. Yang dilakukan pada ruang bilangan yang terbatas, yang menjadikan hasil enkripsi dan dekripsi menjadi selalu konsisten serta menghasilkan fungsi satu arah yang sangat sulik di balik 

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
