import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ========================
# CONFIG
# ========================
st.set_page_config(page_title="Dashboard Analisis Pelanggan", layout="wide")

# ========================
# LOAD DATA (AMAN UNTUK SUBMISSION)
# ========================
BASE_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(BASE_DIR, "main_data.csv")


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


df = load_data()

# ========================
# TITLE
# ========================
st.title("Dashboard Analisis Pelanggan E-Commerce")
st.markdown("Analisis distribusi pelanggan berdasarkan state dan kota")

# ========================
# VALIDASI KOLOM
# ========================
required_cols = ["customer_state", "customer_city"]

for col in required_cols:
    if col not in df.columns:
        st.error(f"Kolom '{col}' tidak ditemukan di dataset!")
        st.stop()

# ========================
# METRICS
# ========================
st.subheader("Ringkasan Data")

col1, col2, col3 = st.columns(3)

col1.metric("Total Pelanggan", f"{df.shape[0]:,}")
col2.metric("Total State", df["customer_state"].nunique())
col3.metric("Total Kota", df["customer_city"].nunique())

st.markdown("---")

# ========================
# TOP STATE
# ========================
st.subheader("Top 10 State Pelanggan")

state_counts = df["customer_state"].value_counts().head(10)

fig1, ax1 = plt.subplots(figsize=(8, 5))
ax1.barh(state_counts.index[::-1], state_counts.values[::-1], color="#1E88E5")
ax1.set_xlabel("Jumlah Pelanggan")
ax1.set_title("Top 10 State")

st.pyplot(fig1)

# ========================
# TOP CITY
# ========================
st.subheader("Top 10 Kota Pelanggan")

city_counts = df["customer_city"].value_counts().head(10)

fig2, ax2 = plt.subplots(figsize=(8, 5))
ax2.barh(city_counts.index[::-1], city_counts.values[::-1], color="#1565C0")
ax2.set_xlabel("Jumlah Pelanggan")
ax2.set_title("Top 10 Kota")

st.pyplot(fig2)

# ========================
# PIE CHART STATE
# ========================
st.subheader(" Distribusi Top State")

top_state = df["customer_state"].value_counts().head(5)

fig3, ax3 = plt.subplots()

ax3.pie(top_state.values, labels=top_state.index, autopct="%1.1f%%", startangle=140)

ax3.set_title("Top 5 State")

st.pyplot(fig3)

# ========================
# HEATMAP
# ========================
st.subheader(" Heatmap Distribusi State")

heat_data = df["customer_state"].value_counts().head(10).to_frame().T

fig4, ax4 = plt.subplots(figsize=(10, 2))

sns.heatmap(heat_data, annot=True, fmt="d", cmap="Blues", ax=ax4)

ax4.set_yticklabels([])
ax4.set_title("Distribusi Pelanggan per State")

st.pyplot(fig4)

# ========================
# FOOTER
# ========================
st.markdown("---")
st.markdown(" Dibuat oleh Nabila Carrissa Dewi")
