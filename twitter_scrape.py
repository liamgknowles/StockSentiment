import twint


def twintfunc(ticker, dates=[]):
    tweet_dict = {}

    for i in range(len(dates) - 2):
        # Configure
        c = twint.Config()
        c.Limit = 20
        c.Popular_tweets = True
        c.Store_object = True
        c.Hide_output = True
        c.Search = "$" + ticker
        c.Since = dates[i]
        c.Until = dates[i + 2]

        # Run
        twint.run.Search(c)
        tweets = twint.output.tweets_list

        tweet_dict[dates[i]] = [t.tweet for t in tweets[:20]]

    return tweet_dict


if __name__ == "__main__":
    ticker = 'aapl'
    dates = ['2020-3-16', '2020-3-17', '2020-3-18', '2020-3-19', '2020-3-20']
    res = twintfunc(ticker, dates)

    # saving to a file and printing the output
    file = open('{}.txt'.format(ticker), 'w')
    for k, v in res.items():
        print(k)
        file.write(k+'\n')
        for i in v:
            print(i)
            file.write(i+'\n')
        print('\n\n')
        file.write('\n\n')
    file.close()
