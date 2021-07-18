FROM python:3.8

COPY src /app/src
COPY requirements.txt /app

RUN mkdir -p /app/data/raw

COPY data/raw/ames_housing_data.csv /app/data/raw

WORKDIR /app

RUN pip install -r requirements.txt

WORKDIR /app/src

CMD streamlit run apps/ames_housing_app.py