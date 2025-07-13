import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
from sympy import symbols, Eq, solve
from scipy.stats import norm
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

st.title("📊 Studi Kasus Pabrik Kopi - Aroma Nusantara")

st.sidebar.header("Input Data")
D = st.sidebar.number_input("Permintaan tahunan (unit)", value=10000)
S = st.sidebar.number_input("Biaya pemesanan per pesanan (Rp)", value=50000)
H = st.sidebar.number_input("Biaya penyimpanan per unit per tahun (Rp)", value=2000)

st.subheader("🔢 Perhitungan EOQ (Economic Order Quantity)")

# EOQ formula
Q = symbols('Q', positive=True)
TC = (D / Q)
