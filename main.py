def calculate_eoq(D, S, H):
    """
    EOQ Formula: sqrt((2 * D * S) / H)
    D = Permintaan tahunan
    S = Biaya pemesanan per order
    H = Biaya penyimpanan per unit per tahun
    """
    from math import sqrt

    eoq = sqrt((2 * D * S) / H)
    total_orders = D / eoq
    total_inventory_cost = total_orders * S + (eoq / 2) * H

    return eoq, total_inventory_cost, total_orders


def main():
    print("=== Aplikasi Perhitungan EOQ ===")
    try:
        D = float(input("Masukkan permintaan tahunan (unit): "))
        S = float(input("Masukkan biaya pemesanan per order: "))
        H = float(input("Masukkan biaya penyimpanan per unit per tahun: "))

        eoq, total_cost, order_freq = calculate_eoq(D, S, H)

        print("\n--- Hasil Perhitungan ---")
        print(f"EOQ (Jumlah pesanan optimal): {eoq:.2f} unit")
        print(f"Total biaya persediaan: Rp {total_cost:,.2f}")
        print(f"Jumlah pemesanan per tahun: {order_freq:.2f} kali")
    except ValueError:
        print("Input tidak valid. Pastikan Anda memasukkan angka.")


if __name__ == "__main__":
    main()
