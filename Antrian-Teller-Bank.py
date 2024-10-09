import math

def calculate_queue_metrics(arrival_rate, service_rate):
    # perhitungan utilitas
    utilization = arrival_rate / service_rate
    
    # Hitung jumlah rata-rata pelanggan dalam sistem
    L_s = arrival_rate / (service_rate - arrival_rate)
    
    # Hitung rata-rata jumlah pelanggan dalam antrian
    L_q = (arrival_rate ** 2) / (service_rate * (service_rate - arrival_rate))
    
    # Hitung waktu tunggu rata-rata dalam sistem (dalam menit)
    W_s = 1 / (service_rate - arrival_rate)
    
    # Hitung waktu tunggu rata-rata dalam antrian (dalam menit)
    W_q = arrival_rate / (service_rate * (service_rate - arrival_rate))
    
    return utilization, L_s, L_q, W_s, W_q

def get_valid_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Masukkan tidak valid. Harap masukkan angka positif.")

def main():
    print("Selamat datang di Kalkulator Teori Antrian!")
    
    # Dapatkan masukan pengguna
    arrival_rate = get_valid_input("Masukkan tingkat kedatangan (λ) dalam nasabah/menit: ")
    service_rate = get_valid_input("Masukkan tingkat pelayanan (μ) dalam nasabah/menit: ")
    
    # Validasi masukan
    if arrival_rate >= service_rate:
        print("Error: Tingkat kedatangan harus lebih kecil dari tingkat pelayanan untuk sistem yang stabil.")
        return
    
    # menghitung metrik
    utilization, L_s, L_q, W_s, W_q = calculate_queue_metrics(arrival_rate, service_rate)
    
    # Hasil cetak
    print(f"\nTingkat kedatangan (λ) = {arrival_rate:.2f} nasabah/menit")
    print(f"Tingkat pelayanan (μ) = {service_rate:.2f} nasabah/menit")
    print("\nHasil Perhitungan:")
    print(f"1. Utilitas Sistem (ρ): {utilization:.2f}")
    print(f"2. Rata-rata Jumlah Nasabah dalam Sistem (Ls): {L_s:.2f} nasabah")
    print(f"3. Rata-rata Jumlah Nasabah dalam Antrian (Lq): {L_q:.2f} nasabah")
    print(f"4. Rata-rata Waktu Tunggu dalam Sistem (Ws): {W_s:.2f} menit")
    print(f"5. Rata-rata Waktu Tunggu dalam Antrian (Wq): {W_q:.2f} menit")

if __name__ == "__main__":
    main()