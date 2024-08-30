import pandas as pd
import streamlit as st
from database import *

def read_admin():
    result = view_admin_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Admin_id", "A_Fname", "A_Lname", "A_Email_id", "DOB", "Age","Street_No", "PIN",
        ],
    )
    with st.expander("View all Admins"):
        st.dataframe(df)
    

def read_admin_phone():
    result = view_admin_phone_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Admin_id", "Phone_no",
        ],
    )
    with st.expander("View all Phone nos"):
        st.dataframe(df)
    
def read_bill():
    result = view_bill_data()
    df = pd.DataFrame(
        result,
        columns=[
           "Bill_id", "Total_cost", "Issued_date", "Last_valid_date", "Present_date", "Validity", "Shopkeeper_id", "RFID",
        ],
    )
    with st.expander("View all Bills"):
        st.dataframe(df)
    

def read_bill_product():
    result = view_bill_product_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Bill_id", "P_Name", "Quantity", "Total_cost_per_product",
        ],
    )
    with st.expander("View all"):
        st.dataframe(df)
    
def read_customer():
    result = view_customer_data()
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "FName", "LName", "Email_id", "DOB", "Gender", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("View all Customers"):
        st.dataframe(df)
    

def read_customer_phone():
    result = view_customer_phone_data()
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "Phone_no",
        ],
    )
    with st.expander("View all Phone nos"):
        st.dataframe(df)
    
def read_dependent():
    result = view_dependent_data()
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "D_Name", "DOB", "Gender", "Age", "Relation",
        ],
    )
    with st.expander("View all dependent"):
        st.dataframe(df)
    

def read_product():
    result = view_product_data()
    df = pd.DataFrame(
        result,
        columns=[
            "P_Name",
            "Cost_per_unit",
            "Unit",
        ],
    )
    with st.expander("View all Products"):
        st.dataframe(df)
    
def read_product_customer():
    result = view_product_customer_data()
    df = pd.DataFrame(
        result,
        columns=[
            "P_Name",
            "RFID",
        ],
    )
    with st.expander("View all"):
        st.dataframe(df)
    

def read_shopkeeper():
    result = view_shopkeeper_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "S_Fname", "S_Lname", "Store_name", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("View all Shopkeeper"):
        st.dataframe(df)
    
def read_shopkeeper_product():
    result = view_shopkeeper_product_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "P_Name", "Initial_Quantity", "Present_Quantity",
        ],
    )
    with st.expander("View all"):
        st.dataframe(df)

def read_shopkeeper_phone():
    result = view_shopkeeper_phone_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "Phone_no",
        ],
    )
    with st.expander("View all Phone nos"):
        st.dataframe(df)
