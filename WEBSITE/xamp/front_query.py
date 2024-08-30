import streamlit as st
import pandas as pd
from database import queryy


def front_query():
        col1, col2 = st.columns(2)
        l=[]
        with col1:
            c1 = st.text_input("Column 1:")
            c2 = st.text_input("Column 2:")
            c3 =  st.text_input("Column 3:")
            c4 =  st.text_input("Column 4:")

        with col2:
            c5 = st.text_input("Column 5:")
            c6 = st.text_input("Column 6:")
            c7 = st.text_input("Column 7:")
            c8 = st.text_input("Column 8:")
        Query = st.text_input("Query:")

        if c1!='':
            l.append(c1)
        if c2!='':
            l.append(c2)
        if c3!='':
            l.append(c3)
        if c4!='':
            l.append(c4)
        if c5!='':
            l.append(c5)
        if c6!='':
            l.append(c6)
        if c7!='':
            l.append(c7)
        if c8!='':
            l.append(c8)

        if st.button('Execute'):
            df = pd.DataFrame(queryy(Query), columns=l)
            st.dataframe(df)