import urllib, re
from multiprocessing import Pool
from functools import partial

content = urllib.urlopen("http://github.com/languages").read()
ranks = {}

def fetch(lang):
    lang = urllib.unquote(lang)
    sub = urllib.urlopen("http://github.com/languages/" + lang).read()
    matches = re.findall("is the #([0-9]+)", sub)
    if(len(matches) > 0):
        rank = matches[0]
        ranks[int(rank)] = lang
	print(lang + " is " + rank)

if __name__ == '__main__':
    langs = re.findall("/languages/(.+)\"", content)
    p = Pool(45)
    p.map(fetch, langs)
    print(ranks)
