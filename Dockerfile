FROM python:3.12-slim

# Ustawiamy katalog roboczy w kontenerze
WORKDIR /app

# Kopiujemy pliki z lokalnego systemu do kontenera
COPY . /app

# Instalujemy wymagane zależności z pliku requirements.txt
RUN pip install .

