# Laporan Praktikum Kriptografi
Minggu ke-: 15
Topik: Proyek Kelompok – TinyCoin ERC20  
Nama: Asadila Haila Hamada  
NIM: 230202801 
Kelas: 5IKRA  

---

## 1. Tujuan
1. Mengembangkan proyek sederhana berbasis algoritma kriptografi.
2. Mendokumentasikan proses implementasi proyek ke dalam repository Git.
3. Menyusun laporan teknis hasil proyek akhir.


---

## 2. Dasar Teori
TinyCoin ERC20 adalah proyek token digital yang dibangun di atas standar ERC20 pada jaringan ETH. Dasar dteorinya yaitu pembuatan token kriptografi yang dapat dipertukarkan secara digital dengan fungsi standar seperti transfer, saldo, dan persetujuan transaksi

---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
# Langkah 1 — Membuat Kontrak ERC20
Contoh kontrak sederhana TinyCoin.sol:

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}

# Langkah 2 — Deploy Kontrak
Buka Remix IDE → buat file TinyCoin.sol.
Kompilasi dengan Solidity Compiler.
Deploy ke jaringan JavaScript VM atau testnet Ethereum.
Catat alamat kontrak hasil deployment.

# Langkah 3 — Uji Fungsionalitas
Cek saldo awal dengan fungsi balanceOf(address).
Lakukan transfer token dengan fungsi transfer(address, amount).
Uji apakah total supply tetap konsisten setelah transaksi.

# Langkah 4 — Dokumentasi
Simpan tangkapan layar proses deployment & transaksi.
Dokumentasikan alur kontrak (fungsi utama: constructor, mint, transfer).
Tambahkan analisis singkat tentang potensi keamanan smart contract (contoh: reentrancy, overflow – walaupun mitigasi sudah ada di Solidity >=0.8).

---

## 5. Source Code
```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }
}
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
1. FUngsi ERC20 adalah menetapkan standar protokol bagi token di blockcahin ETH sehingga token dari berbagai proyek dapat saling kompatibel dan mudah diperdagangkan
2. Mekanisme transfer token dalam ERC20 beerja dengan memanggil fungsi transfer yang mengurangi saldo pengirim dan menambah saldo penerima dan kemudian memancarkan event transfer untuk transparansi dan pelacakan
3. Resiko utaman smart contracr adalah bug kode, celah keamanan dan kerentanan ekspolitasi

---

## 8. Kesimpulan
TinyCoin ERC20 adalah token digital berbasis standar ERC20 Ethereum yang memungkinkan transaksi dan pengelolaan token secara aman dan transparan melalui smart contract, memanfaatkan fitur interoperabilitas dan automasi dalam ekosistem blockchain.

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
