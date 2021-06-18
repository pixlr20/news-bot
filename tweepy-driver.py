import tweepy
import json

auth = tweepy.OAuthHandler("FaTc7AUqEfg1bYeOiHiIMTDad", "uD8KFKGFyWNVpdDbb8TEmMO5HYcO5R7mm85xQX3LIMsyvwJaX3")
auth.set_access_token("716292606607667201-ITbAV2WFnla9Uhs3Mc3NLllML4V6heL", "t268gHUr5FZ8oBIFd8fiMkH9tzcspzXmAfpGVCKQFlVsL")

api = tweepy.API(auth)

q = "from:@nytimes"
results = api.search(q=q, result_type="recent")
news = list()
for r in results:
    tweet = dict(r._json)['entities']['urls']
    try:
        news.append(dict(tweet[0])['url'])
    except:
        continue

for story in news:
    print(story)