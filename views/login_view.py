"""
views/login_view.py
--------------------
KONTRIBUTOR : Anggota D
BRANCH      : feature/login-view
TUGAS       : Tampilan halaman Login dan Register
"""

import tkinter as tk
from tkinter import ttk
from controllers.auth_controller import login, register
from utils.helpers import WARNA, FONT, tampil_pesan, tengahkan_window


class LoginView(tk.Tk):
    """Jendela utama untuk Login."""

    def __init__(self, on_login_sukses):
        super().__init__()
        self.on_login_sukses = on_login_sukses  # callback → dipanggil saat login berhasil
        self.title("Sistem Pengaduan Masyarakat — Login")
        self.configure(bg=WARNA["bg"])
        self.resizable(False, False)
        tengahkan_window(self, 420, 480)
        self._bangun_ui()

    def _bangun_ui(self):
        # ── Header ──────────────────────────────────────────────────────────
        header = tk.Frame(self, bg=WARNA["primer"], pady=20)
        header.pack(fill="x")
        tk.Label(header, text="🏛️ SIPADU", font=("Segoe UI", 22, "bold"),
                 bg=WARNA["primer"], fg=WARNA["putih"]).pack()
        tk.Label(header, text="Sistem Pengaduan Masyarakat",
                 font=FONT["kecil"], bg=WARNA["primer"],
                 fg="#a8c8e8").pack()

        # ── Form ─────────────────────────────────────────────────────────────
        frame = tk.Frame(self, bg=WARNA["bg"], padx=40, pady=30)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Username", font=FONT["normal"],
                 bg=WARNA["bg"], fg=WARNA["teks"]).pack(anchor="w")
        self.entry_username = ttk.Entry(frame, font=FONT["normal"], width=30)
        self.entry_username.pack(fill="x", pady=(2, 12))

        tk.Label(frame, text="Password", font=FONT["normal"],
                 bg=WARNA["bg"], fg=WARNA["teks"]).pack(anchor="w")
        self.entry_password = ttk.Entry(frame, font=FONT["normal"],
                                         width=30, show="●")
        self.entry_password.pack(fill="x", pady=(2, 20))

        # Tombol Login
        tk.Button(
            frame, text="Masuk", command=self._proses_login,
            bg=WARNA["primer"], fg=WARNA["putih"],
            font=FONT["sub"], relief="flat", cursor="hand2", pady=8
        ).pack(fill="x", pady=(0, 8))

        # Link ke Register
        tk.Button(
            frame, text="Belum punya akun? Daftar di sini",
            command=self._buka_register,
            bg=WARNA["bg"], fg=WARNA["sekunder"],
            font=FONT["kecil"], relief="flat", cursor="hand2", bd=0
        ).pack()

        # Bind Enter
        self.bind("<Return>", lambda e: self._proses_login())
        self.entry_username.focus()

    def _proses_login(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()
        user, pesan_error = login(username, password)

        if user:
            self.destroy()
            self.on_login_sukses(user)
        else:
            tampil_pesan("Login Gagal", pesan_error, "error")

    def _buka_register(self):
        RegisterView(self)


class RegisterView(tk.Toplevel):
    """Dialog popup untuk Registrasi akun warga baru."""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Daftar Akun Baru")
        self.configure(bg=WARNA["bg"])
        self.resizable(False, False)
        tengahkan_window(self, 400, 420)
        self.grab_set()  # modal
        self._bangun_ui()

    def _bangun_ui(self):
        header = tk.Frame(self, bg=WARNA["sekunder"], pady=14)
        header.pack(fill="x")
        tk.Label(header, text="Daftar Akun Warga", font=FONT["sub"],
                 bg=WARNA["sekunder"], fg=WARNA["putih"]).pack()

        frame = tk.Frame(self, bg=WARNA["bg"], padx=30, pady=20)
        frame.pack(fill="both", expand=True)

        fields = [
            ("Nama Lengkap", False),
            ("Username",     False),
            ("Password",     True),
            ("Konfirmasi Password", True),
        ]
        self.entries = {}
        for label, is_pass in fields:
            tk.Label(frame, text=label, font=FONT["kecil"],
                     bg=WARNA["bg"], fg=WARNA["teks"]).pack(anchor="w")
            ent = ttk.Entry(frame, font=FONT["normal"],
                            show="●" if is_pass else "")
            ent.pack(fill="x", pady=(2, 8))
            self.entries[label] = ent

        tk.Button(
            frame, text="Daftar Sekarang", command=self._proses_register,
            bg=WARNA["sukses"], fg=WARNA["putih"],
            font=FONT["normal"], relief="flat", cursor="hand2", pady=6
        ).pack(fill="x", pady=(8, 0))

        self.entries["Nama Lengkap"].focus()

    def _proses_register(self):
        nama      = self.entries["Nama Lengkap"].get().strip()
        username  = self.entries["Username"].get().strip()
        password  = self.entries["Password"].get()
        konfirmasi = self.entries["Konfirmasi Password"].get()

        sukses, pesan = register(nama, username, password, konfirmasi)

        if sukses:
            tampil_pesan("Berhasil", pesan, "info")
            self.destroy()
        else:
            tampil_pesan("Gagal", pesan, "error")
