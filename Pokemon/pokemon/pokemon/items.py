# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from scrapy.loader.processors import TakeFirst, MapCompose, Join

def img_join(img):
    url = "https://vn.portal-pokemon.com"
    if (img):
        url += img
        return url
    else :
        return "Not have src"

class PokemonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field(output_processor = TakeFirst())
    img = scrapy.Field(input_processor=MapCompose(img_join), output_processor = TakeFirst())
    he1 = scrapy.Field(output_processor = TakeFirst())
    he2 = scrapy.Field(output_processor = TakeFirst())
   
