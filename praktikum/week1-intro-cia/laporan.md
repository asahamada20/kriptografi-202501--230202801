# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: Sejarah Kriptografi dan Prinsip CIA
Nama: Asadila Haila Hamada
NIM: 230202801  
Kelas: 5 IKRA

---

## 1. Tujuan
1. Mengetahui sejarah dan fungsi dari kriptografi
2. Mempelajari prinsip CIA
3. Menyimpulkan fungsi kriptografi di sistem keamanan modern 

---

## 2. Dasar Teori
Kriptografi berasal dari bahasa yunani kryptos dan graphein, kryptos yang mengartikan rahasi, sedangankan graphien yang mengartikan menulis. Secara umum kriptogafi adalah ilmu dan seni untuk mengamankan infomasi dengan cara mengubah data menjadi bentuk yang tidak dapat dibaca secara langsung, melainkan pembaca harus mengetahui key dan metode yang digunakan dalam pembuatanya. Tujuanya adalahmelindungi pesan agar tidak dapat dibaca, diubah, atau dipalsukan oleh pihak yang tidak berwenang.

Di dalam kriptografi memiliki beberapa komponen, yaitu:
1. Plaintext - pesan asli yang belum di ubah atau masih asli
2. Chipertect - pesan yang sudah di samarkan agar tidak mudah dibaca dan diubah
3. Enkripsi - adalah proses pengubahan Plaintext ( pesan asli ) menjadi Chipertext ( pesan yang sudah di ubah )
4. Dekripsi - adalah proses pengembalian dari Chipertext menjadi Plaintext
5. Kunci - nilai rahasia yang digunakan dalam proses enkripsi dan deksripsi

Kriptografi memiliki beberapa jenis, yaitu:
1. Kriptografi simetris - menggunakan satu kunci untuk enkripsi dan dekripsi
   Conrtoh: AES, DES
2. Kriptografi asimetris - menggunakan 2 kunvci berbeda yaitu kunci publik dan kunci private
   Contoh: RSA, ECC
3. Kriptografi hash - mengubah data menjadi nilai unik dengan panjang tetap yang biasa digunakan untuk memverifikasi integritas data
   Contoh: SHA, MDS

Prinsip CIA merupakan konsep dasar dalam pembuatan keamanan informasi, yang terdiri dari 3 prinsip utama yang saling melengkapi
1. Kerahasiaan - menjamin bahwa informasi hanya dapat di akses oleh pihak yang berhak
2. Integritas - menjamin bahwa informasi tidak diubah, dirusakm atau dimodifikasi tanpa izin
3. Ketersediaan - menjamin bahwa indormasi dan sistem selalu dapat diakses saat dibutuhkan
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
import string
import random

def generate_substitution_key(seed=None):
    letters = list(string.ascii_lowercase)
    shuffled = letters.copy()
    if seed is not None:
        random.seed(seed)
    random.shuffle(shuffled)
    enc_map = {a: b for a, b in zip(letters, shuffled)}
    dec_map = {b: a for a, b in zip(letters, shuffled)}
    return enc_map, dec_map

def encrypt(text, enc_map):
    result = []
    for ch in text:
        low = ch.lower()
        if low in enc_map:
            cipher = enc_map[low]
            result.append(cipher.upper() if ch.isupper() else cipher)
        else:
            result.append(ch)
    return ''.join(result)

def decrypt(ciphertext, dec_map):
    result = []
    for ch in ciphertext:
        low = ch.lower()
        if low in dec_map:
            plain = dec_map[low]
            result.append(plain.upper() if ch.isupper() else plain)
        else:
            result.append(ch)
    return ''.join(result)

# =======================
# Program Utama
# =======================
print("=== Program Kriptografi Sederhana ===")
text = input("Masukkan kata atau kalimat: ")

# kamu bisa ubah angka seed untuk hasil berbeda
seed = 42  
enc_map, dec_map = generate_substitution_key(seed)

ciphertext = encrypt(text, enc_map)
plaintext = decrypt(ciphertext, dec_map)

print("\nHasil Enkripsi :", ciphertext)
print("Hasil Dekripsi :", plaintext)

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
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?
   Tokoh yang dianggap sebagai Bapak Kriptografi Modern adalah Claude E. Shannon

2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
   - RSA ( Rivest Shamir Adleman ) - algoritma yang paling terkenal yang digunakan di SSL/TLS, email, VPN yang berufngsi untuk enkripsi & tanda tangan digital
   - ECC ( Elliptic Curve Cryptographhy ) - algoritma yang lebih efisieb dari pada RSA dengan kunci yang lebih kecil fungsinya antara lain enkripsi & autentikasi
   - Diffle Hellman ( DH ) - algortima yang digunakan untuk dasar dari banyak protokol keamanan seperti HTTPS
     
3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?
    Perbedaan dari kriptogradi klasik dan kriptigradi modren terletelak pada metode dan tingkat keamananya. kriptografi klasik menggunakan teknik sederhana seperti substitusi dan transportasi huruf dengan satu kunci yang sama, menjadikan kriptografi klasik mudah dipecahkan dengan analisis frekuensi. Sedangakan kriptogradi modern menggunakan algoritma matematika yang kompleks serta dapat menggunakan 2 kunci berbeda, contohnya seperti RSA dan AES, sehingga lebih aman dan cocok digunakan dalam sistem digital serta jaringan komputer saat ini
   
## 8. Kesimpulan
kriptografi merupakan dasar dari sebuah keamanan digital modren yang berfungsi untuk melindungi informasi agar hanya dapat di akses oleh pihak berwenang. Proses ini dilakukan melalui enkripsi (mengubah pesan menjadi bentuk tidak terbaca) dan dekripsi (mengembalikannya ke bentuk semula). Saat ini, kriptografi tidak hanya melindungi kerahasiaan pesan, tetapi juga menjamin keaslian (authenticity), integritas data, dan non-repudiation atau keabsahan pengirim. Teknologi ini diterapkan luas dalam transaksi perbankan online, email aman, autentikasi media sosial, hingga layanan cloud, dengan algoritma populer seperti RSA, AES, dan SHA.
Kesimpulannya, kriptografi tidak sekadar menyembunyikan pesan, tetapi menjadi kunci utama dalam menjaga keamanan dan kepercayaan digital di era modern.

---

## 9. Daftar Pustaka
Sistem Kriptografi pada Pengamanan Autentikasi Dokumen Elektronik: Systematic Literature Review - 2023

---

## 10. Commit Log


commit abc12345
Author: Asadila Haila Hamada
Date:   2025-10-11
week1-cryptosystem: Sejarah kriptografi & prinsip CIA

   

