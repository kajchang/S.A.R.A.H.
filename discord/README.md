# S.A.R.A.H.

A Discord Bot for the [NovaBlitz](https://novablitz.com/) card game.
Invite me to your server [here](https://discordbots.org/bot/476208085246017536). 

## Available Commands

<img src="https://github.com/kajchang/SARAH/raw/master/discord/images/!card.png" height="250"/>

`!card card-name`

Searches for a card using the [NovaBlitz API](https://documenter.getpostman.com/view/4967569/RWTivyzL).

<img src="https://github.com/kajchang/SARAH/raw/master/discord/images/!nvt.png" height="250"/>

`!nvt`

Gets the latest price for the Nova Token using the [CoinGecko API](https://www.coingecko.com/api/docs/v3).

<img src="https://github.com/kajchang/SARAH/raw/master/discord/images/!play.png" height="250"/>

`!play`

Displays links to the Steam page for NovaBlitz and the signup form for the Mobile Beta.


<img src="https://github.com/kajchang/SARAH/raw/master/discord/images/!info.png" height="250"/>

`!info`

Displays a link to this repository, a way to contact the author, and an invite link for the bot.

## Other Features

The S.A.R.A.H discord bot with also respond with cards if their names are contained in brackets (e.g. [suprise attack]).

## Deploying

You will need a [Discord bot token](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token).

```bash
$ git clone https://github.com/kajchang/S.A.R.A.H..git
$ cd S.A.R.A.H./discord
$ pip install -r requirements.txt
$ export TOKEN='yourtoken'
$ python3 SARAH.py
```
