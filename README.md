# 🚲 Bike Sharing Dashboard ✨

Dashboard ini dibuat untuk menganalisis pola penyewaan sepeda berdasarkan faktor waktu, kondisi cuaca, dan jenis hari menggunakan dataset Bike Sharing (2011–2012).

---

## 📌 Setup Environment - Anaconda

```
conda create --name bike-ds python=3.9
conda activate bike-ds
pip install -r requirements.txt
```

---

## 📌 Setup Environment - Shell/Terminal

```
pip install -r requirements.txt
```

---

## 📌 Run Streamlit App

```
streamlit run dashboard/dashboard.py
```

---

## 📁 Project Structure

```
submission/
│── dashboard/
│   ├── dashboard.py
│   ├── day_cleaned.csv
│   └── hour_cleaned.csv
│── data/
│   ├── day.csv
│   ├── hour.csv
│── notebook.ipynb
│── requirements.txt
│── README.md
│── url.txt
```

---

## 📊 Main Features

* Analisis penyewaan berdasarkan kondisi cuaca
* Analisis pola penyewaan berdasarkan jam
* Perbandingan penyewaan antara hari kerja dan akhir pekan
* Visualisasi interaktif menggunakan Streamlit

---

## 🌐 Dashboard Link

Lihat pada file `url.txt`
