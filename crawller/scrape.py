from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import lxml
from lxml import etree


def get_photolist():
	photo_list = []
	url = 'https://pixabay.com/zh/photos'
	html = requests.get(url)
	bsObj = BeautifulSoup(html.text, 'html.parser')
	scope = bsObj.find_all('div', {'class': 'item'})
	if len(scope) == 0:
        return None
    for i in scope:
        lazy = i.find('img')
        if lazy['src'] != '/static/img/blank.gif':
            if lazy['src'] in photo_list:
                return photo_list
            else:
                photo_list.append(lazy['src'])
        else:
            photo_list.append(lazy['data-lazy'])


        if len(photo_list) >= download_num:
            return photo_list
get_photolist()

