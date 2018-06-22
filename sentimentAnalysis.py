from tkinter import *
from textblob import TextBlob
import tweepy
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

tweets_list=list()
root=Tk();
"""text=Text(root);
text.pack(expand="yes", fill='both')

f = Figure(figsize=(5,5), dpi=100)
a = f.add_subplot(111)
"""
Consumer_Key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
Consumer_Secret='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
Access_Token='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
Access_Token_Secret='XXXXXXXXXXXXXXXXXXXXXXXXXXX'
def submit():
	tweets_list.clear()
	labels= 'Negative', 'Positive', 'Neutral'
	colors=['red','blue','yellow']
	counts=list()
	explode=(0,0.1,0)
	auth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
	auth.set_access_token(Access_Token,Access_Token_Secret)
	api=tweepy.API(auth)
	search_string=e1.get()
	number=e2.get()	
	tweets_list.extend(api.search(lang="en",q=search_string + " -rt",count=number,result_type="recent"))
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
		print(tweets.text.encode('utf-8'))
		print(sentiments)
	print("Total number of tweets:")
	print(total)
	counts.append(negative)
	counts.append(positive)
	counts.append(neutral)
	plt.pie(counts,explode=explode,labels=labels,colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
	plt.axis('equal')
	plt.show()

def show():
	label.config(text=("\n".join(list_of_items)))

Label(root , text="Welcome to sentiment analysis website").grid(row=0)
Label(root, text="Term to be analyzed").grid(row=1)
Label(root, text="Number of tweets to be analysed").grid(row=2)

e1 = Entry(root)
e2 = Entry(root)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

Submit=Button(root,text="SUBMIT",command=submit)

Submit.grid(row=3,column=1)	

Button(root,text="SHOW TWEETS",command=show).grid()
root.geometry('700x1000')
root.mainloop();
