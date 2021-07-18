import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_csv('data/raw/ames_housing_data.csv')
max_price = df['SalePrice'].max()+50
min_price = df['SalePrice'].min()
bins = np.linspace(min_price, max_price, 60)
inds = np.digitize(df['SalePrice'], bins)
price_groups = [bins[inds[i]] for i in range(df['SalePrice'].size)]
df['price_groups'] = np.round(price_groups)

df['log_price'] = np.log(df['SalePrice'])
max_price_log = df['log_price'].max()+.01
min_price_log = df['log_price'].min()
bins_log = np.linspace(min_price_log, max_price_log, 60)
inds_log = np.digitize(df['log_price'], bins_log)
price_groups_log = []
for i in range(df['log_price'].size):
    price_groups_log.append(bins_log[inds_log[i]])
df['log_price_groups'] = price_groups_log

st.title('Ames Housing Project')

st.write(df.head(10))
st.bar_chart(df['price_groups'].value_counts())
st.subheader('Log Transformation')
st.bar_chart(np.round(df['log_price_groups'], 2).value_counts())


#st.bar_chart(hist_vals2)