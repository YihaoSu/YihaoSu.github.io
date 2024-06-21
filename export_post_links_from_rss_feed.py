import feedparser

feed_source = 'https://4everland.io/ipns/astrobackhacker.eth/rss.xml'
d = feedparser.parse(feed_source)
entries = d['entries']

with open('contents.lr', 'w') as file:
    for e in entries:
        file.write(f"* [{e.get('title')}]({e.get('link')})\n")
