import requests as req
from bs4 import BeautifulSoup
import json
import pandas as pd
from standardize import *
from key import api_key

url = 'https://data.milwaukee.gov/api/3/action/datastore_search?resource_id='


def pull_data(url, record_id, api_key, u_text = False):
    '''
    pull data from ckan exploiting row limits and offsets
    '''

    limit = '250000'

    offset = 0

    empty = False

    df = pd.DataFrame()

    while not empty:

        print('offset'+ str(offset))

        url_adj = url+record_id+'&limit='+limit+'&offset='+str(offset)

        records = req.get(url_adj, auth=('Authorization', api_key))

        soup = BeautifulSoup(records.content,'html.parser')


        offset+=250000

        if u_text:

            if not len(pd.DataFrame(pd.read_json(soup.contents[0])).loc['records'].loc['result']):
                return df
            else:
                df = df.append(pd.DataFrame(pd.io.json.json_normalize(pd.read_json(soup.contents[0]).loc['records'].loc['result'])))

        else:

            if not len(pd.DataFrame(pd.read_json(soup.contents[0])).loc['records'].loc['result']):
                return df
            else:
                df = df.append(pd.DataFrame(pd.read_json(soup.contents[0]).loc['records'].loc['result']))
            
        


lead_sl = 'c8c72ec0-8331-4ccb-949b-bd284d0054db'

crime_sl = '87843297-a6fa-46d4-ba5d-cb342fb2d3bb'

cfs_sl = '6b290551-3a5d-4d2b-a95e-2e82c28a0889'

master_prop = '0a2c7f31-cd15-4151-8222-09dd57d5f16d'

ems_18qtr2 = '2208b5e8-3b7a-48bc-97b7-02641a21aa4f'

#crime_df = pull_data(url, crime_sl, api_key)

#lead_df = pull_data(url, lead_sl, api_key)

#master_df = pull_data(url, master_prop, api_key)

#cfs_df = pull_data(url, cfs_sl, api_key)

#can multiprocessing help here?
