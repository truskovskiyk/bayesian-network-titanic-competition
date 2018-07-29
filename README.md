# bayesian-network-titanic-competition
BayesianNetwork for Titanic: Machine Learning from Disaster competition

## docker
```bash
docker build -t bn-tatanic:latest .
docker run -it bn-tatanic:latest /bin/bash
```

## setup
```bash
virtualenv -p python3.6 venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Train
```bash
python bn/main.py
```