from base import Engine as m
import json
from bs4 import BeautifulSoup


host = 'https://tumanhwas.com/'


def main():
    # ** Main function to get the last updates **

    body = m.Engine.navigate(host).find_all('div', 'listupd')[0]

    # get Titles
    titles = body.find_all('div', 'tt')
    listSeries = {}

    # get Series
    seriesContainer = body.find_all('div', 'bsx')

    for serie in seriesContainer:
        # get Title
        title = serie.find('div', 'tt').text.strip()
        listSeries[title] = {}

        # get Url
        urlSerie = serie.find('a')['href'].strip().split('leer')[1][1:]
        urlSerie = urlSerie.split('-')
        urlSerie = ' '.join(urlSerie)
        urlSerie = '-'.join(urlSerie.split(' ')[:-1])
        urlSerie = host + 'manga/' + urlSerie

        listSeries[title]['url'] = urlSerie

        # get Image
        image = serie.find('img')['src'].strip()
        listSeries[title]['image'] = image

        # get last Chapter
        # *title
        chapterName = serie.find('div', 'epxs').text.strip()
        # *link
        chapterLink = serie.find('a')['href'].strip()

        chapterList = {}
        chapterList['name'] = chapterName
        chapterList['url'] = chapterLink
        listSeries[title]['last_chapter'] = chapterList

    result = {}
    result['last_updates'] = listSeries
    return json.dumps(result, indent=4, ensure_ascii=False).encode('utf-8')
