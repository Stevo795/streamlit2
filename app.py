import streamlit as st
import numpy as np
import pandas as pd
import time

st.title('APP Tittle')
st.write('###header')

dat = pd.read_csv("admin_data.csv")
dat1 = dat.loc[0:5, :]

st.write(dat1)

if st.checkbox('Show dataframe'):
    st.line_chart(dat1)

option = st.sidebar.selectbox(
    'Which number do you like best?',
     dat1['SOP'])

left_column, right_column = st.beta_columns(2)
pressed = left_column.button('Press me?')
if pressed:
    right_column.write("Woohoo!")

expander = st.beta_expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'