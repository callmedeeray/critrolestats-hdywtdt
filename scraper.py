# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
from lxml import html
import requests


# # Read in a page
# html = scraperwiki.scrape("https://www.critrolestats.com/dmcrits-wm")  
## need everything in the <ol> elements with class c6

##root = fromstring(page.content)
##print [child.tag for child in root.iterdescendants()]


page2 = requests.get('https://docs.google.com/document/d/e/2PACX-1vTNv_QeiT5PlIM8-XalUlW06QzHjwhkO-WiybYEvFF9GAu1Hhxq1u8T68IpxH4tUmoxdZjObmSE1kGG/pub?embedded=true')
tree2 = html.fromstring(page2.content)


hdywtdt = tree2.xpath('//ol//span/text()')


for hdy in hdywtdt:
    ind = hdy.find('(')
    char = hdy[0:ind-1]
    ind2 = hdy.find(')')
    epinfo = hdy[ind+1:ind2]
    onwhat = hdy[ind2+2:len(hdy)]
    if char.find(' and ') > -1:
        char1, char2 = char.split(' and ')
        dat1 = {'character': char1, 'episode info': epinfo, 'killed what': onwhat, 'kills': 0.5, 'full string': hdy}
        scraperwiki.sqlite.save(unique_keys=['full string'], data = dat1)
        dat2 = {'character': char2, 'episode info': epinfo, 'killed what': onwhat, 'kills': 0.5, 'full string': hdy}
        scraperwiki.sqlite.save(unique_keys=['full string'], data = dat2)
    else:
        dat = {'character': char, 'episode info': epinfo, 'killed what': onwhat, 'kills': 1, 'full string': hdy}
        scraperwiki.sqlite.save(unique_keys=['full string'], data = dat)


        




#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("ol[class='c6']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
