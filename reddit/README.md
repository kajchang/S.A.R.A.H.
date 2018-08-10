# S.A.R.A.H.

A Discord Bot for the [NovaBlitz](https://novablitz.com/) card game.

Live on Reddit at [Nova_Sarah](https://www.reddit.com/user/Nova_Sarah).

The bot will respond to any comment with a card name between brackets on the [NovaBlitz subreddit](https://reddit.com/r/NovaBlitz) using the [NovaBlitz API](https://documenter.getpostman.com/view/4967569/RWTivyzL).

## Example

<img src="https://github.com/kajchang/SARAH/raw/master/reddit/images/example.png" height="250"/>


## Deploying

You will need the create a [script application](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) on Reddit.

```bash
$ git clone https://github.com/kajchang/S.A.R.A.H..git
$ cd S.A.R.A.H./reddit
$ pip install -r requirements.txt```

In the `reddit` folder, create a file called `secrets.json` and populate it with the authentication data:

```json
{
	"client_id": "XXXXXX",
	"client_secret": "XXXXXX",
	"user_agent": "XXXXXX",
	"username": "XXXXXX",
	"password": "XXXXXX"
}
```

Finally, you can run `SARAH.py`.
