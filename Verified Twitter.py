import pandas as pd
from itertools import islice
import time
import twint

def twintfunc(ticker, sdate, edate):
    ''' return the stock tweets satisfying given conditions from start to end date
    Args:
        ticker (str): stock ticker symbol
        sdate (str): start date to scrape tweets
        edate (str): end date to scrape tweets
        
    Returns:
        tweets (list): list of stock tweets in given date range
    '''
    # Configure
    c = twint.Config()
    query = '$' + ticker + ' OR ' + '$' + ticker.lower()
    c.Search = query  #what to search
    c.Since = sdate  # the start date
    c.Until = edate  # the end date
    c.Verified = True  # verified user tweet
    #c.Min_likes = 10
    c.Hide_output = True  #dont print anything
    c.Store_object = True  #store the tweets

    # Run
    twint.run.Search(c)
    tweets = twint.output.tweets_list

    return tweets


def compile_tweets(ticker, date_range):
    ''' compile the components of the tweets into a dataframe
    
    '''
    text = []
    ds = []
    username = []
    likes = []
    
    # use weekly ranges to extract verified tweets
    for dates in date_range:
        sdate = dates[0]
        edate = dates[1]
        print(edate)
        time.sleep(1)
        tweets = twintfunc(ticker, sdate, edate)
        
        # extract needed components of the tweets
        for tweet in tweets:
            text.append(tweet.tweet)
            ds.append(tweet.datetime)
            username.append(tweet.username)
            likes.append(tweet.likes_count)
    
    # form into dictionary for simple conversion to dataframe
    df_dict = {'date':ds, 'username':username, 'likes':likes, 'tweet':text}
    
    return pd.DataFrame(df_dict)


if __name__ == "__main__":
    
    # create weekly date range splits in 2019 using islice
    # https://www.geeksforgeeks.org/python-itertools-islice/
    dates_2019 = pd.date_range('2019-01-01', '2019-12-31').strftime('%Y-%m-%d')
    split = [7] * 51
    split.insert(0, 6)
    split.append(2)
    
    Input = iter(dates_2019)
    output = [list(islice(Input, elem)) for elem in split]

    # create list of date ranges
    date_range = []
    for item in output:
        date_range.append([item[0], item[-1]])
    
    # generate verified stock tweet dataframe for each stock
    stock_df = compile_tweets('aapl', date_range)
    stock_df.to_csv('AAPL_verified.csv')
