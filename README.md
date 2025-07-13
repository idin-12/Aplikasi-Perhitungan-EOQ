# EOQ Streamlit App 📦

Aplikasi interaktif untuk menghitung Economic Order Quantity (EOQ) menggunakan Streamlit dan berbagai pustaka analisis dan optimasi.

## 🎯 Fitur
- Input: Permintaan tahunan, biaya pemesanan, biaya penyimpanan
- Output:
  - EOQ (jumlah pemesanan optimal)
  - Jumlah pesanan per tahun
  - Total biaya persediaan
- Visualisasi kurva total biaya vs kuantitas pesanan
- Representasi simbolik rumus EOQ
- Contoh penggunaan `pulp` untuk optimasi linear dasar

## ▶️ Cara Menjalankan
```bash
pip install -r requirements.txt
streamlit run app.py
