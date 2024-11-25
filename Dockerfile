FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir jupyter nbconvert
RUN pip install -r requirements.txt

COPY Data_Scrapping.py /app
COPY analysis_notebook.ipynb /app

# Créer un volume pour les résultats
VOLUME /app/output

# Commande par défaut à exécuter
CMD ["bash", "-c", "\
    python Data_Scrapping.py && \
    jupyter nbconvert --to html --execute analysis_notebook.ipynb --output ./output/analysis_results.html"]