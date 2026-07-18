import tkinter as tk
from tkinter import ttk
from controllers.pengaduan_controller import (
    get_pengaduan_warga, get_semua_pengaduan,
    get_detail, ubah_status, hapus
)
from utils.helpers import (
    WARNA, FONT, STATUS_WARNA, tampil_pesan,
    buat_tombol, tengahkan_window
)


class ListPengaduanView(tk.Frame):
    """
    Digunakan oleh warga (hanya miliknya) dan admin (semua).
    `mode` : 'warga' | 'admin'
    """

    def __init__(self, parent, user: dict, mode: str = "warga"):
        super().__init__(parent, bg=WARNA["bg"])
        self.user = user
        self.mode = mode
        self._bangun_ui()
        self.refresh()

    def _bangun_ui(self):
        # ── Toolbar ──────────────────────────────────────────────────────────
        toolbar = tk.Frame(self, bg=WARNA["bg"], pady=8)
        toolbar.pack(fill="x", padx=20)

        label_teks = ("📋 Semua Pengaduan" if self.mode == "admin"
                      else "📋 Pengaduan Saya")
        tk.Label(toolbar, text=label_teks, font=FONT["sub"],
                 bg=WARNA["bg"], fg=WARNA["primer"]).pack(side="left")

        buat_tombol(toolbar, "🔄 Refresh", self.refresh,
                    WARNA["sekunder"], lebar=10).pack(side="right")

        # ── Tabel ────────────────────────────────────────────────────────────
        frame_tabel = tk.Frame(self, bg=WARNA["bg"], padx=20)
        frame_tabel.pack(fill="both", expand=True, pady=(0, 12))

        kolom = self._kolom()
        self.tree = ttk.Treeview(frame_tabel, columns=kolom,
                                  show="headings", height=14)
        self._setup_kolom(kolom)

        # Scrollbar
        sb = ttk.Scrollbar(frame_tabel, orient="vertical",
                            command=self.tree.yview)
        self.tree.configure(yscrollcommand=sb.set)
        self.tree.pack(side="left", fill="both", expand=True)
        sb.pack(side="right", fill="y")

        # Klik baris → buka detail
        self.tree.bind("<Double-1>", self._buka_detail)

        # Styling baris berdasarkan status
        for status, warna in STATUS_WARNA.items():
            self.tree.tag_configure(status, foreground=warna)

    def _kolom(self):
        if self.mode == "admin":
            return ("ID", "Pelapor", "Judul", "Kategori", "Status", "Tanggal")
        return ("ID", "Judul", "Kategori", "Status", "Tanggal")

    def _setup_kolom(self, kolom):
        lebar = {
            "ID": 40, "Pelapor": 120, "Judul": 200,
            "Kategori": 110, "Status": 80, "Tanggal": 140
        }
        for k in kolom:
            self.tree.heading(k, text=k)
            self.tree.column(k, width=lebar.get(k, 100), anchor="w")

    def refresh(self):
        """Mengambil ulang data dari controller lalu render ke tabel."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        if self.mode == "admin":
            data = get_semua_pengaduan()
            for baris in data:
                status = baris["status"]
                self.tree.insert("", "end", values=(
                    baris["id"], baris["nama"], baris["judul"],
                    baris["kategori"], status, baris["tanggal"]
                ), tags=(status,))
        else:
            data = get_pengaduan_warga(self.user["id"])
            for baris in data:
                status = baris["status"]
                self.tree.insert("", "end", values=(
                    baris["id"], baris["judul"],
                    baris["kategori"], status, baris["tanggal"]
                ), tags=(status,))

    def _buka_detail(self, event):
        item = self.tree.focus()
        if not item:
            return
        values = self.tree.item(item, "values")
        pengaduan_id = int(values[0])
        DetailPengaduanPopup(self, pengaduan_id, self.mode, self.refresh)


class DetailPengaduanPopup(tk.Toplevel):
    """Popup detail lengkap satu pengaduan + aksi admin."""

    def __init__(self, parent, pengaduan_id: int,
                 mode: str, on_refresh=None):
        super().__init__(parent)
        self.pengaduan_id = pengaduan_id
        self.mode         = mode
        self.on_refresh   = on_refresh

        data = get_detail(pengaduan_id)
        if not data:
            tampil_pesan("Error", "Data tidak ditemukan.", "error")
            self.destroy()
            return

        self.data = dict(data)
        self.title(f"Detail Pengaduan #{pengaduan_id}")
        self.configure(bg=WARNA["bg"])
        self.resizable(False, False)
        tengahkan_window(self, 480, 420)
        self.grab_set()
        self._bangun_ui()

    def _bangun_ui(self):
        d = self.data
        header = tk.Frame(self, bg=WARNA["primer"], pady=10)
        header.pack(fill="x")
        tk.Label(header, text=f"#{d['id']} — {d['judul']}",
                 font=FONT["sub"], bg=WARNA["primer"],
                 fg=WARNA["putih"], wraplength=440).pack(padx=16)

        body = tk.Frame(self, bg=WARNA["bg"], padx=20, pady=12)
        body.pack(fill="both", expand=True)

        def baris_info(label, nilai, warna_nilai=None):
            f = tk.Frame(body, bg=WARNA["bg"])
            f.pack(fill="x", pady=2)
            tk.Label(f, text=f"{label}:", font=FONT["kecil"],
                     bg=WARNA["bg"], fg=WARNA["abu"], width=14,
                     anchor="w").pack(side="left")
            tk.Label(f, text=nilai, font=FONT["normal"],
                     bg=WARNA["bg"],
                     fg=warna_nilai or WARNA["teks"]).pack(side="left")

        baris_info("Pelapor",  d.get("nama_pelapor", "-"))
        baris_info("Kategori", d["kategori"])
        baris_info("Tanggal",  d["tanggal"])
        baris_info("Status",   d["status"],
                   STATUS_WARNA.get(d["status"], WARNA["teks"]))

        tk.Label(body, text="Deskripsi:", font=FONT["kecil"],
                 bg=WARNA["bg"], fg=WARNA["abu"]).pack(anchor="w", pady=(8, 2))
        txt = tk.Text(body, font=FONT["normal"], height=6,
                      relief="solid", bd=1, wrap="word", state="normal")
        txt.insert("1.0", d["deskripsi"])
        txt.config(state="disabled")
        txt.pack(fill="x")

        # Aksi admin
        if self.mode == "admin":
            self._panel_admin(body)

    def _panel_admin(self, parent):
        panel = tk.Frame(parent, bg=WARNA["bg"], pady=10)
        panel.pack(fill="x")

        tk.Label(panel, text="Ubah Status:", font=FONT["kecil"],
                 bg=WARNA["bg"], fg=WARNA["teks"]).pack(side="left", padx=(0, 6))

        self.combo_status = ttk.Combobox(
            panel,
            values=["Menunggu", "Diproses", "Selesai"],
            state="readonly", width=14, font=FONT["normal"]
        )
        self.combo_status.set(self.data["status"])
        self.combo_status.pack(side="left", padx=(0, 8))

        buat_tombol(panel, "✔ Simpan", self._simpan_status,
                    WARNA["sukses"], lebar=10).pack(side="left", padx=(0, 6))
        buat_tombol(panel, "🗑 Hapus", self._hapus_pengaduan,
                    WARNA["bahaya"], lebar=8).pack(side="left")

    def _simpan_status(self):
        status_baru = self.combo_status.get()
        sukses, pesan = ubah_status(self.pengaduan_id, status_baru)
        tampil_pesan("Status", pesan, "info" if sukses else "error")
        if sukses and self.on_refresh:
            self.on_refresh()
        self.destroy()

    def _hapus_pengaduan(self):
        from tkinter import messagebox
        konfirm = messagebox.askyesno(
            "Konfirmasi", "Yakin ingin menghapus pengaduan ini?"
        )
        if konfirm:
            hapus(self.pengaduan_id)
            tampil_pesan("Berhasil", "Pengaduan dihapus.")
            if self.on_refresh:
                self.on_refresh()
            self.destroy()
