import json
import mongoengine as me
from models import Author, Quote

me.connect('8th_hw', host='mongodb+srv://mmmunchkin:mongolia123@atlascluster.mhfficr.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster')

def load_authors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        authors = json.load(file)
        for author_data in authors:
            author = Author(**author_data)
            author.save()

def load_quotes(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        quotes = json.load(file)
        for quote_data in quotes:
            author_name = quote_data.pop('author')
            author = Author.objects(fullname=author_name).first()
            if author:
                quote_data['author'] = author
                quote = Quote(**quote_data)
                quote.save()

if __name__ == '__main__':
    load_authors('authors.json')
    load_quotes('quotes.json')
