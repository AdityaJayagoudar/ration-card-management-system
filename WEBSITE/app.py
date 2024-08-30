import pickle 
from pathlib import Path
import streamlit_authenticator as stauth

import streamlit as st
import mysql.connector

from create import *
from delete import *
from read import *
from update import *
from front_query import *
from sell_product import *

mydb = mysql.connector.connect(host="localhost", user="root", password="")
c = mydb.cursor()

c.execute("CREATE DATABASE IF NOT EXISTS ration_card_system;")


names = ["ADMIN", "ADMIN", "ADMIN", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER", "SHOPKEEPER"]
usernames = ["ADM_001", "ADM_002", "ADM_003", "SHK_001", "SHK_002", "SHK_003", "SHK_004", "SHK_005", "SHK_006"]

file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "sales_dashboard", "1234", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status == False :
        st.error("Username/password is incorrect")

if authentication_status == None :
        st.warning("Please enter your username and password")

if authentication_status :
    st.title("Ration Card System")
    def main():
            
        
        authenticator.logout("Logout", "sidebar")
        if name == "ADMIN" :
            Tables_admin = ["Customer", "Customer Phone", "Dependents", "Product", "Shopkeeper", "Shopkeeper Phone","Shopkeeper Product", "Sale", "Query"]
            choice = st.sidebar.selectbox("Tables", Tables_admin)
                
            if choice == "Customer":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected2 = st.sidebar.selectbox("Operations", Operations)
                    
                    if selected2 == "Add":
                        st.subheader("Enter Customer Details:")
                        create_customer()

                    elif selected2 == "View":
                        st.subheader("View all Customer")
                        read_customer()

                    elif selected2 == "Edit":
                        st.subheader("Update Customer details:")
                        update_customer()

                    elif selected2 == "Remove":
                        st.subheader("Delete Customer details:")
                        delete_customer()

            elif choice == "Customer Phone":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected2 = st.sidebar.selectbox("Operations", Operations)
                    
                    if selected2 == "Add":
                        st.subheader("Enter Customer Details:")
                        create_customer_phone()

                    elif selected2 == "View":
                        st.subheader("View all Customer")
                        read_customer_phone()

                    elif selected2 == "Edit":
                        st.subheader("Update Customer details:")
                        update_customer_phone()

                    elif selected2 == "Remove":
                        st.subheader("Delete Customer details:")
                        delete_customer_phone()

            elif choice == "Dependents":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected1 = st.sidebar.selectbox("Operations", Operations)

                    if selected1 == "Add":
                        st.subheader("View all Product")
                        create_dependent()
                
                    elif selected1 == "View":
                        st.subheader("View all Product")
                        read_dependent()

                    elif selected1 == "Edit":
                        st.subheader("Update Product details:")
                        update_dependent()
                
                    elif selected1 == "Remove":
                        st.subheader("Delete Product details:")
                        delete_dependent()
            
            elif choice == "Product":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected1 = st.sidebar.selectbox("Operations", Operations)

                    if selected1 == "Add":
                        st.subheader("View all Product")
                        create_product()
                
                    elif selected1 == "View":
                        st.subheader("View all Product")
                        read_product()

                    elif selected1 == "Edit":
                        st.subheader("Update Product details:")
                        update_product()
                
                    elif selected1 == "Remove":
                        st.subheader("Delete Product details:")
                        delete_product()
                
            elif choice == "Shopkeeper":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected2 = st.sidebar.selectbox("Operations", Operations)
                    
                    if selected2 == "Add":
                        st.subheader("Enter Customer Details:")
                        create_shopkeeper()

                    elif selected2 == "View":
                        st.subheader("View all Customer")
                        read_shopkeeper()

                    elif selected2 == "Edit":
                        st.subheader("Update Customer details:")
                        update_shopkeeper()

                    elif selected2 == "Remove":
                        st.subheader("Delete Customer details:")
                        delete_shopkeeper()

            elif choice == "Shopkeeper Phone":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected2 = st.sidebar.selectbox("Operations", Operations)
                    
                    if selected2 == "Add":
                        st.subheader("Enter Customer Details:")
                        create_shopkeeper_phone()

                    elif selected2 == "View":
                        st.subheader("View all Customer")
                        read_shopkeeper_phone()

                    elif selected2 == "Edit":
                        st.subheader("Update Customer details:")
                        update_shopkeeper_phone()

                    elif selected2 == "Remove":
                        st.subheader("Delete Customer details:")
                        delete_shopkeeper_phone()

            elif choice == "Shopkeeper Product":
                Operations =["Add", "View", "Remove"]
                selected2 = st.sidebar.selectbox("Operations", Operations)
                    
                if selected2 == "Add":
                    st.subheader("Enter Customer Details:")
                    create_shopkeeper_product()

                elif selected2 == "View":
                    st.subheader("View all Customer")
                    read_shopkeeper_product()

                elif selected2 == "Remove":
                    st.subheader("Delete Customer details:")
                    delete_shopkeeper_product()
            
            elif choice == "Sale":
                st.subheader("Enter dates to get sales between them")
                sales_between_dates()

            elif choice=='Query':
                st.subheader("Enter output Columns")
                front_query()
                
        elif name == "SHOPKEEPER":
            Tables_shopkeeper = ["Bill", "Bill Product", "Product Customer", "Shopkeeper Product", "Sell", "Sale", "Query"]
            choice = st.sidebar.selectbox("Tables", Tables_shopkeeper)
            if choice == "Bill":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected1 = st.sidebar.selectbox("Operations", Operations)

                    if selected1 == "Add":
                        st.subheader("View all Product")
                        create_bill()
                
                    elif selected1 == "View":
                        st.subheader("View all Product")
                        read_bill()

                    elif selected1 == "Edit":
                        st.subheader("Update Product details:")
                        update_bill()
                
                    elif selected1 == "Remove":
                        st.subheader("Delete Product details:")
                        delete_bill()

            elif choice == "Bill Product":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected1 = st.sidebar.selectbox("Operations", Operations)

                    if selected1 == "Add":
                        st.subheader("View all Product")
                        create_bill_product()
                
                    elif selected1 == "View":
                        st.subheader("View all Product")
                        read_bill_product()

                    elif selected1 == "Edit":
                        st.subheader("Update Product details:")
                        update_bill_product()
                
                    elif selected1 == "Remove":
                        st.subheader("Delete Product details:")
                        delete_bill_product()

            
            elif choice == "Product Customer":
                    Operations =["Add", "View", "Edit", "Remove"]
                    selected1 = st.sidebar.selectbox("Operations", Operations)

                    if selected1 == "Add":
                        st.subheader("View all Product")
                        create_product_customer()
                
                    elif selected1 == "View":
                        st.subheader("View all Product")
                        read_product_customer()

                    elif selected1 == "Edit":
                        st.subheader("Update Product details:")
                        update_product_customer()
                
                    elif selected1 == "Remove":
                        st.subheader("Delete Product details:")
                        delete_product_customer()

            
            
            elif choice == "Shopkeeper Product":
                    Operations =["View"]
                    selected2 = st.sidebar.selectbox("Operations", Operations)

                    if selected2 == "View":
                        st.subheader("View all Customer")
                        read_shopkeeper_product()
            
            elif choice == "Sale":
                st.subheader("Enter dates to get sales between them")
                sales_between_dates()
                
            elif choice=='Sell':
                sell_product()

            elif choice=='Query':
                st.subheader("Enter output Columns")
                front_query()
                    
        else:
             st.subheader("About tasks")


    if __name__ == "__main__":
        main()
