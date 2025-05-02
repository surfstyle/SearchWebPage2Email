  
# SearchWebPages2Email
The main scope is scraping **not-complex websites** that periodically update content (like posts) for finding target keywords. 
The script collect data from a webpage, trasform html into text, search lines with specific keywords, notify (email) of new content.  

  
Advice: The scraping can be made on **simple webpages** where the main content is inside a simple body. Increasing the complexity of the website, is more difficult to have a correct scrape. You can test the scraped output in a saved file .txt and then opt if you can search correctly your keywords inside it.
  

## How is working
- Every scraping of a website is configured in a .json file (url, keywords, outputfile ...). You can create multiple .json for multiple sites.
- The single scraping return the data of the page. Then a search rescues the lines that matches the keywords. For every line founded are saved also the previous and next 2 lines for giving a context to the search
- The result from the scraping is notified to an email
  
  
  
## How to use
### Dependencies
Need BeatifulSoup for converting html to text
<pre>
pip install beautifulsoup4
</pre>
  
  
### Creating file .env
Create inside the folder a file *.env*
<pre>
# .env

# General
APP_PATH=/home/me/Scripts/SearchWebPage2Email/

# Email
APP_SMTP_SERVER=smtp.gmail.com
APP_SMTP_PORT=587
APP_SMTP_USERNAME=myaddress@gmail.com
APP_SMTP_PASSWORD=aaaa bbbb cccc dddd
</pre>
  
  
### Configuring website
Every site is configured in a file .json  
Rename the file *"_site1-example.json-test"* in *"_website-1.json"*  
Then personalize it
<pre>
{
  "URL": "https://www.myurl.com/something/other",
  "KEYWORDS": [
    "word1",
    "word2",
    "word3"
  ],
  "OUTPUT_FILE": "res_myurl.txt",
  "EMAIL-FROM": "myaddress@gmail.com",
  "EMAIL-TO": "address@gmail.com",
  "EMAIL-SUBJECT": "[HomeSrv] My search for www.myurl.com"
}
</pre>
  
  

#### Run it the first time
<pre>
cd /home/me/Scripts/SearchWebPage2Email
</pre>

then start
<pre>
python /home/me/Scripts/SearchWebPage2Email/start.py _website-1.json
</pre>

  
#### Schedule your script
Edit *crontab -e*
with your script many time as the many website you want to scrap
<pre>
*# Scraping site-1 for searching something*
40 00 * * 6 python /home/me/Scripts/SearchWebPage2Email/start.py _website-1.json
*# Scraping site-2 for searching someother*
45 00 * * 6 python /home/me/Scripts/SearchWebPage2Email/start.py _website-2.json
# ....
</pre>