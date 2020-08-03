# Scraper

Scraper is a terminal web-scraper, which does content from url more readable.

### How it works. Several steps

  1. Scraper gets html content from url 
  2. Clears it from tags, unnecessary garbage and so on
  3. Formats the content, according set format (currently formatting supported only for links)
  4. Saves the content to file with path, which gotten from url (for instance, https://microsoft.com/ -> ".\microsoft.com\index.txt")


You can also:
  - Set content line length
  - Get logs from stdout

### Libs

Scraper uses the follow libraries:

* json - to load config file from json
* argparse - to get arguments from terminal to run
* requests - to get html-content from url
* re - to search tags, links and expressions in html-content
* pathlib - to save file in the path from url

### How to run

To run scraper using terminal, it is necessary to have Python with 3.7+ version. When it will be installed, you can run scraper.

Sample: 
`python main.py --url "https://habr.com/ru/post/446816/"`
or
`python main.py -u "https://habr.com/ru/post/446816/"`

### Todos

 - Write Tests
 - Add support for relative links
 - Extend support for html tags
 - Add pagination for scraper.py module
 - Refactor/extend the content formatting logic
 - Add a more informative logger
