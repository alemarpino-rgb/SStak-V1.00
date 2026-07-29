# SStak! Un linguaggio basato su stack
Ho creato il linguaggio SStak per svago e per provare a creare un linguaggio completamente mio. E' un linguaggio interpretato,
basato su stack e notazione inversa polacca. Ha una sintassi molto semplice e basilare. E ho creato anche un'estensione per Vs code per i file .SStak .
## Come iniziare
### Prequisiti:
La versione più recente di python installata.
### Esecuzione:
Per avviare un qualsiasi programma SStak (se all'interno della cartella examples)
```bash
.\run examples/nome_file.SStak
```
## Sintassi del linguaggio

Ecco un piccolo esempio di codice in SStak:

```text
4 1 REP +
^^ viene ignorato! ^^
DUP( 1 2 ) +
DUP( 2 3 ) +
DUP( 3 4 ) +
DUP( 4 5 ) +
DUP( 5 6 ) +
DUP( 6 7 ) +
: La sequenza di Fibonacci è: : SHOW
```
```output
La sequenza di Fibonacci è: 1, 1, 2, 3, 5, 8, 13, 21, 34
```
### Come funziona SStak?
SStak, come si intuisce dal nome è un linguaggio basatosullo stack. Per chi non lo sapesse, lo stack è una lista in cui si aggiungono (push) elementi e si eliminano (pop) elementi.
### Comandi base:
Regole fisse: **tutti i comandi vanno eseguiti con le maiuscole**, **gli spazi sono necessari tranne che tra il comando e la parentesi e nomi di variabili**
1. **Dichiarare una variabile**: "numero", esempio "2" = stack=[2]
2. **Fare calcoli**: "numero numero operatore", esempio "1 1 + o * o - o /" = stack=[2]
3. **Duplicare l'ultimo numero nello stack**: "numero DUP", esempio "1 DUP" = stack=[1, 1]
4. **Duplicare un numero nello stack in base all'indice**: "numero DUP( indice )", esempio "1 5 3 DUP( 1 )"= stack=[1, 5, 3, 5]
5. **Ripetere un numero X volte**: "a b REP", esempio " 3 5 REP" = stack=[5, 5, 5]
6. **Eliminare l'ultimo numero nello stack**: "numero DEL", esempio "2 1 DEL" = stack=[2]
7. **Eliminare l'ultimo numero nello stack in base all'indice**: "numero DEL( indice )", esempio "1 5 3 DEL( 1 )"= stack=[1, 3]
8. **Eliminare tutti i numeri presenti nello stack**: "numero numero DELALL", esempio "1 5 3 DELALL" = stack=[]
9. **Portare in cima un numero in base all'indice**: "a b PICK( indice )", esempio "1 5 3 PICK( 1 )" = stack=[1, 3, 5]
10. **Ricordare il numero in una variabile**: "valore nome REM", esempio "100 variabile REM" = stack=[], mem={'variabile' : 100}
11. **Riprendere e aggiungere variabili ricordate**: "valore1 nome REM   valore1 LOAD", esempio "100 variabile REM variabile LOAD" = stack=[100]
12. **Mostrare gli elementi dello stack**: "numero SHOW", esempio "1 5 3 SHOW" = output="1, 5, 3", stack=[1, 5, 3]
13. **Sommare, Moltiplicare, Sottrarre e Dividere tutti i numeri dello stack da destra a sinistra**: "numero numero numero operatore", esempio "1 34 23 ++ o ** o -- o //" = stack=[58]
14. **Commentare (sia una sola riga che più righe)**: "codice ^^ commento ^^ codice", esempio "2 3 REP ** ^^ ecco un esempio di potenza ^^" = stack=[9]
15. **Sccrivere testi da mostrare all'utente**: ": Scritta vista dall'utente :", si puo' anche stampare un elemento dello stack, esempio ": Sto stampando un elemento dello stack!! Stack[ 2 ] :" = "Sto stampando un elemento dello stack!! 13", oppure andare a capo, esempio ": Ciao £ : : Mondo!! :" = Ciao (a capo) Mondo!!
16. **Creare degli input**: ":? Input ?:", esempio ":? Dimmi un numero ?:" = "Dimmi un numero  3" stack=[3] 

## Come funziona SStak dal punto di vista tecnico
il codice viene passato all'interprete (SStak.py), necessario per far girare SStak. Anche run.cmd è necessario nella cartella del progetto per poter eseguire codice col comando sopra scritto. Entriamo più nel dettaglio. L'interprete funziona in questo modo: il codice viene preso e spezzettato e poi, per ogni parola chiave c'è un blocco di codice che ne definisce le azioni.
## Come eseguire l'estensione
basta andare nella riga di comando della cartella 'estensione' e digitare il seguente comando:
```bash
code --install-extension sstak-0.0.1.vsix
```
### Come utilizzare l'estensione?
E' già stata scaricata col comando qui sopra! Quindi se crei un file .SStak sarà già tutto evidenziato.

## Licenza e Diritto d'Autore

Questo progetto è ideato e sviluppato da **Alessandro Marpino**.

Il codice è distribuito sotto **Licenza MIT**. 
Se utilizzi, modifichi o redistribuisci questo codice:
* **Devi** mantenere l'avviso di copyright originale con il mio nome.
* **Non puoi** ripubblicare il progetto o parti di esso spacciandole per tue.
* **Puoi** modificarlo, integrarlo ed estenderlo liberamente.

Consulta il file [LICENSE](LICENSE) per i dettagli completi della licenza.