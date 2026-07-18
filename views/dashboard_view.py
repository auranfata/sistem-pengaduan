import tkinter as tk
from tkinter import ttk
from utils.helpers import WARNA, FONT, buat_tombol, tengahkan_window
from views.form_pengaduan_view import FormPengaduanView
from views.list_pengaduan_view import ListPengaduanView


class DashboardView(tk.Tk):
    """
    Jendela utama setelah login.
    Layout: sidebar kiri + area konten kanan.
    """

    def __init__(self, user: dict):
        super().__init__()
        self.user         = user
        self.frame_aktif  = None  # frame konten yang sedang tampil

        self.title(f"SIPADU — {user['nama']} ({user['role'].capitalize()})")
        self.configure(bg=WARNA["bg"])
        tengahkan_window(self, 900, 580)
        self.minsize(800, 500)

        self._bangun_sidebar()
        self._bangun_area_konten()
        self._tampil_halaman_default()

    # ── Sidebar ──────────────────────────────────────────────────────────────
    def _bangun_sidebar(self):
        self.sidebar = tk.Frame(self, bg=WARNA["primer"], width=190)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)

        # Logo / nama app
        tk.Label(self.sidebar, text="🏛️ SIPADU",
                 font=("Segoe UI", 14, "bold"),
                 bg=WARNA["primer"], fg=WARNA["putih"],
                 pady=20).pack()

        tk.Frame(self.sidebar, bg="#2e5a80", height=1).pack(fill="x", padx=16)

        # Info user
        tk.Label(self.sidebar, text=self.user["nama"],
                 font=FONT["normal"], bg=WARNA["primer"],
                 fg="#cde", wraplength=160).pack(pady=(10, 2))
        tk.Label(self.sidebar, text=self.user["role"].capitalize(),
                 font=FONT["kecil"], bg=WARNA["primer"],
                 fg=WARNA["aksen"]).pack(pady=(0, 14))

        tk.Frame(self.sidebar, bg="#2e5a80", height=1).pack(fill="x", padx=16)

        # Menu navigasi berdasarkan role
        menu_items = self._menu_items()
        for label, perintah in menu_items:
            btn = tk.Button(
                self.sidebar, text=label,
                command=perintah,
                bg=WARNA["primer"], fg=WARNA["putih"],
                font=FONT["normal"], relief="flat",
                cursor="hand2", anchor="w", padx=20, pady=10
            )
            btn.pack(fill="x")
            btn.bind("<Enter>", lambda e, b=btn: b.config(bg=WARNA["sekunder"]))
            btn.bind("<Leave>", lambda e, b=btn: b.config(bg=WARNA["primer"]))

        # Tombol Logout di bawah
        tk.Frame(self.sidebar, bg=WARNA["primer"]).pack(expand=True)
        tk.Button(
            self.sidebar, text="⏻  Keluar",
            command=self._logout,
            bg=WARNA["bahaya"], fg=WARNA["putih"],
            font=FONT["normal"], relief="flat",
            cursor="hand2", pady=8
        ).pack(fill="x", padx=16, pady=16)

    def _menu_items(self):
        """Mengembalikan pasangan (label, callback) sesuai role."""
        if self.user["role"] == "admin":
            return [
                ("📋  Semua Pengaduan", self._halaman_list_admin),
            ]
        else:  # warga
            return [
                ("📝  Buat Pengaduan",  self._halaman_form),
                ("📋  Pengaduan Saya",  self._halaman_list_warga),
            ]

    # ── Area Konten ──────────────────────────────────────────────────────────
    def _bangun_area_konten(self):
        self.area_konten = tk.Frame(self, bg=WARNA["bg"])
        self.area_konten.pack(side="left", fill="both", expand=True)

    def _tampil(self, FrameClass, **kwargs):
        """Mengganti frame konten yang aktif."""
        if self.frame_aktif:
            self.frame_aktif.destroy()
        self.frame_aktif = FrameClass(self.area_konten, **kwargs)
        self.frame_aktif.pack(fill="both", expand=True)

    # ── Navigasi ─────────────────────────────────────────────────────────────
    def _tampil_halaman_default(self):
        if self.user["role"] == "admin":
            self._halaman_list_admin()
        else:
            self._halaman_list_warga()

    def _halaman_form(self):
        self._tampil(
            FormPengaduanView,
            user=self.user,
            on_selesai=self._halaman_list_warga
        )

    def _halaman_list_warga(self):
        self._tampil(ListPengaduanView, user=self.user, mode="warga")

    def _halaman_list_admin(self):
        self._tampil(ListPengaduanView, user=self.user, mode="admin")

    # ── Logout ───────────────────────────────────────────────────────────────
    def _logout(self):
        self.destroy()
        # Re-import di sini untuk menghindari circular import
        from views.login_view import LoginView
        from views.dashboard_view import DashboardView

        def on_login(user):
            DashboardView(user).mainloop()

        LoginView(on_login).mainloop()
