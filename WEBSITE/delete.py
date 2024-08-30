import pandas as pd
import streamlit as st
from database import *

def delete_product():
    result = view_product_data()
    df = pd.DataFrame(
        result,
        columns=[
            "P_Name",
            "Cost_per_unit",
            "Unit",
        ],
    )
    with st.expander("Current product data"):
        st.dataframe(df)

    list_of_products = [i[0] for i in view_only_product_names()]
    selected_product = st.selectbox("Product to Delete", list_of_products)
    if(selected_product):
        st.warning("Do you want to delete product {}? This action cannot be reversed!".format(selected_product))
    if st.button("DELETE PRODUCT"):
        delete_data_product(selected_product)
        st.success("Product {} has been deleted successfully, see Updated data below.".format(selected_product))
    new_result = view_product_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "P_Name",
            "Cost_per_unit",
            "Unit",
        ],
    )
    with st.expander("Updated product data"):
        st.dataframe(df2)



def delete_customer():
    result = view_customer_data()
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "FName", "LName", "Email_id", "DOB", "Gender", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("Current customer data"):
        st.dataframe(df)

    list_of_customers = [i[0] for i in view_only_rfid()]
    selected_customer = st.selectbox("Customer to Delete", list_of_customers)
    if(selected_customer):
        st.warning("Do you want to delete customer {}? This action cannot be reversed!".format(selected_customer))
    if st.button("DELETE CUSTOMER"):
        delete_data_customer(selected_customer)
        st.success("Customer {} has been deleted successfully, see Updated data below.".format(selected_customer))
    new_result = view_customer_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "RFID", "FName", "LName", "Email_id", "DOB", "Gender", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("Updated customer data"):
        st.dataframe(df2)


def delete_bill():
    result = view_bill_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Bill_id", "Total_cost", "Issued_date", "Last_valid_date", "Present_date", "Validity", "Shopkeeper_id", "RFID",
        ],
    )
    with st.expander("Current bill data"):
        st.dataframe(df)

    list_of_bills = [i[0] for i in view_only_bill_id()]
    selected_bill = st.selectbox("Bill to Delete", list_of_bills)
    if(selected_bill):
        st.warning("Do you want to delete bill {}? This action cannot be reversed!".format(selected_bill))
    if st.button("DELETE BILL"):
        delete_data_bill(selected_bill)
        st.success("Bill {} has been deleted successfully, see Updated data below.".format(selected_bill))
    new_result = view_bill_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "Bill_id", "Total_cost", "Issued_date", "Last_valid_date", "Present_date", "Validity", "Shopkeeper_id", "RFID",
        ],
    )
    with st.expander("Updated bill data"):
        st.dataframe(df2)


def delete_bill_product():
    result = view_bill_product_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Bill_id", "P_Name", "Quantity", "Total_cost_per_product",
        ],
    )
    with st.expander("Current bill product data"):
        st.dataframe(df)

    list_of_bill_id = [i[0] for i in view_only_bill_id()]
    selected_bill_id = st.selectbox("Bill id", list_of_bill_id)
    list_of_bill_products = [i[0] for i in view_only_bill_product_names(selected_bill_id)]
    selected_bill_product = st.selectbox("Bill Product to Delete", list_of_bill_products)
    if(selected_bill_product):
        st.warning("Do you want to delete bill product {}? This action cannot be reversed!".format(selected_bill_product))
    if st.button("DELETE BILL PRODUCT"):
        delete_data_bill_product(selected_bill_id, selected_bill_product)
        st.success("Bill Product {} has been deleted successfully, see Updated data below.".format(selected_bill_product))
    new_result = view_bill_product_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "Bill_id", "P_Name", "Quantity", "Total_cost_per_product",
        ],
    )
    with st.expander("Updated bill product data"):
        st.dataframe(df2)

def delete_customer_phone():
    result = view_customer_phone_data()
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "Phone_no",
        ],
    )
    with st.expander("Current Customer phone data"):
        st.dataframe(df)

    list_of_rfid = [i[0] for i in view_only_rfid()]
    selected_customer_rfid = st.selectbox("Customer", list_of_rfid)
    list_of_customer_phone = [i[0] for i in view_only_customer_phone(selected_customer_rfid)]
    selected_customer_phone = st.selectbox("Customer Phone to delete", list_of_customer_phone)
    if(selected_customer_phone):
        st.warning("Do you want to delete customer phone {}? This action cannot be reversed!".format(selected_customer_phone))
    if st.button("DELETE CUSTOMER PHONE NO"):
        delete_data_customer_phone(selected_customer_rfid, selected_customer_phone)
        st.success("Customer phone {} has been deleted successfully, see Updated data below.".format(selected_customer_phone))
    new_result = view_customer_phone_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "RFID", "Phone_no",
        ],
    )
    with st.expander("Updated Customer phone data"):
        st.dataframe(df2)




def delete_dependent():
    result = view_dependent_data()
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "D_Name", "DOB", "Gender", "Age", "Relation",
        ],
    )
    with st.expander("Current dependent data"):
        st.dataframe(df)

    list_of_rfid = [i[0] for i in view_only_rfid()]
    selected_rfid = st.selectbox("Customer", list_of_rfid)
    list_of_dependents = [i[0] for i in view_only_dependent(selected_rfid)]
    selected_dependent = st.selectbox("Dependent to Delete", list_of_dependents)
    if(selected_dependent):
        st.warning("Do you want to delete dependent {}? This action cannot be reversed!".format(selected_dependent))
    if st.button("DELETE DEPENDENT"):
        delete_data_dependent(selected_dependent, selected_rfid)
        st.success("dependent {} has been deleted successfully, see Updated data below.".format(selected_dependent))
    new_result = view_dependent_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "RFID", "D_Name", "DOB", "Gender", "Age", "Relation",
        ],
    )
    with st.expander("Updated dependent data"):
        st.dataframe(df2)


def delete_product_customer():
    result = view_product_customer_data()
    df = pd.DataFrame(
        result,
        columns=[
            "P_Name",
            "RFID",
        ],
    )
    with st.expander("Current product customer data"):
        st.dataframe(df)

    list_of_rfid= [i[0] for i in view_only_rfid()]
    selected_product_customer_rfid = st.selectbox("Customer", list_of_rfid)
    list_of_product= [i[0] for i in view_only_customer_product_name(selected_product_customer_rfid)]
    selected_product_customer = st.selectbox("Product to Delete", list_of_product)
    if(selected_product_customer):
        st.warning("Do you want to delete product customer {}? This action cannot be reversed!".format(selected_product_customer))
    if st.button("DELETE PRODUCT CUSTOMER"):
        delete_data_product_customer(selected_product_customer, selected_product_customer_rfid)
        st.success("Product Customer {} has been deleted successfully, see Updated data below.".format(selected_product_customer))
    new_result = view_product_customer_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "P_Name",
            "RFID",
        ],
    )
    with st.expander("Updated product customer data"):
        st.dataframe(df2)



def delete_shopkeeper():
    result = view_shopkeeper_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "S_Fname", "S_Lname", "Store_name", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("Current shopkeeper data"):
        st.dataframe(df)

    list_of_shopkeepers = [i[0] for i in view_only_shopkeeper_id()]
    selected_shopkeeper = st.selectbox("Shopkeeper to Delete", list_of_shopkeepers)
    if(selected_shopkeeper):
        st.warning("Do you want to delete shopkeeper {}? This action cannot be reversed!".format(selected_shopkeeper))
    if st.button("DELETE SHOPKEEPER"):
        delete_data_shopkeeper(selected_shopkeeper)
        st.success("Shopkeeper {} has been deleted successfully, see Updated data below.".format(selected_shopkeeper))
    new_result = view_shopkeeper_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "Shopkeeper_id", "S_Fname", "S_Lname", "Store_name", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("Updated shopkeeper data"):
        st.dataframe(df2)

def delete_shopkeeper_product():
    result = view_shopkeeper_product_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "P_Name","Initial_Quantity", "Present_Quantity",
        ],
    )
    with st.expander("Current shopkeeper product data"):
        st.dataframe(df)

    list_of_shopkeeper = [i[0] for i in view_only_shopkeeper_id()]
    selected_shopkeeper = st.selectbox("Shopkeeper", list_of_shopkeeper)
    list_of_shopkeeper_products = [i[0] for i in view_shopkeeper_product_name(selected_shopkeeper)]
    selected_shopkeeper_product = st.selectbox("Shopkeeper product to Delete", list_of_shopkeeper_products)
    if(selected_shopkeeper_product):
        st.warning("Do you want to delete shopkeeper product {}? This action cannot be reversed!".format(selected_shopkeeper_product))
    if st.button("DELETE SHOPKEEPER PRODUCT"):
        delete_data_shopkeeper_product(selected_shopkeeper, selected_shopkeeper_product)
        st.success("Shopkeeper product {} has been deleted successfully, see Updated data below.".format(selected_shopkeeper_product))
    new_result = view_shopkeeper_product_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
            "Shopkeeper_id", "P_Name","Initial_Quantity", "Present_Quantity",
        ],
    )
    with st.expander("Updated shopkeeper product data"):
        st.dataframe(df2)



def delete_shopkeeper_phone():
    result = view_shopkeeper_phone_data()
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "Phone_no",
        ],
    )
    with st.expander("Current shopkeeper phone data"):
        st.dataframe(df)

    list_of_shopkeeper = [i[0] for i in view_only_shopkeeper_id()]
    selected_shopkeeper = st.selectbox("Shopkeeper", list_of_shopkeeper)
    list_of_shopkeeper_phones = [i[0] for i in view_only_shopkeeper_phone(selected_shopkeeper)]
    selected_shopkeeper_phone = st.selectbox("Shopkeeper phone to Delete", list_of_shopkeeper_phones)
    if(selected_shopkeeper_phone):
        st.warning("Do you want to delete shopkeeper phone {}? This action cannot be reversed!".format(selected_shopkeeper_phone))
    if st.button("DELETE SHOPKEEPER PHONE"):
        delete_data_shopkeeper_phone(selected_shopkeeper, selected_shopkeeper_phone)
        st.success("Shopkeeper phone {} has been deleted successfully, see Updated data below.".format(selected_shopkeeper_phone))
    new_result = view_shopkeeper_phone_data()
    df2 = pd.DataFrame(
        new_result,
        columns=[
           "Shopkeeper_id", "Phone_no",
        ],
    )
    with st.expander("Updated shopkeeper phone data"):
        st.dataframe(df2)
