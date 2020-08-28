# selenium_python_project

Requisiti di utilizzo:
- Anaconda Individual Edition (https://www.anaconda.com/products/individual#windows)
- Python 3.8 (https://www.python.org/downloads/)
- Git (https://git-scm.com/)

Creazione ambiente operativo
- Creare una cartella di progetto
- Entrare all'interno della cartella e lanciare l'applicazione "Git Bash" (tasto destro del mouse e fare click su "Git Bash Here")
- lanciare il comando "git clone https://github.com/msabetta/selenium_python_project.git" (senza virgolette)
- Terminata la procedura al punto precedente, aprire da menu avvio "Anaconda Prompt (Anaconda3)"
- lanciare il comando "conda activate envs\test-automation" (senza virgolette)

Esecuzione del codice di progetto con Selenium (main.py):
- lanciare il comando "python main.py"

Esecuzione del codice di progetto con Selenium e Pytest (pytest_example.py):
- lanciare il comando "pytest --driver Chrome pytest_example.py"  (esecuzione del codice con Google Chrome)

Esecuzione del codice di progetto con Selenium e Pytest con l'utilizzo della piattaforma Gridlastic (test_unittest.py)
- Dalla pagina web "https://www.gridlastic.com/grid-configuration.php" avviare Gridlastic cliccare sul tasto "Start Grid"
- lanciare il comando "pytest --driver Chrome test_unittest.py"
- Nella dashboard di Gridlastic è possibile accedere a "Selenium Grid" ed al "Selenium Grid Hub Console" ai link riportati in sezione
per ulteriori dettagli sul esito dei test effettuati

NOTE: nel punto precedente vanno inseriti le credenziali "Username" ed "Access Key" per l'accesso a Selenium Grid  

Al termine del test ricordarsi di cliccare su "Terminate Grid" per fermare il Selenium Grid Hub Server in running


