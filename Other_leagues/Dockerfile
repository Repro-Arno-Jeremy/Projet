FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir jupyter nbconvert
RUN pip install -r requirements.txt

COPY Scrapping_other_leagues.py /app
COPY analysis_other_leagues.ipynb /app

# Créer un volume pour les résultats
VOLUME /app/output

# Commande par défaut à exécuter
CMD ["bash", "-c", "\
    python Scrapping_other_leagues.py && \
    jupyter nbconvert --to html --execute analysis_other_leagues.ipynb --output ./output/analysis_other_leagues_results.html"]