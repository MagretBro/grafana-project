# Система мониторинг ПК (macOs)

## Зависимости
- Python 3+
- Grafana 12+
- Prometheus 2.47+
- Node Exporter 1.7+

## Запуск
1. Установите компоненты:

2. Запустите сервисы:
   
node_exporter
/Users/margaritaborodina/ALL_PROJECTS/grafana/prometheus-2.47.0.darwin-amd64/node_exporter/node_exporter-1.7.0.darwin-amd64/node_exporter --collector.cpu --collector.meminfo

prometheus.yml
./prometheus --config.file=prometheus.yml

swap_exporter.py
python3 swap_exporter.py
Serving metrics on http://localhost:8000

mailhog - фэйковый email сервис для Alerts
brew install mailhog
mailhog

grafana
./bin/grafana-server --config=./grafana.ini


3. Откройте Grafana: http://localhost:3000
