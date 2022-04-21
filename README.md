# Property Search
Project created for automation property sales search process. Program uses Selenium and BeautifulSoup to collect all needed data from https://www.otodom.pl first page and create possible google sheet if necessary. In order for project to work, all necessary filters must be provided.      


### Steps:
1. Go to https://www.otodom.pl and filter your search.
2. Create your own google form with address, price and link.
3. Set environment variables.
4. Run the code.

####ENV vars:
- CHROME_DRIVER_PATH - path to your ChromeDriver
- GOOGLE_FORM_LINK - link to your previously created google form
- OTODOM_LINK - link to your Otodom search

### How to run 
```
export CHROME_DRIVER_PATH=""
export GOOGLE_FORM_LINK=""
export OTODOM_LINK=""
python3 main.py
```

**exception**: program only works for property sales search **not rental search**
