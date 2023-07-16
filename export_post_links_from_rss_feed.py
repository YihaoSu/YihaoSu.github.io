import feedparser

# feed_source = 'https://mirror.xyz/astrobackhacker.eth/feed/atom'
# feed_source = 'https://cloudflare-ipfs.com/ipns/astrobackhacker.eth/rss.xml'
feed_source = 'https://astrobackhacker.eth.limo/rss.xml'
d = feedparser.parse(feed_source)
entries = d['entries']

with open('contents.lr', 'w') as file:
    for e in entries:
        file.write(f"* [{e.get('title')}]({e.get('link')})\n")
