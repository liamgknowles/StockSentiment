#!/usr/bin/env python
# coding: utf-8

# In[44]:


import praw
import pandas as pd
import datetime as dt

secret = "pKx-AzAyNWLJvYvRvl1do_yAw9I6iA"
personal_script = "JtB5Q-catE-mvQ"

reddit = praw.Reddit(client_id=personal_script, 
                     client_secret=secret, 
                     user_agent="keywordsearcher", 
                     username="lgksensei", 
                     password="Jhk@3132")


# In[45]:


subreddit = reddit.subreddit('wallstreetbets')
top_subreddit = subreddit.top()
top_subreddit = subreddit.top(limit=500)


# In[46]:


topics_dict = { "title":[], 
                "score":[], 
                "id":[], "url":[], 
                "comms_num": [], 
                "created": [], 
                "body":[]}

for submission in top_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["url"].append(submission.url)
    topics_dict["comms_num"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    
    
topics_data = pd.DataFrame(topics_dict)


# In[48]:


print(topics_data["body"])


# In[ ]:




