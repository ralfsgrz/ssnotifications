import time
import feedparser
from datetime import datetime
import telegram_send


if __name__ == '__main__':

    old_post = datetime.strptime('Mon, 15 Nov 2021 19:33:24 +0300', '%a, %d %b %Y %H:%M:%S %z')

    while True:
        apartments = feedparser.parse("https://www.ss.lv/lv/real-estate/flats/riga/teika/hand_over/rss/")
        entries = apartments.entries
        for apt in entries:
            last_post = datetime.strptime(apt.published, '%a, %d %b %Y %H:%M:%S %z')
            if last_post > old_post:
                telegram_send.send(messages=["Jauns sludinajums: " + apt.title])
        time.sleep(2400)

    


    




