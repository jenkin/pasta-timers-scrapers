# Pasta Timers Scrapers

[Pasta Timers](https://github.com/jenkin/pasta-timers-app) mostra i tempi di cottura raccomandati per le tipologie e i marchi di pasta più comuni sul mercato.

![screenshot](https://repository-images.githubusercontent.com/214686946/4b0a8980-ed27-11e9-827f-88954c137291)

Questi sono gli scraper per scaricare le informazioni rilevanti dai siti dei produttori e generare il database.
Il progetto è scritto in Python 3 ed è basato su [Scrapy](https://scrapy.org/).

## Requisiti

Python 3, [pipenv](https://pipenv.kennethreitz.org/en/latest/), [scrapy](https://scrapy.org/).

## Come si installa

* Clona questo repository: `git clone https://github.com/jenkin/pasta-timers-scrapers.git`.
* Entra nella cartella di progetto: `cd pasta-timers-scrapers/`.
* Attiva il virtualenv: `pipenv shell && pipenv install`.

## Come si usa

* Se non l'hai fatto, attiva il virtualenv: `pipenv shell`.
* Usa lo script fornito per lanciare gli scraper: `bash scrape.sh [nome scraper]`.
  * `Barilla`
  * `Garofalo`
  * `"De Cecco"`
* Controlla i risultati in formato json nella cartella `pasta/data/`.

## Garanzie

Questa applicazione viene fornita così com'è, senza garanzie di alcun tipo, esplicite o implicite.
In nessun caso gli autori o i titolari del copyright saranno responsabili per qualsiasi reclamo, danno o altro tipo di responsabilità.

## Copyright

Tutti i marchi registrati e tutte le immagini e i loghi sono dei rispettivi proprietari.

## Licenze di riutilizzo

Il codice sorgente di questa applicazione è rilasciato in open source con licenza <a href="https://tldrlegal.com/license/mit-license" rel="noopener noreferrer" target="_blank">MIT</a>.
Il database dei tempi di cottura della pasta (file timers.json) è rilasciato con licenza <a href="https://tldrlegal.com/license/odc-open-database-license-(odbl)" rel="noopener noreferrer" target="_blank">ODbL</a>.

## Contatti

Per segnalare malfunzionamenti, suggerire una modifica o fare una domanda puoi aprire una issue sul repository del progetto su <a href="https://github.com/jenkin/pasta-timers-scrapers/issues" rel="noopener noreferrer" target="_blank">Github</a>.
