import tweepy

# Set up your Twitter API credentials
consumer_key = "yDXdL2s8Pn0Cu6ds7VjuzJ7Kb"
consumer_secret = "XB1nE3mE9PoB1XJAjO6kaXEJr5qjMfIOz7zKYSfX2ep2Og1bVE"
access_token = "843470773-6VOMSRdakEbdbs4slKkH8UxDdz24qHzkuMxLmxsb"
access_token_secret = "GUPUfIRiw4kxoZn6XUA9P2UKIqCD3sn5EPwBokF02YFyy"

# Authenticate with the API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Search for tweets containing "UCM"
search_results = api.search_tweets(q="UCM")

# Print out the text of the tweets
for tweet in search_results:
    print(tweet.csv)
