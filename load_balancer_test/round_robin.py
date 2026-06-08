# Simulasi Load Balancing Round Robin

servers = ["Server-1", "Server-2", "Server-3"]

jumlah_request = 12

print("=== ROUND ROBIN ===\n")

for i in range(jumlah_request):
    server = servers[i % len(servers)]
    print(f"Request-{i+1} -> {server}")