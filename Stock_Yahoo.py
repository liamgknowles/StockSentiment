import requests
import codecs

def download_file(url, filename):
    r = requests.get(url)
    with open('data/'+filename+'.csv', "wb") as code:
        code.write(r.content)
        print("download the ", filename)

def merge(filenames):
    allData = codecs.open('merge.csv', 'w', encoding='utf-8')
    #write the head
    head = ['Data', 'Open', 'Close', 'Adj Close', 'Company', 'Industry', 'Stock ticker']
    allData.write(','.join(head)+'\n')
    for industry in filenames.keys():
        for company in filenames[industry]:
            text = codecs.open('data/'+company[1]+'.csv', 'r', encoding='utf-8')
            next(text)
            for line in text:
                line = line.strip().split(',')
                data = list()
                data.append(line[0])
                data.append(line[1])
                data.append(line[4])
                data.append(line[5])
                data.append(company[0])
                data.append(industry)
                data.append(company[1])
                allData.write(','.join(data)+'\n')

if __name__ == '__main__':
    filenames = {
        'Basic Materials':[('Linde plc', 'LIN'), ('Air Products and Chemicals, Inc.', 'APD'), ('Ecolab', 'ECL'), ('International Paper', 'IP')],
        'Consumer Cyclical':[('Amazon', 'AMZN'), ('General Motors', 'GM'), ('Marriott Intl', 'MAR'), ('Starbucks', 'SBUX')],
        'Industrial':[('3M Company', 'MMM'), ('American Airlines Group', 'AAL'), ('Boeing Company', 'BA'), ('General Electric', 'GE')],
        'Technology':[('Apple', 'AAPL'), ('Nvidia', 'NVDA'), ('Oracle', 'ORCL'), ('Microsoft', 'MSFT')],
        'Utilities':[('Dominion Energy', 'D'), ('NextEra Energy', 'NEE'), ('Southern Company', 'SO'), ('Eversource Energy', 'ES')],
        'Financial services':[('JP Morgan', 'JPM'), ('Wells Fargo', 'WFC'), ('Berkshire Hathaway', 'BRK'), ('StateStreet', 'STT')],
        'Real Estate':[('American Tower Corp.', 'AMT'), ('Boston Properties', 'BXP'), ('Equity Residential', 'EQR'), ('Crown Castle', 'CCI')],
        'Healthcare':[('Amgen', 'AMGN'), ('Biogen', 'BIB'), ('Pfizer', 'PFE'), ('Johnson & Johnson', 'JNJ')],
        'Communication Services':[('AT & T', 'T'), ('Comcast', 'CMCSA'), ('Verizon','VA'), ('T - Mobile','TMUS')],
        'Energy': [('Chevron', 'CVX'), ('Exxon', 'XOM'), ('Devon', 'DVN'), ('Kinder Morgan', 'KMI')]
    }
    #download the all data
    # for industry in filenames:
    #     for company in filenames[industry]:
    #         ticker = company[1]
    #         url = "https://query1.finance.yahoo.com/v7/finance/download/"+ticker+"?period1=1420070400&period2=1577750400&interval=1d&events=history&includeAdjustedClose=true"
    #         download_file(url, ticker)

    #merge the all data
    merge(filenames)
