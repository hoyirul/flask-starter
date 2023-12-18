# Flask Template

Proyek ini merupakan aplikasi web yang dibangun menggunakan Flask, sebuah framework web Python yang ringan dan mudah digunakan. Aplikasi ini memiliki fitur query builder yang memungkinkan pengambilan data yang lebih fleksibel dan dinamis dari database MySQL.

## Deskripsi

Proyek ini merupakan yang dibangun menggunakan Flask, sebuah framework web Python yang ringan dan mudah digunakan. API ini menyediakan endpoints untuk mengelola data pada database MySQL dengan menggunakan fitur query builder yang memungkinkan pengambilan data yang lebih fleksibel dan dinamis.

## Fitur Utama

- Query Builder: Memanfaatkan query builder untuk menyusun dan mengeksekusi kueri SQL dengan mudah, termasuk fitur-fitur select, where, order by, dan group by.

- Relasi Model: Menggunakan fitur relasi model untuk mengelola hubungan antara tabel dengan mudah.

- User-Friendly: Antarmuka API yang sederhana dan mudah digunakan bagi para pengguna untuk berinteraksi dengan data.

## Cara Penggunaan

1. Pastikan Anda memiliki Python dan MySQL terinstal di komputer Anda.

2. Jika sudah mempunyai python silahkan jalankan di terminal anda (`pip install -U virtualenv`)

5. Membuat virualenv (`python -m venv venv`)

4. Lalu (`source ./venv/bin/activate`) MacOS atau (`venv\Scripts\activate`) Windows

5. Setelah itu silahkan jalankan di terminal anda (`pip install -r requirements.txt`)

6. Lalu jalankan (`cp .env.example .env`)

7. Setelah itu generate key dengan menjalankan (`python ./utils/generate_key.py`)

2. Buat database dengan nama yang sesuai dalam MySQL.

3. Ubah konfigurasi database di file `.env` agar sesuai dengan pengaturan MySQL Anda.

4. Jalankan aplikasi dengan perintah berikut: (`python manage.py`)

5. Buka browser dan akses [http://127.0.0.1:8000](http://127.0.0.1:8000) untuk memulai penggunaan API.

## Versi

**Versi 1.0.0**

## Kontribusi

Anda dapat berkontribusi pada proyek ini dengan cara berikut:

1. Fork proyek ini.

2. Buat branch baru (`git checkout -b fitur-anda`).

3. Lakukan perubahan pada kode Anda.

4. Commit perubahan (`git commit -m 'Menambahkan fitur baru'`).

5. Push ke branch (`git push origin fitur-anda`).

6. Buat Pull Request baru.

## Author

Mochammad Hairullah
Developer