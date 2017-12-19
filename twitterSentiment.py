from textblob import TextBlob
import tweepy
Consumer_Key='55HfunDO3D2ZtNf45h10fpI7N'
Consumer_Secret='RMOStDyzUcLAbqi2lIeMJeIplRRrUhnehOjhTHxpY4ge3TFH4R'
Access_Token='938251354602061825-n5zubgcEwgmPehVB74JbRmsLLyGvY76'
Access_Token_Secret='rkbXDA3jiMyJABdZYZxolHp3eD9YJ7DvPzMfCdZ9hKGPY'
auth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
auth.set_access_token(Access_Token,Access_Token_Secret)
api=tweepy.API(auth)
search_string=input("What do you want to perform Sentiment Analysis on?\n")
number=int(input("How many tweets do you want to search for?"))
tweets_list=api.search(lang="en",
   q=search_string + " -rt",
   count=number,
   result_type="recent")
positive=0
negative=0
neutral=0
total=0
for tweets in tweets_list:
	analysis=TextBlob(tweets.text)
	sentiments=analysis.sentiment.polarity
	if sentiments>0.0:
		print("Positive Sentiment:")
		positive=positive+1
		total=total+1
	elif sentiments<0.0:
		print("Negative Sentiment:")
		total=total+1
		negative=negative+1
	else:
		print("Neutral Sentiment:")
		total=total+1
		neutral=neutral+1
	print(tweets.text)
	print(sentiments)
print("Total number of tweets:")
print(total)
print("Positive Tweets:")
print(positive)
print("Negative Tweets:")
print(negative)
print("Neutral Tweets:")
print(neutral)







