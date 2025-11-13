# 🔐 Flask Simple Login App

Aplikasi web sederhana untuk sistem login menggunakan Flask framework. Proyek ini cocok untuk pembelajaran dasar Flask dan autentikasi pengguna.

## ✨ Fitur

- 🚀 Login form sederhana dengan validasi
- ✅ Autentikasi pengguna
- ❌ Pesan error untuk kredensial yang salah
- 🎉 Halaman sukses setelah login berhasil
- 📱 Interface responsif dan user-friendly

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **Flask** - Micro web framework
- **HTML** - Template rendering
- **Jinja2** - Template engine (built-in Flask)

## 📋 Prasyarat

Pastikan kamu sudah menginstall:

- Python 3.x
- pip (Python package manager)

## 🚀 Instalasi

### 1. Clone Repository

```bash
git clone <repository-url>
cd uji_flask
```

### 2. Buat Virtual Environment (Opsional tapi Direkomendasikan)

```bash
python3 -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
```

### 3. Install Dependencies

```bash
pip install flask
```

## 📁 Struktur Proyek

```
uji_flask/
│
├── app.py                 # File utama aplikasi Flask
├── templates/             # Folder untuk template HTML
│   ├── login.html        # Halaman login
│   └── success.html      # Halaman sukses login
└── README.md             # Dokumentasi proyek
```

## ▶️ Cara Menjalankan

1. Pastikan kamu berada di direktori proyek:
```bash
cd ~/uji_flask
```

2. Jalankan aplikasi:
```bash
python3 app.py
```

3. Buka browser dan akses:
```
http://localhost:5000
```

Atau jika menjalankan di server, akses melalui:
```
http://<IP-ADDRESS>:5000
```

## 🔑 Kredensial Login

Untuk testing, gunakan kredensial berikut:

- **Username:** `iqbal`
- **Password:** `12345`

> ⚠️ **Catatan Keamanan:** Ini hanya untuk development/testing. Jangan gunakan kredensial hardcoded di production!

## 📸 Screenshot

### Halaman Login
```
┌─────────────────────────┐
│    Form Login           │
│                         │
│ Username: [________]    │
│ Password: [________]    │
│                         │
│      [Login]            │
└─────────────────────────┘
```

### Halaman Sukses
```
┌─────────────────────────┐
│ Selamat datang, Iqbal! 🎉│
│ Login berhasil!         │
└─────────────────────────┘
```

## 🔧 Konfigurasi

Aplikasi berjalan pada:
- **Host:** `0.0.0.0` (accessible dari network)
- **Port:** `5000`

Untuk mengubah konfigurasi, edit bagian ini di `app.py`:
```python
app.run(host='0.0.0.0', port=5000)
```

## 🎯 Pengembangan Selanjutnya

Beberapa ide untuk improvement:

- [ ] Implementasi database untuk menyimpan user
- [ ] Hash password dengan bcrypt
- [ ] Session management dengan Flask-Login
- [ ] Form registration untuk user baru
- [ ] CSRF protection
- [ ] Rate limiting untuk mencegah brute force
- [ ] Logout functionality
- [ ] Remember me feature
- [ ] Password recovery

## 🐛 Troubleshooting

### Port sudah digunakan
Jika port 5000 sudah digunakan, ubah port di `app.py` atau kill process yang menggunakan port tersebut:
```bash
sudo lsof -i :5000
kill -9 <PID>
```

### Module Flask tidak ditemukan
Install Flask terlebih dahulu:
```bash
pip install flask
```

## 📝 Lisensi

Proyek ini dibuat untuk keperluan pembelajaran.

## 👤 Author

**Iqbal**

---

⭐ Jangan lupa beri star jika proyek ini membantu!

## 🤝 Kontribusi

Kontribusi, issues, dan feature requests sangat diterima!

---

**Happy Coding! 🚀**
