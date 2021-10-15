# Fizz Bar

## Descrizione

Creare una semplice modellazione di un bar dove l'utente può visualizzare i prodotti e procedere con un ordine.

## Richieste

Creare un sistema di API REST in Python tramite il framework Flask che:

* restituisca la lista dei prodotti (indicati sotto) con relativo prezzo
* poter effettuare un ordine di uno o più prodotti, questa chiamata restituisce all'utente il costo totale dell'ordine

## Vincoli

* ogni prodotto è composto dagli ingredienti: thè, latte, caffè, acqua
* il costo del prodotto è composto dalla somma dei prezzi degli ingredienti:
    * latte: 10 cent ogni 10cl
    * caffe: 20 cent ogni 1g
    * acqua: 5 cent ogni 10cl
    * thè: 15 cent ogni 1g
* abbiamo i seguenti prodotti
    * espresso:
        * 3g di caffè
        * 10cl di acqua
    * americano:
        * 3g di caffè
        * 30cl di acqua
    * thè nero:
        * 3g di thè
        * 30cl di acqua
    * cappucino:
        * 20cl latte
        * 10cl acqua
        * 3g caffe
    * macchiato:
        * 10cl latte
        * 10cl acqua
        * 3g caffe

## Informazioni

* best practice di sviluppo, setup di ambiente e testing vengono valutate come plus
* non è richiesta alcuna memorizzazione su database
* non è richiesta alcuna interfaccia grafica
