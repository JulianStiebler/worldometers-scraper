# worldometers-scraper
 Scrapes all data about corona from https://www.worldometers.info/coronavirus/ and creates a folder named by day with a html table and csv file with the data.
 
# Usage

## Requirements are:
> Pandas, requests, bs4 (BeautifulSoup4)

Open a cmd-window, preferably in the directory u plan to place the script to save further work. A fast way to do that is to left-click the adressbar while having open the folder with the script and type "cmd". Type:
> py -m pip install pandas requests bs4

## Usage

> py corona-scraper.py

in a cmd-window to use it. It will create a folder named by day with a html table and csv file with the data.