from tipi import nome, cognome, intero, data, dataora, sequenzaInteri, sequenzaStringhe, randomStringhe, indirizzo, telefono,generaQuery

#MODIFICA QUA SOTTO
struttura = [nome(), cognome(), intero(70, 18), data(1990, 2002), dataora(2020), sequenzaInteri(5, 1), sequenzaStringhe(["questo", "è", "un", "test"]), randomStringhe(["questo", "è", "un", "test"]), indirizzo(), telefono(True)]
iterazioni = 3
tabella = "persone"
campi = "" #separati da virgola
#MODIFICA QUA SOPRA

print(generaQuery(struttura, iterazioni, tabella, campi))

# nome() nome scelto a caso da una lista
# cognome() stessa cosa
# intero(max, min) genera un numero intero incluso tra un massimo ed un minimo. Il minimo è opzionale
# decimale(max, min, decimali) genera un numero decimale incluso tra un massimo ed un minimo. Il minimo è opzionale. decimali è il numero di cifre decimali, default = 2
# data(min, max) genera una data nel formato giusto, min e max vanno espressi in ANNI e sono opzionali
# dataora(min, max) genera una data nel formato giusto, min e max vanno espressi in ANNI e sono opzionali
# sequenzaInteri(max, min) genera una sequenza di interi, se le iterazioni sono maggiori del numero max la seqeuenza riparte dal min. Il default di min è 0
# sequenzaStringhe(["array", "di", "stringhe"]) genera una sequenza di stringhe, se le iterazioni sono maggiori delle stringhe riparte dalla prima.
# randomStringhe(["array", "di", "stringhe"]) sceglie dall'array dato come argomento una stringa a caso e la inserisce
# indirizzo() crea un indirizzo casuale tipo: Via verdi
# telefono() genera un numero di telefono mobile, telefono(True) genera un numero fisso
