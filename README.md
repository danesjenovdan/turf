# Parsing comments on rtvslo.si to fight astroturfing

This is a parser for comments on articles found at http://www.rtvslo.si/slovenija/. Set up a cron job and run it every 5 minutes to store comments in JSON files named with the timestamp of the time of parsing.

## Requirements

- python3
- pip
- requests (installed with pip)
- scrapy (installed with pip)
- virtualenv and virtualenvwrapper (to keep things in check)

## Setup

1) `git clone https://github.com/danesjenovdan/turf.git`
2) `mkvirtualenv -p python3 turf`
3) `pip install -r requirements.txt`
4) `chmod +x parse.sh` (run with `./parse.sh`)
5) edit `parse.sh` to provide correct paths to scrapy binary, rtvslo.py, folder to store comments
6) `crontab -e` and add this to your cronfile `*/5 * * * * /path/to/turf/parse.sh` (replace `/path/to` with the actual path to the file)

:tada: You're done! The script will now parse comments every 5 minutes and store them into the appropriate file in `/comments`. :tada:

## Roadmap

Automate analysis of these comments.