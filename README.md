# News-view

This application lists various sources of news and subsequent highlights in each of the source. clicking an individual highlights takes the user to the article itself for the full story

## By **[Anderson Okiny](https://github.com/opanga77)**

## Description
This news-highlights is a web application that lists various News sources gotten from [News API](https://newsapi.org/). A user can click on a News source and be directed to a page that contains News Articles from the selected News source. The article's title, image, date of publication and preview will be displayed and a user can click on the article to be directed to the source's site to read the entire article.

## User Stories
As a user I would like:
* to see various news sources and select the ones I prefer
* to see all the news articles from that news source
* to see the image, description and time the news article was created.
* to click on an article and read it fully from the news source.


## Prerequisites
* Python3.6


## Setup/Installation Requirements
* internet ac
* git clone 
* $ cd news-view
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = create_app('production') should be app = create_app('development')
* $ ./start.sh

# CREDITS

#### Google.com, StackOverflow.com and moringa school 'study content'



## Known Bugs

No known bugs at the moment

## Technologies Used
- Python3.6
- Flask framework
- Bootstrap (for styling)

