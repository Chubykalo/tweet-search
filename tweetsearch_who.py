## scrape tweets from list from .ods column-------------------

import twint
import pandas as pd

dataframe = pd.read_excel('data/twitterAccountsCongress.ods')
congress = dataframe['handlelist1'].tolist()

for twitter_handle in congress:

    c = twint.Config()
    c.Lang='es'
    c.Search = 'from:@' + twitter_handle + ' oms'
    c.Since = "2020-01-01"
    c.Store_csv = True
    c.Output = "congresstweets2020oms.csv"
    c.Count = True

    twint.run.Search(c)

# print(congress[-1])

## count the number of lines in a CSV file--------------------------------

# import csv
# file = open("congresstweets2020oms.csv")
#
# reader = csv.reader(file)
#
# lines= len(list(reader))
#
# print(lines)

## test run------------------------------------------------------

# import twint
# import pandas as pd
#
#
# congress = ['pablocasado_','santi_ABASCAL']
#
# for twitter_handle in congress:
#
#     c = twint.Config()
#     c.Lang='es'
#     c.Search = 'from:@' + twitter_handle + ' oms'
#     c.Since = "2020-01-01"
#     # c.Store_csv = True
#     # c.Output = "congresstweets2020full.csv"
#     c.Count = True
#
#     twint.run.Search(c)