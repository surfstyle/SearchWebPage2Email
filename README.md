  
# SearchWebPages2Email
Web scaping notification for general web site configured in .json
  

## Notes
Documentation:  
  
Esiste un file json con dei parametri perche' il programma sia parametrizzabile e modulabile.  
Il programma di lancio deve leggere i parametri e chiamare gli altri con i parametri letti.  
Il programma di ricerca recupero il testo della pagina url ed esegue al suo interno una ricerca per delle keywords. Per ogni keyword trovata copia le precedenti e seguenti 2 righe in un file di testo txt.  
Il programma di notifica prepara una email con FROM, TO, e un SUBJECT passato come parametro. Il body è letto dal file prodotto dal programma di ricerca. Invia la email.  
  
  
1) script che esegue un recupero della pagina web   
lo script è parametrizzato in modo che i parametri sono passati in un filetxt con la chiamata script  
Es. eseguo un cron schedulato di time mioScript.py config-XYZ.txt  
permette la riusabilita dello script  
la pagina web viene recuperata, ci si appoggia alla libreria BeautifulSoup per convertire l html in testo  
il testo viene scandagliato per cercare le keywords passate come parametri  
per ogni key viene salvato le precedenti e successive 2 righe  
tutte le ricerche vengono salvate in un file txt il cui nome è nel config  
2) dal file txxt un programma legge il file, se vuoto non esegue niente  
se contiene testo allora invia una email con lo script email come notifica  
uno script generale chiama il primo prg, poi il secondo e termina  
  

## Install
pip install > beautifulsoup4  
  
ToDo:  
-valutare installazione su Docker dedicato a scripp  

  
  