import streamlit as st
import pandas as pd
import numpy as np
import requests


base_url = "https://phone-specs-api.azharimm.dev/"
top_by_interest_endpoint = 'top-by-interest'
top_by_fans_endpoint = 'top-by-fans'
latest_endpoint = 'latest'
search_endpoint= '/search?query='

def get_data(base_url, endpoint):
    request = requests.get(base_url + endpoint)
    return request.json()

def print_table(data):
    phone_list = []
    for item in data['data']['phones']:
        phone_list.append(item['phone_name'])
    data_frame = {
        'phones': phone_list
    }
    print(phone_list)
    df=pd.DataFrame(data_frame, index= ('%d' % i for i in range(1,len(phone_list)+1)))
    st.dataframe(df)

#main page statistics
data = get_data(base_url, top_by_interest_endpoint)
st.write('TOP BY INTEREST:')
print_table(data)

data = get_data(base_url, top_by_fans_endpoint)
st.write('TOP BY FANS:')
print_table(data)

data = get_data(base_url, latest_endpoint)
st.write('LATEST PHONES:')
print_table(data)


#search phone and get its specs
phone_search=input('Enter phone name: ')

data = get_data(base_url, search_endpoint + phone_search)
st.write('PHONE SPECIFICATIONS:')
print(data)




