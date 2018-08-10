import praw
import json
import sqlite3
import os
import re
import requests
import time


def is_responded(comment_id):
    return bool(c.execute('SELECT * FROM "COMMENTS" WHERE "COMMENT_ID" = ?', (comment_id,)).fetchone())


def respond(comment):
    for match in re.findall('\[\[(.*?)\]\]', comment.body):
        r = requests.get(
            'http://novablitz.pythonanywhere.com/cards/{}'.format(''.join(match.split())))
        if r.status_code == 200:
            card_data = r.json()
            if card_data['type'] == 'Unit':
                comment.reply('''[{name}]({image}) - {type} - {set}

Costs {cost} Energy - {attack}/{health} - {text}'''.format(**card_data))

            else:
                comment.reply('''[{name}]({image}) - {type} - {set}

Costs {cost} Energy - {text}'''.format(**card_data))

            time.sleep(6)

    c.execute('INSERT INTO "COMMENTS" VALUES (?)', (comment.id,))
    conn.commit()


def main():
    for comment in reddit.subreddit('NovaBlitz').stream.comments():
        if re.search('\[\[(.*?)\]\]', comment.body) and not is_responded(comment.id):
            respond(comment)

    time.sleep(6)


if __name__ == '__main__':
    with open('secrets.json') as secrets_file:
        secrets = json.load(secrets_file)

    reddit = praw.Reddit(**secrets)

    if not os.path.exists('comments.db'):
        conn = sqlite3.connect('comments.db')
        c = conn.cursor()
        c.execute(
            'CREATE TABLE COMMENTS (COMMENT_ID CHAR(7) NOT NULL, PRIMARY KEY (COMMENT_ID))')

    else:
        conn = sqlite3.connect('comments.db')
        c = conn.cursor()

    main()
