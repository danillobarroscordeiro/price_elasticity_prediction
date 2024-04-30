import pandas as pd
import numpy as np
import streamlit as st

df_results = pd.read_parquet('../data/result_elasticity.parquet')
df_results = df_results.set_index('name')
df_elasticity = pd.read_parquet('../data/df_elasticity.parquet')
df_elasticity = df_elasticity[['ranking', 'name', 'price_elasticity', 'price_mean', 'demand_mean']].sort_values(by='ranking').set_index('ranking')

st.set_page_config(layout="wide")
st.title('Price elasticity of Bestbuy laptops')

tab1, tab2= st.tabs(['Product price elasticity', 'Business Performance'])

with tab1:
    st.header('Price Elasticity')
    st.dataframe(df_elasticity, use_container_width=True)


with tab2:
    st.header('Business Performance')
    st.dataframe(df_results, use_container_width=True)