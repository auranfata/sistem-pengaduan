# 🏛️ SIPADU — Sistem Pengaduan Masyarakat

> Aplikasi GUI desktop berbasis Python (Tkinter + SQLite) dengan arsitektur MVC.

---

## 🚀 Cara Menjalankan

```bash
# 1. Clone repository
git clone https://github.com/auranfata/sistem-pengaduan.git
cd sistem-pengaduan

# 2. Pastikan Python 3.8+ terinstall
python --version

# 3. Jalankan aplikasi (database otomatis dibuat)
python main.py
```

**Akun default:** `admin` / `admin123`

---

## 👥 Pembagian Tugas Tim

| Anggota | File yang Dikerjakan | Branch |
|---------|----------------------|--------|
| **Lead (Auran)** | `main.py`, review PR, merge ke `dev` | `main` / `dev` |
| **Anggota A** | `database.py`, `models/pengaduan_model.py` | `feature/database-setup`, `feature/pengaduan-model` |
| **Anggota B** | `models/user_model.py`, `controllers/auth_controller.py` | `feature/auth` |
| **Anggota C** | `controllers/pengaduan_controller.py` | `feature/pengaduan-controller` |
| **Anggota D** | `views/login_view.py`, `views/dashboard_view.py` | `feature/login-view`, `feature/dashboard-view` |
| **Anggota E** | `views/form_pengaduan_view.py`, `views/list_pengaduan_view.py` | `feature/form-pengaduan`, `feature/list-pengaduan` |

---

## 🌿 Alur Kerja Git (Wajib Diikuti Semua Anggota)

### Setup Awal (lakukan SEKALI)
```bash
git clone https://github.com/<nama-org>/sistem-pengaduan.git
cd sistem-pengaduan
git checkout dev
```

### Siklus Harian
```bash
# 1. Selalu pull dulu sebelum mulai kerja
git checkout dev
git pull origin dev

# 2. Buat/pindah ke branch fiturmu
git checkout -b feature/nama-fiturmu
# (jika branch sudah ada)
git checkout feature/nama-fiturmu

# 3. Kerjakan file kamu

# 4. Commit dengan pesan yang jelas
git add .
git commit -m "feat: tambah validasi form pengaduan"

# 5. Push ke GitHub
git push origin feature/nama-fiturmu

# 6. Buat Pull Request ke branch dev di GitHub
#    Minta Lead untuk review & merge
```

### Konvensi Pesan Commit
```
feat: fitur baru
fix: perbaikan bug
style: perubahan tampilan
refactor: refaktor kode
docs: update dokumentasi
```

---

## 🗂️ Struktur Proyek

```
sistem-pengaduan/
├── main.py                      # Entry point
├── database.py                  # Koneksi & inisialisasi SQLite
├── models/
│   ├── user_model.py            # CRUD tabel users
│   └── pengaduan_model.py       # CRUD tabel pengaduan
├── controllers/
│   ├── auth_controller.py       # Logika login & register
│   └── pengaduan_controller.py  # Logika pengaduan
├── views/
│   ├── login_view.py            # Halaman login & register
│   ├── dashboard_view.py        # Shell navigasi utama
│   ├── form_pengaduan_view.py   # Form kirim pengaduan
│   └── list_pengaduan_view.py   # Daftar & detail pengaduan
├── utils/
│   └── helpers.py               # Warna, font, komponen UI bersama
├── requirements.txt
└── README.md
```

---

## 📋 Fitur Aplikasi

### Role: Warga
- ✅ Register akun baru
- ✅ Login
- ✅ Kirim pengaduan (judul, kategori, deskripsi)
- ✅ Lihat daftar pengaduan sendiri + status terkini

### Role: Admin
- ✅ Login
- ✅ Lihat semua pengaduan dari semua warga
- ✅ Ubah status pengaduan (Menunggu → Diproses → Selesai)
- ✅ Hapus pengaduan

---

## ⚠️ Aturan File

- **Jangan edit file orang lain** tanpa diskusi dulu
- **`pengaduan.db`** sudah masuk `.gitignore` — tidak perlu di-push
- Selalu `git pull` sebelum mulai kerja

---

## 📞 Kontak Lead

Hubungi Auran jika ada konflik merge atau kebingungan tentang integrasi.
