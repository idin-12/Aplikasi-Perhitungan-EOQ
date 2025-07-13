import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sympy as sp
from scipy.optimize import minimize
from pulp import LpProblem, LpMinimize, LpVariable, lpSum

# --- Judul Aplikasi ---
st.set_page_config(page_title="EOQ Calculator", layout="centered")
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.markdown("Simulasi perhitungan jumlah pemesanan optimal dengan model persediaan klasik.")

# --- Input User ---
st.sidebar.header("🔧 Parameter Input")
D = st.sidebar.number_input("Permintaan tahunan (unit)", value=5000.0, min_value=1.0)
S = st.sidebar.number_input("Biaya pemesanan per order (Rp)", value=100000.0, min_value=0.0)
H = st.sidebar.number_input("Biaya penyimpanan per unit per tahun (Rp)", value=1000.0, min_value=0.0)

# --- EOQ Formula ---
eoq = np.sqrt((2 * D * S) / H)
order_freq = D / eoq
total_cost = (order_freq * S) + ((eoq / 2) * H)

# --- Output ---
st.subheader("📊 Hasil Perhitungan EOQ")
st.write(f"**EOQ (Jumlah pesanan optimal):** {eoq:.2f} unit")
st.write(f"**Jumlah pemesanan per tahun:**
