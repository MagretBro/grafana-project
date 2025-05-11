from prometheus_client import start_http_server, Gauge
import subprocess
import time

g = Gauge('macos_swap_used_megabytes', 'Swap used on macOS in MB')
g_total = Gauge('macos_swap_total_megabytes', 'Total Swap in MB')

def update_metrics():
    output = subprocess.check_output("sysctl vm.swapusage", shell=True).decode()
    parts = output.split()
    total = float(parts[3].replace('M', '').replace(',', '.'))
    used = float(parts[6].replace('M', '').replace(',', '.'))
    g_total.set(total)
    g.set(used)

if __name__ == '__main__':
    start_http_server(8000)
    print("Serving metrics on http://localhost:8000")
    while True:
        update_metrics()
        time.sleep(10)
