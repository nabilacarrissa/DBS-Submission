# Proyek Analisis Data Pelanggan E-Commerce

## Identitas

- **Nama:** Nabila Carrissa Dewi
- **Email:** [nabilacarrissa@gmail.com](mailto:nabilacarrissa@gmail.com)
- **ID Dicoding:** CDCC748D6X0297

---

## Deskripsi Proyek

Proyek ini bertujuan untuk menganalisis data pelanggan dari _E-Commerce Public Dataset_ guna memahami distribusi pelanggan berdasarkan lokasi geografis.

Analisis difokuskan pada:

- Distribusi pelanggan berdasarkan **state (provinsi)**
- Distribusi pelanggan berdasarkan **kota (city)**
- Identifikasi wilayah dengan potensi pasar tertinggi

Periode analisis mencakup data pada rentang **2016–2018**.

---

## Pertanyaan Bisnis

1. Bagaimana distribusi pelanggan berdasarkan state dan kontribusinya terhadap total pelanggan selama periode 2016–2018?
2. Bagaimana distribusi pelanggan berdasarkan kota dan kota mana saja yang memiliki jumlah pelanggan tertinggi selama periode 2016–2018?

---

## Proses Analisis Data

### 1. Data Wrangling

- Mengumpulkan dataset pelanggan
- Mengecek kualitas data:
  - Missing values
  - Duplicate data

- Melakukan pembersihan data:
  - Menghapus duplikasi
  - Standarisasi format teks

### 2. Exploratory Data Analysis (EDA)

- Analisis distribusi pelanggan per state
- Analisis distribusi pelanggan per kota
- Analisis konsentrasi wilayah pelanggan

### 3. Visualization

- Bar chart distribusi pelanggan per state
- Bar chart distribusi pelanggan per kota
- Visualisasi dibuat dengan prinsip:
  - Sederhana
  - Konsisten
  - Mudah dipahami

---

## Dashboard

Dashboard dibuat menggunakan **Streamlit** untuk menampilkan hasil analisis secara interaktif.

Fitur dashboard:

- Total jumlah pelanggan
- Distribusi pelanggan per state
- Distribusi pelanggan per kota
- Filter berdasarkan state

---

## Cara Menjalankan Notebook

1. Buka file:

```bash
notebook.ipynb
```

2. Jalankan semua cell:

```bash
Runtime → Run All
```

---

## Cara Menjalankan Dashboard

1. Masuk ke folder project
2. Jalankan perintah berikut:

```bash
streamlit run dashboard/dashboard.py
```

3. Dashboard akan terbuka di browser

---

## Struktur Folder

```bash
submission/
├── Dashboard/
│   ├── dashboard.py
│   └── main_data.csv
├── Data/
│   └── customers_dataset.csv
├── Image
│   ├── visualization_city_distribution.png
│   ├── visualization_heatmap_state
│   ├── visualization_state_distribution.png
│   └── visualization_state_segmentation.png
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

---

## Insight Utama

- State **SP (São Paulo)** memiliki jumlah pelanggan tertinggi
- Kota **São Paulo** menjadi pusat utama pelanggan
- Wilayah Sudeste mendominasi distribusi pelanggan

---

## Rekomendasi Bisnis

- Fokuskan strategi marketing pada wilayah dengan pelanggan tinggi seperti SP
- Lakukan ekspansi ke wilayah dengan jumlah pelanggan rendah
- Optimalkan layanan di kota dengan pelanggan terbanyak

---

## Link Dashboard (Streamlit)

Tuliskan link deployment di sini:

```
https://namamu.streamlit.app
```

---

## Catatan

- Pastikan notebook sudah dijalankan sebelum submit
- Pastikan semua file tersedia dalam folder submission
- Dashboard harus dapat berjalan tanpa error

---

## Penutup

Proyek ini dibuat sebagai bagian dari submission kelas **Coding Camp powered by DBS Foundation (Dicoding)**.

Terima kasih.
