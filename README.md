  
# SearchWebPages2Email
Web scaping of a website, search lines with specific keywords, notification (email) of new content. 
  
It's personalized for more website using a configuration of a file .json (website + keywords)

The main scope is scraping not-smart carrer websites for find new jobs that matches keywords.

## How is working
- Every scraping of a website is configured in a .json file (url, keywords, outputfile ...). You can create multiple .json
- The single scraping return the data of the page. Then a search rescues the lines that matches the keywords. For every line founded are saved also the previous and next 2 lines for giving a context to the search
- The result from the scraping is notified to an email
  
Note: the scraping can be made on simple webpages where the main content is captured in a simple body. You can see the output of scraped in a file.txt and then opt if can search correctly your keywords inside this.
  
  
## How to use
### Dependencies
Need BeatifulSoup for converting html to text
<pre>
pip install beautifulsoup4
</pre>
  
  
### Creating file .env
Create a file *.env"*
<pre>
# .env

# General
APP_PATH=/home/headless/Scripts/SearchWebPage2Email/

# Email
APP_SMTP_SERVER=smtp.gmail.com
APP_SMTP_PORT=587
APP_SMTP_USERNAME=myaddress@gmail.com
APP_SMTP_PASSWORD=nngg gghh iioo lkjh
</pre>
  
  
### Configuring website
Every site is configured in a file .json
Rename the file *_site1-example.json-test* in *_website-1.json*

Personalized your research
<pre>
{
  "URL": "https://www.myurl.com/something/other",
  "KEYWORDS": [
    "keyword1",
    "keyword2",
    "keyword3"
  ],
  "OUTPUT_FILE": "res_myurl.txt",
  "EMAIL-FROM": "test@test.it",
  "EMAIL-TO": "metest@test.it",
  "EMAIL-SUBJECT": "[HomeSrv] My search for www.myurl.com"
}
</pre>
  
  

#### Run it the first time
<pre>
cd /home/me/Scripts/SearchWebPage2Email
</pre>

start
<pre>
python /home/me/Scripts/SearchWebPage2Email/launch_program.py _website-1.json
</pre>pre>

  
#### Schedule your script
Edit *crontab -e*
with your script many time as the many website you want to scrap
<pre>
*# Scraping site-1 for searching something*
40 00 * * 6 python /home/me/Scripts/SearchWebPage2Email/launch_program.py _website-1.json
*# Scraping site-2 for searching someother*
45 00 * * 6 python /home/me/Scripts/SearchWebPage2Email/launch_program.py _website-2.json
*# Scraping site-3 for searching somenew*
50 00 * * 6 python /home/me/Scripts/SearchWebPage2Email/launch_program.py _website-3.json
# ....
</pre>