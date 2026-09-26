# Tugas1-Kriptografi

SOAL KRIPTOGRAFI KLASIK - PERSONAL
Nama : ANDRE ASTAMAM
NIM  : F1D02410103

Catatan: soal ini dibuat unik untuk Anda berdasarkan NIM. Mengerjakan
soal milik teman lain tidak akan menghasilkan jawaban yang benar untuk
soal Anda sendiri, jadi silakan berdiskusi metode dengan teman, tapi
kerjakan angka/kuncinya sendiri.

==============================================================
BAGIAN 1 - CAESAR CIPHER
==============================================================
Berikut adalah sebuah ciphertext hasil enkripsi Caesar Cipher (kunci
geser TIDAK diberikan):

    JREUZ BLEF JVBRCZGLE KVKRG DVERIZB LEKLB UZGVCRARIZ YRIZ ZEZ

Tugas Anda:
  a. Lakukan analisis frekuensi huruf (atau brute-force 25 kemungkinan
     geseran) untuk menemukan kunci geser yang digunakan.
  b. Tuliskan plaintext hasil dekripsi.
(Petunjuk: kunci geser berada di antara 14 dan 20.)

==============================================================
BAGIAN 2 - VIGENERE CIPHER
==============================================================
Berikut adalah sebuah ciphertext hasil enkripsi Vigenere Cipher (kata
kunci TIDAK diberikan):

    CYGKIZ EBNWW XNNIW GNVZSEF XQQYAGZO XNRID XVCVKFVUQC MRRMBNV UIXXV EIOMNT BOLCKAKB

Tugas Anda:
  a. Gunakan Kasiski Examination dan/atau Index of Coincidence untuk
     menduga panjang kata kunci.
  b. Temukan kata kuncinya, lalu tuliskan plaintext hasil dekripsi.
(Petunjuk: panjang kata kunci adalah 5 huruf.)

==============================================================
BAGIAN 3 - ENIGMA MACHINE
==============================================================
Sebuah pesan telah dienkripsi menggunakan mesin Enigma dengan
konfigurasi berikut (konfigurasi ini unik untuk Anda):

  Urutan rotor (kanan ke kiri) : II, I, III
  Ring setting (kanan ke kiri) : G, P, Q
  Posisi awal (kanan ke kiri)  : K, Y, S
  Plugboard                    : A-P, T-V, F-B
  Reflector                    : B (standar)

Ciphertext:
    RWSSKPFJHLGKERLWZMSPOFIZIUJODSQPTAYRYFPRYN

Tugas Anda:
  a. Dekripsikan pesan di atas. Anda boleh mengerjakan manual langkah
     demi langkah, ATAU menulis program (Python/lainnya) yang
     mensimulasikan mesin Enigma sesuai konfigurasi di atas.
  b. Jika Anda menulis program, lampirkan kode sumbernya.

==============================================================
FORMAT PENGUMPULAN
==============================================================
Jawaban dikumpulkan pada file Excel yang telah ditentukan (bukan file
terpisah). Isikan plaintext hasil dekripsi Anda untuk Bagian 1, 2, dan
3 pada baris sesuai NIM Anda di file Excel tersebut.
