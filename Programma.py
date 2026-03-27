import pandas as pd                             # type: ignore #Per gestire il file CSV dato in input
import numpy as np                              #Operazioni matematiche avanzate
import matplotlib.pyplot as plt                 #Grafici
import seaborn as sns                           #Migliorare i grafici
import datetime                                 #Fornisce l'orario della creazione di file univoci di HTML
import os                                       #Per interagire con la gestione dei file
from jinja2 import Template                     # type: ignore #Creare e gestire il file HTML
from colorama import Fore, Style, init          # type: ignore #Colorare le scritte
import time as t                                #Gestire il tempo
import sys
from tqdm import tqdm                           #Progress bar per il terminale
import random                                   #Per generare durate randomiche
init(autoreset=True)                            #Colori tornano al valore di default automaticamente

# Licenza e colorazione personalizzati
licenza = "forcella"
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.CYAN, Fore.MAGENTA]

# Funzione per stampare messaggi con timestamp
def log_message(message, color=Fore.WHITE):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{color}[{timestamp}] {message}")

# Funzione per caricare i dati
def load_data(file_input):
    try:
        if file_input.endswith('.csv'):
            df = pd.read_csv(file_input)        # Legge il file in input
        else:
            log_message("Formato file non supportato. Usa .csv", Fore.RED)
            return None
        log_message(f"Caricato dataset da {file_input}", Fore.GREEN)
        return df
    except Exception as e:
        log_message(f"Errore nel caricamento del file: {e}", Fore.RED)
        return None

# Pulizia e pre-elaborazione dei dati con barra di caricamento e durata randomica
def toglierrori(df):
    log_message("Pulizia dei dati in corso...", Fore.YELLOW)
    
    # Genera un tempo di attesa randomico tra 2 e 10 secondi
    sleep_time = random.randint(2, 10)
    
    # Barra di avanzamento per la durata randomica della pulizia
    for _ in tqdm(range(sleep_time), desc="Pulizia dei dati", unit="secondi", ncols=100, ascii=True):
        t.sleep(1)

    # Rimuovi valori mancanti
    df.dropna(inplace=True)

    # Conversione di una colonna di stringhe in dati
    if 'Data' in df.columns:
        df['Data'] = pd.to_datetime(df['Data'], errors='coerce')  # Gestisce gli errori di conversione

    # Trasforma le colonne delle vendite in numeri
    if 'Vendite' in df.columns:
        df['Vendite'] = pd.to_numeric(df['Vendite'], errors='coerce')  # Gestisce gli errori di conversione

    # Seleziona solo le colonne con all'interno dei valori numerici
    numeric_df = df.select_dtypes(include=[np.number])

    # Rimuovere outliers usando l'IQR
    Q1 = numeric_df.quantile(0.25)
    Q3 = numeric_df.quantile(0.75)
    IQR = Q3 - Q1
    df = df[~((numeric_df < (Q1 - 1.5 * IQR)) | (numeric_df > (Q3 + 1.5 * IQR))).any(axis=1)]

    log_message("Pulizia completata.", Fore.GREEN)
    return df

# Analisi statistica avanzata
def analyze_data(df):
    log_message("Inizio analisi dei dati...", Fore.YELLOW)
    t.sleep(3)

    # Descrizione statistica di base
    descrizione = df.describe()
    log_message(f"Descrizione statistica:\n{descrizione}", Fore.LIGHTRED_EX)

    # Correlazioni tra le variabili numeriche
    numeric_df = df.select_dtypes(include=[np.number])
    correlazione = numeric_df.corr()
    log_message(f"Correlazioni:\n{correlazione}", Fore.CYAN)

    return descrizione, correlazione

# Visualizzazione dei dati
def visualiza_dati(df):
    log_message("Generazione grafici in corso...", Fore.YELLOW)
    t.sleep(2)

    # Crea i grafici temporanei e salvali come immagini
    graf_correlazione = 'Graf_Correlazione.png'

    # Heatmap delle correlazioni (se ci sono colonne numeriche)
    numeric_df = df.select_dtypes(include=[np.number])  # Solo colonne numeriche
    if not numeric_df.empty:
        plt.figure(figsize=(10, 8))
        sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Matrice di Correlazione')
        plt.savefig(graf_correlazione)

    log_message("Grafico delle correlazioni generato con successo!", Fore.GREEN)
    return graf_correlazione

# Template HTML per il report
preimpo_html = """
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Report di Analisi dei Dati</title>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Open+Sans:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        /* Corpo e struttura */
        body {
            font-family: 'Open Sans', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f8f9fa;
            color: #343a40;
        }
        .container {
            max-width: 1100px;
            margin: 50px auto;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            font-size: 16px;
        }
        h1 {
            font-family: 'Roboto', sans-serif;
            text-align: center;
            color: #1a1a1a;
            font-size: 36px;
            font-weight: 700;
            margin-bottom: 40px;
        }
        h3 {
            color: #1a1a1a;
            font-size: 26px;
            font-weight: 500;
            margin-top: 30px;
            border-bottom: 3px solid #3498db;
            padding-bottom: 5px;
        }
        p {
            color: #666;
            font-size: 18px;
            line-height: 1.8;
            margin-bottom: 20px;
        }
        .section {
            margin-bottom: 40px;
        }
        .table-container {
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            padding: 15px;
            text-align: center;
            border: 1px solid #ddd;
        }
        th {
            background-color: #3498db;
            color: #fff;
            font-weight: 600;
        }
        td {
            background-color: #f9f9f9;
            color: #333;
        }
        th, td {
            border-radius: 6px;
        }
        th {
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }
        td {
            border-bottom-left-radius: 8px;
            border-bottom-right-radius: 8px;
        }
        .img-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 40px;
        }
        .img-container img {
            max-width: 100%;
            border-radius: 10px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease-in-out;
        }
        .img-container img:hover {
            transform: scale(1.05);
        }
        footer {
            text-align: center;
            margin-top: 50px;
            font-size: 14px;
            color: #999;
        }
        footer p {
            margin: 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Report di Analisi dei Dati</h1>

        <div class="section">
            <h3>Statistiche Descrittive</h3>
            <p>Le statistiche descrittive riportano i valori principali del dataset, tra cui la media, il minimo, il massimo e i quartili delle vendite. Questi valori forniscono una panoramica iniziale sull'andamento dei dati.</p>
            <div class="table-container">
                {{ description }}
            </div>
        </div>
        <div class="section">
            <h3>Grafici delle Correlazioni</h3>
            <p>Il seguente grafico illustra le correlazioni tra le variabili numeriche, con un focus particolare sui trend e le dinamiche significative.</p>

            <div class="img-container">
                <img src="Graf_Correlazione.png" alt="Matrice di Correlazione"/>
            </div>
        </div>
    </div>
</body>
</html>
"""

# Funzione per generare il report HTML con una barra di avanzamento
def creasito(df_toglierrori, description, correlation, correlation_chart):
    log_message("Generazione del report HTML in corso...", Fore.YELLOW)

    # Barra di caricamento per la generazione del report
    for _ in tqdm(range(100), desc="Creazione del file HTML", ncols=100, ascii=True):
        t.sleep(0.05)  # Simula il tempo di creazione del file HTML

    template = Template(preimpo_html)
    html_content = template.render(description=description.to_html(),
                                   correlation=correlation.to_html(),
                                   correlation_chart=correlation_chart)

    now = datetime.datetime.now()
    formatted_date = now.strftime("%Y-%m-%d")
    html_filename = f"Data_Analysis_Report_{formatted_date}.html"  # Crea il file HTML con la data
    with open(html_filename, "w") as f:
        f.write(html_content)

    log_message(f"Report HTML generato correttamente! {html_filename}", Fore.GREEN)
    return html_filename

# Funzione principale
def main():
    log_message("Benvenuto nel programma di analisi dati avanzata!", Fore.MAGENTA)

    file_input = input(Fore.BLUE + "Inserisci il percorso del file CSV o Excel: ")

    if not os.path.exists(file_input):
        log_message(f"Il file {file_input} non esiste!", Fore.RED)
        return

    df = load_data(file_input)

    if df is None:
        return

    df_toglierrori = toglierrori(df)

    description, correlation = analyze_data(df_toglierrori)

    correlation_chart = visualiza_dati(df_toglierrori)

    creasito(df_toglierrori, description, correlation, correlation_chart)

if __name__ == "__main__":
    text = Fore.LIGHTCYAN_EX + """
 _   _ _   _____ ___ __  __    _  _____ _____    ____    _  _____  _    
| | | | | |_   _|_ _|  \/  |  / \|_   _| ____|  |  _ \  / \|_   _|/ \   
| | | | |   | |  | || |\/| | / _ \ | | |  _|    | | | |/ _ \ | | / _ \  
| |_| | |___| |  | || |  | |/ ___ \| | | |___   | |_| / ___ \| |/ ___ \ 
 \___/|_____|_| |___|_|_ |_/_/__ \_\_|_|_____|_ |____/_/_  \_\_/_/_  \_\ 
   / \  | \ | |  / \  | |   |_ _/ ___|_   _| \ \   / / / | / |( _ )    
  / _ \ |  \| | / _ \ | |    | |\___ \ | |    \ \ / /  | | | |/ _ \    
 / ___ \| |\  |/ ___ \| |___ | | ___) || |     \ V /   | |_| | (_) |   
/_/   \_\_| \_/_/   \_\_____|___|____/ |_|      \_/    |_(_)_|\___/        
"""

    log_message(text, Fore.LIGHTCYAN_EX)

    log_message("\n--- Accesso al sistema ---", Fore.YELLOW)

    while True:
        maranza = input(Fore.BLUE + "Inserire la licenza per utilizzare il programma, se si desidera ricevere info si scriva 'info' ==> ")
        if maranza == licenza:
            log_message("Accesso consentito. Attendi il caricamento...", Fore.GREEN)
            t.sleep(3)
            main()
            break
        elif maranza == "info":
            log_message("Questo programma ti permette di analizzare, visualizzare e creare report dei tuoi dati in modo semplice ma accurato.", Fore.CYAN)
        elif maranza == "premium":
            for i in range(20):
                sys.stdout.write(f"\r{colors[i % len(colors)]}Licenza premium sbloccata ==> forcella")
                sys.stdout.flush()
                t.sleep(0.2)
            print("")
        else:
            log_message("Licenza invalida o scaduta. Puoi acquistarla su rf-corporation.github.io/Homepage", Fore.RED)
            t.sleep(3)
