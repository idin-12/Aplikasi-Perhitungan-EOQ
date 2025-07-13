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
st.markdown("Simulasi perhitungan jumlah pemesanan optimal berdasarkan model persediaan klasik.")

# --- Penjelasan Konsep dan Fitur ---
with st.expander("ℹ️ Tentang Aplikasi"):
    st.markdown("""
    ### 📘 Konsep
    Aplikasi ini menggunakan **Inventory Model – EOQ Formula** untuk menghitung jumlah pemesanan optimal (Economic Order Quantity) yang meminimalkan total biaya persediaan.

    ### ⚙️ Fitur
    **Input:**
    - Permintaan tahunan *(annual demand)*
    - Biaya pemesanan per order *(ordering cost)*
    - Biaya penyimpanan per unit *(holding cost)*

    **Output:**
    - EOQ *(jumlah pemesanan optimal)*
    - Jumlah pemesanan per tahun
    - Total biaya persediaan tahunan

    Aplikasi ini juga menampilkan visualisasi interaktif dan representasi matematis dari formula EOQ.
    """)
