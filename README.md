# generatore di query per popolazione di database mysql
 Il titolo dice tutto, utile se sei pigro come me.
 Questo piccolo programma genera delle query di popolazione per 
 **mysql**.

# Installazione
Clicca sul pulsante verde in alto a destra e poi su "scarica come zip", estrailo, modifica solo il file `main.py` ed eseguilo. <br>
Nota bene: hai bisogno di python3 installato per farlo funzionare.
# Utilizzo
Apri il file *main.py* e modifica l'array `struttura` con i seguenti elementi:

- `nome()` nome scelto a caso da una lista.
- `cognome()` cognome scelto a caso da una lista (la lista comprende anche cognomi presenti in italia ma non italiani).
- `intero(max, min)`  genera un numero intero incluso tra un massimo ed un minimo. Il minimo è opzionale.
- `decimale(max, min, decimali)` genera un numero decimale incluso tra un massimo ed un minimo. Il minimo è opzionale. decimali è il numero di cifre decimali, default = 2.
- `data(min, max)` genera una data nel formato accettato da mysql, min e max vanno espressi in **ANNI** e sono opzionali.
- `dataora(min, max)` genera una data con ora nel formato accettato da mysql, min e max vanno espressi in **ANNI** e sono opzionali.
- `sequenzaInteri(max, min)` genera una sequenza di interi, se le iterazioni sono maggiori del numero max la seqeuenza riparte dal min. Il default di min è 0.
- `sequenzaStringhe(["array", "di", "stringhe"])` sequenzaInteri(max, min) genera una sequenza di interi, se le iterazioni sono maggiori del numero max la seqeuenza riparte dal min. Il default di min è 0.
- `randomStringhe(["array", "di", "stringhe"])` sceglie dall'array dato come argomento una stringa a caso e la inserisce.

# Altre impostazioni

- `iterazioni` il numero di record da generare
- `tabella` il nome della tabella dove inserire i record
- `campi` il nome dei campi dove inserire dati, lasciare vuoto per inserire in tutti i campi

# Esempio
**Input:**

```
struttura = [nome(), cognome(), intero(31, 18), data(1990, 2002), randomStringhe(["Roma", "Milano", "Napoli"])]
iterazioni = 3
tabella = "persone"
campi = "nome, cognome, eta, dataNascita, citta" 
#MODIFICA QUA SOPRA

print(generaQuery(struttura, iterazioni, tabella, campi))

```
**Output:**
```
insert into persone (nome, cognome, eta, dataNascita, citta) values("omar", "Fusco", 28, "1999-08-22", "Roma"), ("adriano", "Silvestri", 27, "1992-11-09", "Roma"), ("roberto", "pereira de castro", 28, "1991-05-05", "Milano");
```
Come vedi ha generato una serie di dati coerenti con le impostazioni che abbiamo passato al programma. E' necessario notare come non appaiano tutte e 3 le città scelte da noi, in quanto casualmente è stata scela due volte roma.

# Come posso aiutare?

Se pensi che possa mancare qualcosa apri una issue, cercherò di implementare la funzione il prima possibile.

# Note:
- La lista di nomi e cognomi sono stati presi da due repository su github, non ricordo bene quali, se li ritrovo li cito
- La funzione per il calcolo della data è stata palesemente rubata da stackoverflow
- La licenza è un meme

# Help! I can't speak italian!

Sorry mate, i don't think i will translate the readme or even the script in english. However, is pretty easy to uderstand so you should be able to make it work even without instructions.