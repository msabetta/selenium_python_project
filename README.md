# Selenium Python Project

Questo repository contiene un progetto di automazione web che utilizza **Selenium** con **Python**. Lo script principale (`main.py`) esegue una serie di azioni automatizzate su un browser, probabilmente per test funzionali o per lo scraping di dati.

## 🚀 Requisiti di Utilizzo

Prima di eseguire il progetto, assicurati di avere installati i seguenti componenti:

*   **Anaconda Individual Edition**: Utilizzato per gestire l'ambiente Python e le dipendenze. Puoi scaricarlo da [anaconda.com](https://www.anaconda.com/products/individual#windows).
*   **Python 3.8**: Il progetto richiede specificamente questa versione di Python. Scaricabile da [python.org](https://www.python.org/downloads/).
*   **Git**: Per clonare il repository. Scaricabile da [git-scm.com](https://git-scm.com/).

## 📦 Installazione ed Esecuzione

Segui questi passaggi nell'ordine indicato per configurare e avviare il progetto.

### Passaggio 1: Clonare il Repository

1.  Crea una cartella sul tuo computer dove desideri salvare il progetto.
2.  Entra nella cartella appena creata.
3.  Fai clic con il tasto destro del mouse all'interno della cartella e seleziona **"Git Bash Here"** per aprire un terminale Git.
4.  Nella finestra di Git Bash, esegui il comando:
    ```bash
    git clone https://github.com/msabetta/selenium_python_project.git
    ```

### Passaggio 2: Attivare l'Ambiente Conda

1.  Dal menu di avvio di Windows, apri l'applicazione **"Anaconda Prompt (Anaconda3)"**.
2.  Nella finestra del prompt, spostati nella directory del progetto clonato (se necessario). Ad esempio:
    ```bash
    cd percorso/della/tua/cartella/selenium_python_project
    ```
3.  Attiva l'ambiente Conda specifico per il progetto (incluso nel repository):
    ```bash
    conda activate envs\test-automation
    ```
    *Nota: Questo comando presume che l'ambiente `test-automation` sia già stato creato e salvato nella cartella `envs` del progetto. In caso contrario, potrebbe essere necessario crearlo manualmente.*

### Passaggio 3: Eseguire lo Script Principale

Sempre nell'Anaconda Prompt con l'ambiente attivato, esegui:
```bash
python main.py
```

Lo script inizierà l'esecuzione. Dovrebbe aprire una finestra del browser (Chrome) e compiere le azioni programmate.

## 📁 Struttura del Progetto

*   **`main.py`**: Script principale che contiene la logica di automazione con Selenium.
*   **`chromedriver/`**: Cartella contenente il driver eseguibile per Google Chrome, necessario per far comunicare Selenium con il browser.
*   **`images/`**: Probabilmente contiene screenshot o risorse grafiche usate dallo script o per la documentazione.
*   **`set_envs.bat`**: Script batch per semplificare la configurazione delle variabili d'ambiente su Windows.

## 🛠️ Cosa fa lo Script (`main.py`)?

Basandosi sui commit ("fix ignore ssl webdriver option", "wait clickable cookie message button"), lo script probabilmente:

1.  Configura il driver di Chrome con opzioni specifiche (es. ignorare errori SSL).
2.  Apre una o più pagine web.
3.  Attende che elementi specifici della pagina (come un bottone per accettare i cookie) diventino cliccabili.
4.  Esegue azioni come click, compilazione di moduli o estrazione di dati.
5.  Alla fine, chiude il browser in modo pulito (`driver.quit()`).

## ⚠️ Note e Risoluzione Problemi

*   Assicurati che la versione del **ChromeDriver** nella cartella `chromedriver` sia compatibile con la versione di Google Chrome installata sul tuo sistema.
*   Se l'ambiente Conda `test-automation` non è presente, puoi crearlo manualmente con:
    ```bash
    conda create --prefix ./envs/test-automation python=3.8
    conda activate ./envs/test-automation
    pip install selenium webdriver-manager
    ```
*   Per problemi di esecuzione, verifica che tutti i percorsi (path) siano corretti e che il firewall non blocchi il driver.

## 🤝 Contributi

Se desideri migliorare lo script o aggiungere nuove funzionalità, sentiti libero di aprire una **Issue** o una **Pull Request**.
