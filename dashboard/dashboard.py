# ==============================
# IMPORT LIBRARY
# ==============================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import streamlit as st

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

# ==============================
# TITLE
# ==============================
st.title("🚲 Bike Sharing Dashboard")
st.markdown("Analisis penyewaan sepeda berdasarkan cuaca, waktu, dan hari kerja (2011–2012)")

# ==============================
# LOAD DATA
# ==============================
day_df = pd.read_csv("day_cleaned.csv")
hour_df = pd.read_csv("hour_cleaned.csv")

# ==============================
# SIDEBAR (optional filter)
# ==============================
st.sidebar.header("Filter")

selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca",
    options=sorted(day_df["weathersit"].unique()),
    default=sorted(day_df["weathersit"].unique())
)

# filter data
filtered_day = day_df[day_df["weathersit"].isin(selected_weather)]

# ==============================
# VISUALISASI 1: CUACA
# ==============================
st.subheader("📊 Penyewaan Sepeda Berdasarkan Kondisi Cuaca")

weather_avg = filtered_day.groupby("weathersit")["cnt"].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(8,5))
sns.barplot(data=weather_avg, x="weathersit", y="cnt", ax=ax1)

ax1.set_title("Rata-rata Penyewaan Berdasarkan Cuaca")
ax1.set_xlabel("Weathersit")
ax1.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig1)

st.caption("Cuaca cerah memiliki rata-rata penyewaan tertinggi.")

# ==============================
# VISUALISASI 2: JAM
# ==============================
st.subheader("⏰ Penyewaan Sepeda Berdasarkan Jam")

hour_avg = hour_df.groupby("hr")["cnt"].mean().reset_index()

fig2, ax2 = plt.subplots(figsize=(10,5))
sns.lineplot(data=hour_avg, x="hr", y="cnt", marker="o", ax=ax2)

ax2.set_title("Rata-rata Penyewaan Berdasarkan Jam")
ax2.set_xlabel("Jam")
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.set_xticks(range(0,24))

st.pyplot(fig2)

st.caption("Puncak penyewaan terjadi pada pagi dan sore hari.")

# ==============================
# VISUALISASI 3: WORKING DAY
# ==============================
st.subheader("📅 Penyewaan: Hari Kerja vs Akhir Pekan")

workingday_avg = day_df.groupby("workingday")["cnt"].mean().reset_index()

fig3, ax3 = plt.subplots(figsize=(6,5))
sns.barplot(data=workingday_avg, x="workingday", y="cnt", ax=ax3)

ax3.set_title("Perbandingan Penyewaan")
ax3.set_xlabel("0 = Weekend/Holiday, 1 = Working Day")
ax3.set_ylabel("Rata-rata Penyewaan")

st.pyplot(fig3)

st.caption("Penyewaan lebih tinggi pada hari kerja.")

# ==============================
# CLUSTERING
# ==============================
st.subheader("📌 Distribusi Kategori Permintaan")

# buat kategori demand
day_df['demand_category'] = pd.qcut(
    day_df['cnt'],
    q=3,
    labels=['Low', 'Medium', 'High']
)

fig4, ax4 = plt.subplots(figsize=(6,5))
sns.countplot(data=day_df, x="demand_category", ax=ax4)

ax4.set_title("Distribusi Demand Category")
ax4.set_xlabel("Kategori")
ax4.set_ylabel("Jumlah Hari")

st.pyplot(fig4)

st.caption("Data dibagi menjadi Low, Medium, dan High demand.")

# ==============================
# FOOTER
# ==============================
st.markdown("---")

st.caption("(Dibuat untuk submission Proyek Analisis Data)")