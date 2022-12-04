import scrapy
from scrapy_selenium import SeleniumRequest
from scrapy.loader import ItemLoader
from ..items import PokemonItem


class PokebuSpider(scrapy.Spider):
    name = 'pokebu'
#'document.getElementsByClassName("pokemon-list__load-more__button size-14")[0].click()'

    def start_requests(self):
        url = 'https://vn.portal-pokemon.com/play/pokedex'
        yield SeleniumRequest(url=url, callback=self.parse,
                              script='''
                                var buttons = document.getElementsByClassName('pokemon-list__load-more__button size-14');
                                for(var i = 0; i < 1000; i++)  
                                    buttons[0].click();''')

    def parse(self, response):
        links = response.xpath("/html/body/div/div/div[4]/div[2]/div/div")

        for r in links:
            poke = ItemLoader(item=PokemonItem(),
                              response=response, selector=r)
            poke.add_xpath('name', ".//a/span[2]/text()")
            poke.add_xpath('img', ".//a/img/@src")
            poke.add_xpath('he1', ".//a/div/div[1]/span/text()")
            poke.add_xpath('he2', ".//a/div/div[2]/span/text()")
            yield poke.load_item()
