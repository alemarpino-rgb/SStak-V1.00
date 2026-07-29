# SStak

Supporto per il linguaggio [SStak](https://github.com/ale-marpino/dante) in Visual Studio Code: syntax highlighting, snippet e configurazione base dell'editor (parentesi, commenti) per i file `.SStak`.

## Cos'è SStak

SStak è un linguaggio interpretato basato su stack e notazione polacca inversa.

```text
1 1 DUP +
DUP( 0 1 ) + SHOW
DUP( 1 2 ) +
```

```text
1, 2, 3,
stack = [1, 2, 3, 5, 8, 13, 21, 34]
```

## Funzionalità

- Evidenziazione della sintassi per numeri, parole chiave (`REP DUP SHOW DEL DELALL LOAD REM PICK Stack`), operatori aritmetici (`+ - * / ++ -- ** //`), commenti a blocco `^^ ... ^^`, stringhe `: ... :` e input `:? ... ?:`.
- Chiusura automatica di parentesi `(` `)` e `[` `]`.

## Requisiti

Per eseguire i programmi SStak serve Python installato; l'interprete e le istruzioni di esecuzione sono nel progetto SStak.

## Release Notes

### 0.0.1

Prima versione: syntax highlighting per file `.SStak`.
