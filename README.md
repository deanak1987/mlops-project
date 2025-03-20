# MLOps Project
Automated Model Deployment with Docker, GitHub Actions, and AWS
 ## Project Overview
This project demonstrates end-to-end machine learning model deployment using FastAPI, Docker, Prometheus, and Grafana, orchestrated with Docker Compose. It automates deployment on an AWS EC2 instance via GitHub Actions, ensuring seamless updates on each code push.
## Key Features

* FastAPI backend for serving a trained ML model (Titanic survival prediction).
* Docker & Docker Compose for containerized deployment.
* Prometheus for monitoring ML API performance and system metrics.
* Grafana for visualizing metrics in real-time.
* GitHub Actions CI/CD for automatic deployment to AWS EC2 on push to main.

## To Run:
### Clone Repository
```
git clone https://github.com/deanak1987/mlops-project.git
cd mlops-project
```

### Install Dependancies
```
sudo apt update
sudo apt install -y docker-compose python3-pip
pip install -r requirements.txt
```

### Run the Service
```
docker-compose up -d --build
```
The following services and their respective endpoints:
* FastAPI API: http://localhost:8000
* Prometheus UI: http://localhost:9090
* Grafana Dashboard: http://localhost:3000

### Test the API Endpoint
```
curl -X 'POST' 'http://localhost:8000/predict' \
-H 'Content-Type: application/json' \
-d '{"Pclass": 3, "Sex": 1, "Age": 22, "Fare": 7.25}'
```