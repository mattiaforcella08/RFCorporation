# RFCorporation
Progetto di informatica di terza superiore. Realizzazione di un programma di analisi dati tramite un file csv dato in input. Creato da Forcella Mattia e Rasmo Gabriele

#📊 Data Analysis & Reporting Tool
#📖 Panoramica

Questo progetto è un'applicazione Python progettata per automatizzare il processo di analisi dei dati, dalla pulizia iniziale fino alla generazione di report strutturati.

A partire da un semplice file CSV, il programma esegue:

pulizia e pre-elaborazione dei dati
analisi statistica
calcolo delle correlazioni
visualizzazione grafica
generazione automatica di un report HTML

Il tool è adatto a scopi didattici, analisi esplorative e utilizzi professionali leggeri.

✨ Funzionalità principali
🧹 Pulizia automatica dei dati
Rimozione dei valori mancanti
Conversione automatica dei tipi (Data, Vendite)
Individuazione e rimozione degli outlier (metodo IQR)
📊 Analisi statistica
Statistiche descrittive (media, quartili, minimo, massimo)
Calcolo della matrice di correlazione
📈 Visualizzazione
Generazione di heatmap delle correlazioni tramite Seaborn
🌐 Generazione report
Creazione automatica di un report HTML
Tabelle e grafici integrati
Layout moderno e responsive
💻 Esperienza utente
Output colorato nel terminale
Barre di avanzamento (progress bar)
Sistema di log con timestamp


#🛠️ Requisiti

Installare le dipendenze necessarie:

pip install pandas numpy matplotlib seaborn jinja2 colorama tqdm
📂 Formato dei dati in input

Il programma supporta attualmente:

File CSV (.csv)
Struttura consigliata:
Colonna	Descrizione
Data	Data (convertita automaticamente)
Vendite	Valore numerico (convertito automaticamente)
Altre colonne numeriche	Utilizzate per analisi e correlazioni

#🚀 Utilizzo
Avviare il programma:
python Programma.py
Inserire la licenza richiesta:
forcella
Inserire il percorso del file CSV:
C:\percorso\al\file.csv
🔐 Sistema di licenze

Il programma include un semplice sistema di accesso:

forcella → accesso completo
info → descrizione del programma
premium → modalità dimostrativa (effetto visivo)
📁 Output generati

Il programma produce automaticamente:

📄 Report HTML
Nome: Data_Analysis_Report_YYYY-MM-DD.html
🖼️ Grafico correlazioni
Nome: Graf_Correlazione.png
🧩 Architettura del progetto

Principali componenti:

load_data() → caricamento del dataset
toglierrori() → pulizia e preprocessing
analyze_data() → analisi statistica
visualiza_dati() → generazione grafici
creasito() → creazione report HTML
main() → flusso principale
#⚠️ Limitazioni
Supporta esclusivamente file .csv
Richiede input manuale da terminale
Alcuni tempi di attesa sono simulati per migliorare l’esperienza utente