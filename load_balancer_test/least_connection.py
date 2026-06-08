# Simulasi Load Balancing Least Connection

servers = {
    "Server-1": 0,
    "Server-2": 0,
    "Server-3": 0
}

jumlah_request = 12

print("=== LEAST CONNECTION ===\n")

for i in range(jumlah_request):

    # Memilih server dengan koneksi paling sedikit
    server_terpilih = min(servers, key=servers.get)

    print(f"Request-{i+1} -> {server_terpilih}")

    # Menambah jumlah koneksi
    servers[server_terpilih] += 1

print("\nJumlah koneksi akhir:")

for server, koneksi in servers.items():
    print(f"{server} : {koneksi}")