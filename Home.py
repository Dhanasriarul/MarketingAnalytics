import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
from numerize.numerize import numerize
#from query import *
from query import view_all_data  

st.set_page_config(page_title="Dashboard",page_icon="🌎",layout="wide")
st.subheader("🕬 Marketing Analytics")
st.markdown("##")



result=view_all_data()
columns = ['Id', 'Name', 'Location', 'Product', 'interaction_score']
df = pd.DataFrame(result, columns=columns)

#df = pd.DataFrame(result, columns=["id", "Name", "Location", "Product", "interaction_score"])
st.dataframe(df)
