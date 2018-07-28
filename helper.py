import requests as req
from bs4 import BeautifulSoup
import json
import pandas as pd

from key import api_key

lead_sl = 'c8c72ec0-8331-4ccb-949b-bd284d0054db'

url = 'https://data.milwaukee.gov/api/3/action/datastore_search?resource_id='+lead_sl+'&limit=80000'

lead_set = req.get(url, auth=('Authorization', api_key))

soup = BeautifulSoup(lead_set.content,'html.parser')

#print(soup.p.find('{'))

crime_sl = '87843297-a6fa-46d4-ba5d-cb342fb2d3bb'

url_crime = 'https://data.milwaukee.gov/api/3/action/datastore_search?resource_id='+crime_sl+'&limit=700000'

crime_set = req.get(url, auth=('Authorization', api_key))

crime_soup = BeautifulSoup(crime_set.content,'html.parser')
