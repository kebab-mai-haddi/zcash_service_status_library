# Zcash Service Status Dashboard
This readme deals with installation and setup instructions for building a health-check system for Zcash communities and exchanges. The dashboard is live [here](https://zcashservicestatus.info).

The health check system involves three tools: Prometheus, Blackbox Exporter and Grafana.

## 1. Install [Prometheus](https://www.digitalocean.com/community/tutorials/how-to-install-prometheus-on-ubuntu-16-04)
Use the prometheus.yml file included in this repository for the config.
### For Docker:
```
docker run \
    -p 9090:9090 \
    -v <absolute path to the current directory>/prometheus.yml:/etc/prometheus/prometheus.yml \
    prom/prometheus
```

## 2. Install [Grafana](https://www.digitalocean.com/community/tutorials/how-to-install-and-secure-grafana-on-ubuntu-18-04)


## 3. Install [Blackbox Exporter](https://www.digitalocean.com/community/tutorials/how-to-use-alertmanager-and-blackbox-exporter-to-monitor-your-web-server-on-ubuntu-16-04)
### For Docker:
```
docker run --rm -d -p 9115:9115 --name blackbox_exporter -v `pwd`:/config prom/blackbox-exporter:master --config.file=/config/blackbox.yml
```

## 4. Install Dependencies
```
sudo apt-get install python3-pip
pip3 install prometheus-client==0.7.1
```


## 5. Now, run these commands in different screens to run all the health checks.

```
python3 blockchain_explorers_health_check.py
python3 communities_and_forums_response_time.py
python3 exchanges_health_check.py
python3 metrics.py
```


Note: This readme will be further updated with 'why' section and some FAQs. Please feel free to open any issue and provide us your valuable feedback.
