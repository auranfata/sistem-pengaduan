import tkinter as tk
from tkinter import ttk
from controllers.pengaduan_controller import kirim_pengaduan, KATEGORI_VALID
from utils.helpers import WARNA, FONT, tampil_pesan, buat_tombol


class FormPengaduanView(tk.Frame):
    """
    Frame yang ditanamkan ke dalam DashboardView (warga).
    Menerima `user` dict dan `on_selesai` callback untuk refresh list.
    """

    def __init__(self, parent, user: dict, on_selesai=None):
        super().__init__(parent, bg=WARNA["bg"])
        self.user       = user
        self.on_selesai = on_selesai  # dipanggil setelah berhasil kirim
        self._bangun_ui()

    def _bangun_ui(self):
        # ── Judul ────────────────────────────────────────────────────────────
        tk.Label(self, text="📝 Buat Pengaduan Baru",
                 font=FONT["sub"], bg=WARNA["bg"],
                 fg=WARNA["primer"]).pack(anchor="w", padx=20, pady=(16, 8))

        card = tk.Frame(self, bg=WARNA["putih"],
                        padx=20, pady=16, relief="groove", bd=1)
        card.pack(fill="both", expand=True, padx=20, pady=(0, 16))

        # Judul Pengaduan
        tk.Label(card, text="Judul Pengaduan *", font=FONT["kecil"],
                 bg=WARNA["putih"], fg=WARNA["teks"]).grid(
                     row=0, column=0, sticky="w", pady=(0, 2))
        self.entry_judul = ttk.Entry(card, font=FONT["normal"], width=50)
        self.entry_judul.grid(row=1, column=0, columnspan=2,
                               sticky="ew", pady=(0, 10))

        # Kategori
        tk.Label(card, text="Kategori *", font=FONT["kecil"],
                 bg=WARNA["putih"], fg=WARNA["teks"]).grid(
                     row=2, column=0, sticky="w", pady=(0, 2))
        self.combo_kategori = ttk.Combobox(
            card,
            values=KATEGORI_VALID,
            state="readonly",
            font=FONT["normal"],
            width=28,
        )
        self.combo_kategori.current(0)
        self.combo_kategori.grid(row=3, column=0, sticky="w", pady=(0, 10))

        # Deskripsi
        tk.Label(card, text="Deskripsi Lengkap *", font=FONT["kecil"],
                 bg=WARNA["putih"], fg=WARNA["teks"]).grid(
                     row=4, column=0, sticky="w", pady=(0, 2))
        self.text_deskripsi = tk.Text(
            card, font=FONT["normal"], width=50, height=8,
            relief="solid", bd=1, wrap="word"
        )
        self.text_deskripsi.grid(row=5, column=0, columnspan=2,
                                  sticky="ew", pady=(0, 16))
        card.columnconfigure(0, weight=1)

        # Tombol
        baris_btn = tk.Frame(card, bg=WARNA["putih"])
        baris_btn.grid(row=6, column=0, columnspan=2, sticky="e")

        buat_tombol(baris_btn, "🗑 Bersihkan",
                    self._bersihkan, WARNA["abu"]).pack(side="left", padx=(0, 8))
        buat_tombol(baris_btn, "📤 Kirim Pengaduan",
                    self._kirim, WARNA["primer"]).pack(side="left")

    def _kirim(self):
        judul      = self.entry_judul.get().strip()
        deskripsi  = self.text_deskripsi.get("1.0", "end").strip()
        kategori   = self.combo_kategori.get()

        sukses, pesan = kirim_pengaduan(
            self.user["id"], judul, deskripsi, kategori
        )

        tampil_pesan(
            "Berhasil" if sukses else "Gagal",
            pesan,
            "info" if sukses else "error"
        )

        if sukses:
            self._bersihkan()
            if self.on_selesai:
                self.on_selesai()  # refresh list pengaduan

    def _bersihkan(self):
        self.entry_judul.delete(0, "end")
        self.text_deskripsi.delete("1.0", "end")
        self.combo_kategori.current(0)
        self.entry_judul.focus()
