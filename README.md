# 🏛️ SIPADU — Sistem Pengaduan Masyarakat

Aplikasi desktop untuk mengelola pengaduan masyarakat secara digital. Warga dapat mengirimkan pengaduan, memantau statusnya, dan admin dapat mengelola serta memperbarui status pengaduan secara real-time.

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
|----------|-----------|
| Bahasa | Python 3.8+ |
| GUI | Tkinter (built-in) |
| Database | SQLite 3 (built-in) |
| Arsitektur | MVC (Model-View-Controller) |
| Version Control | Git & GitHub |

> Tidak memerlukan instalasi library eksternal — semua dependensi sudah bawaan Python.

---

## 🚀 Cara Menjalankan

```bash
# 1. Clone repository
git clone https://github.com/auranfata/sistem-pengaduan.git
cd sistem-pengaduan

# 2. Checkout ke branch dev
git checkout dev

# 3. Jalankan aplikasi
python main.py
```

Database `pengaduan.db` akan dibuat otomatis saat pertama kali dijalankan.

**Akun default admin:** `admin` / `admin123`

---

## 🗂️ Struktur Proyek

```
sistem-pengaduan/
│
├── main.py                          # Entry point aplikasi
├── database.py                      # Koneksi & inisialisasi SQLite
│
├── models/
│   ├── user_model.py                # CRUD tabel users
│   └── pengaduan_model.py           # CRUD tabel pengaduan
│
├── controllers/
│   ├── auth_controller.py           # Logika login & registrasi
│   └── pengaduan_controller.py      # Logika bisnis pengaduan
│
├── views/
│   ├── login_view.py                # Halaman login & registrasi
│   ├── dashboard_view.py            # Shell navigasi utama
│   ├── form_pengaduan_view.py       # Form kirim pengaduan
│   └── list_pengaduan_view.py       # Daftar & detail pengaduan
│
├── utils/
│   └── helpers.py                   # Warna, font, komponen UI bersama
│
├── requirements.txt
└── README.md
```

---

## ✨ Fitur Aplikasi

### 👤 Role: Warga
- Registrasi akun baru
- Login ke sistem
- Mengirim pengaduan baru (judul, kategori, deskripsi)
- Memantau daftar pengaduan sendiri beserta status terkini

### 🔑 Role: Admin
- Login ke sistem
- Melihat seluruh pengaduan dari semua warga
- Mengubah status pengaduan (Menunggu → Diproses → Selesai)
- Menghapus pengaduan

### Kategori Pengaduan
`Infrastruktur` · `Kebersihan` · `Keamanan` · `Pelayanan Publik` · `Lainnya`

---

## 👨‍👩‍👧‍👦 Anggota Kelompok 1

| No | Nama | NIM |
|----|------|-----|
| 1 | Ahmad Rifqi | 240511057 |
| 2 | Auran Fata Mohammad | 240511173 |
| 3 | Dimas Herdiansyah R | 240511138 |
| 4 | Syifa Dwi Aryeni | 240511109 |
| 5 | Heru Prasetyo | 240511133 |

---

## 📋 Pembagian Tugas

| Nama | File yang Dikerjakan |
|------|----------------------|
| Auran Fata Mohammad | `main.py`, setup repo, integrasi akhir |
| Ahmad Rifqi | `database.py`, `models/pengaduan_model.py` |
| Dimas Herdiansyah R | `models/user_model.py`, `controllers/auth_controller.py` |
| Syifa Dwi Aryeni | `views/login_view.py`, `views/dashboard_view.py` |
| Heru Prasetyo | `views/form_pengaduan_view.py`, `views/list_pengaduan_view.py` |

> `controllers/pengaduan_controller.py` dan `utils/helpers.py` dikerjakan bersama.

---

## 🌿 Alur Kerja Git

```bash
# Clone & masuk ke branch dev (sekali saja)
git clone https://github.com/auranfata/sistem-pengaduan.git
cd sistem-pengaduan
git checkout dev

# Sebelum mulai kerja — selalu pull dulu
git pull origin dev

# Setelah selesai edit file bagian masing-masing
git add <nama-file>
git commit -m "feat: deskripsi singkat"
git push origin dev
```

---

*Tugas Mata Kuliah Pemrograman Berorientasi Objek — Teknik Informatika, Universitas Muhammadiyah Cirebon*
