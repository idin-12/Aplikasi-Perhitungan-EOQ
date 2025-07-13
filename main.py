import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sympy as sp
from scipy.optimize import minimize
from pulp import LpProblem, LpMinimize, LpVariable

# --- Konfigurasi halaman ---
st.set_page_config(page_title="EOQ Calculator", layout="centered")
st.title("📦 Aplikasi Perhitungan EOQ (Economic Order Quantity)")
st.markdown("Simulasi perhitungan jumlah pemesanan optimal dengan model persediaan klasik.")

# --- Penjelasan Fitur dan Konsep ---
with st.expander("ℹ️ Tentang Aplikasi"):
    st.markdown("""
    ### 📘 Konsep
    Aplikasi ini menggunakan **Inventory Model – EOQ Formula** untuk menentukan jumlah pemesanan optimal yang meminimalkan total biaya persediaan.

    Rumus dasar EOQ:
    \[
    EOQ = \sqrt{\\frac{2DS}{H}}
    \]
    Di mana:
    - **D** = Permintaan tahunan (unit)
    - **S** = Biaya pemesanan per order (Rp)
    - **H** = Biaya penyimpanan per unit per tahun (Rp)

    ### ⚙️ Fitur
    **Input:**
    - Permintaan tahunan *(D)*
    - Biaya pemesanan per order *(S)*
    - Biaya penyimpanan per unit *(H)*

    **Output:**
    - EOQ *(jumlah pesanan optimal)*
    - Jumlah pemesanan per tahun
    - Total biaya persediaan tahunan
    """)

# --- Input User ---
st.sidebar.header("🔧 Parameter Input")
D = st.sidebar.number_input("Permintaan tahunan (unit)", value=5000.0, min_value=1.0)
S = st.sidebar.number_input("Biaya pemesanan per order (Rp)", value=100000.0, min_value=0.0)
H = st.sidebar.number_input("Biaya penyimpanan per unit per tahun (Rp)", value=1000.0, min_value=0.0)

# --- Perhitungan EOQ ---
eoq = np.sqrt((2 * D * S) / H)
order_freq = D / eoq
total_cost = (order_freq * S) + ((eoq / 2) * H)

# --- Output ---
st.subheader("📊 Hasil Perhitungan EOQ")
st.write(f"**EOQ (Jumlah pesanan optimal):** {eoq:.2f} unit")
st.write(f"**Jumlah pemesanan per tahun:** {order_freq:.2f} kali")
st.write(f"**Total biaya persediaan:** Rp {total_cost:,.2f}")

# --- Visualisasi Kurva Total Biaya ---
Q = np.linspace(1, D, 200)
TC = (D / Q) * S + (Q / 2) * H

fig = go.Figure()
fig.add_trace(go.Scatter(x=Q, y=TC, mode='lines', name='Total Cost'))
fig.add_trace(go.Scatter(x=[eoq], y=[total_cost], mode='markers+text',
                         name='EOQ', text=["EOQ"], textposition="top center"))
fig.update_layout(title="Kurva Total Biaya Persediaan",
                  xaxis_title="Order Quantity (Q)",
                  yaxis_title="Total Cost (Rp)",
                  height=400)
st.plotly_chart(fig)

# --- Formula EOQ ---
st.subheader("📐 Rumus EOQ (dalam simbol)")
Q_sym, D_sym, S_sym, H_sym = sp.symbols('Q D S H')
eoq_expr = sp.sqrt((2 * D_sym * S_sym) / H_sym)
st.latex(r"EOQ = \sqrt{\frac{2DS}{H}}")
st.latex(f"EOQ = {sp.latex(eoq_expr)}")

# --- Optimasi Linear (Opsional) ---
st.subheader("🧪 [Eksperimental] Optimasi Linear (Pulp)")
prob = LpProblem("Minimize_Inventory_Cost", LpMinimize)
Q_opt = LpVariable("Q", lowBound=1)
prob += (D / Q_opt) * S + (Q_opt / 2) * H
prob.solve()
st.write(f"**Hasil optimasi (Pulp):** Q = {Q_opt.varValue:.2f} unit")
