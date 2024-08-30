import streamlit as st
from database import *



def create_admin():
    col1, col2 = st.columns(2)
    with col1:
        Admin_id = st.text_input("Admin id:")
        A_Fname = st.text_input("First Name:")
        A_Lname = st.text_input("Last Name:")
        A_Email_id = st.text_input("Email id:")
    with col2:
        DOB = st.text_input("Date of birth:")
        Age = st.text_input("Age")
        Street_No = st.text_input("Street number:")
        PIN = st.text_input("PIN:")
    if st.button("Add Admin"):
        add_data_admin(Admin_id, A_Fname, A_Lname, A_Email_id, DOB, Age, Street_No, PIN)
        st.success("Successfully added Admin: {}".format(A_Fname))

def create_admin_phone():
    Admin_id = st.text_input("Admin id:")
    Phone_no = st.text_input("Phone no:")
    if st.button("Add Admin Phone No"):
        add_data_admin_phone(Admin_id, Phone_no)
        st.success("Successfully added Admin Phone for admin id: {}".format(Admin_id))

def create_bill():
    col1, col2 = st.columns(2)
    with col1:
        Bill_id= st.text_input("Bill id:")
        Total_cost = st.text_input("Total cost:")
        Issued_date = st.text_input("Issued date:")
        Last_valid_date = st.text_input("Last Valid Date:")
    with col2:
        Present_date = st.text_input("Present Date:")
        Validity = st.text_input("Validity:")
        Shopkeeper_id = st.text_input("Shopkeeper id:")
        RFID = st.text_input("RFID:")
    if st.button("Add Bill"):
        add_data_bill(Bill_id, Total_cost, Issued_date, Last_valid_date, Present_date, Validity, Shopkeeper_id, RFID)
        st.success("Successfully added Bill: {}".format(Bill_id))

def create_bill_product():
    Bill_id= st.text_input("Bill id:")
    P_Name = st.text_input("Product Name:")
    Quantity = st.text_input("Quantity:")
    Total_cost_per_product = st.text_input("Total cost per product:")
    if st.button("Add Bill Product"):
        add_data_bill_product(Bill_id, P_Name, Quantity, Total_cost_per_product)
        st.success("Successfully added")

def create_customer():
    col1, col2 = st.columns(2)
    with col1:
        RFID = st.text_input("RFID:")
        C_Fname = st.text_input("First Name:")
        C_Lname = st.text_input("Last Name:")
        C_Email_id = st.text_input("Email id:")
        DOB = st.text_input("Date of birth:")
    with col2:
        Gender = st.selectbox("Gender", ["M", "F", "Others"])
        Street_No = st.text_input("Street number:")
        City = st.text_input("City:")
        PIN = st.text_input("PIN:")
        Admin_id = st.text_input("Admin id:")
    if st.button("Add Customer"):
        add_data_customer(RFID, C_Fname, C_Lname, C_Email_id, DOB, Gender, Street_No, City, PIN, Admin_id)
        st.success("Successfully added Customer: {}".format(C_Fname))

def create_customer_phone():
    RFID = st.text_input("RFID:")
    Phone_no = st.text_input("Phone no:")
    if st.button("Add Customer Phone No"):
        add_data_customer_phone(RFID, Phone_no)
        st.success("Successfully added Customer Phone for customer id: {}".format(RFID))

def create_dependent():
    RFID = st.text_input("RFID:")
    D_Name = st.text_input("Dependent Name:")
    DOB = st.text_input("Date of birth:")
    Gender = st.selectbox("Gender", ["M", "F", "Others"])
    Age = st.text_input("Age:")
    Relation = st.text_input("Relation:")
    if st.button("Add Dependent"):
        add_data_dependent(RFID, D_Name, DOB, Gender, Age, Relation)
        st.success("Successfully added Dependent: {}".format(D_Name))

def create_product():
    P_Name = st.text_input("Product Name:")
    Cost_per_unit = st.text_input("Cost per unit:")
    Unit = st.text_input("Unit:")
    if st.button("Add Product"):
        add_data_product(P_Name, Cost_per_unit, Unit)
        st.success("Successfully added Product: {}".format(P_Name))

def create_product_customer():
    P_Name = st.text_input("Product Name:")
    RFID = st.text_input("RFID:")
    if st.button("Add Product Customer"):
        add_data_product_customer(P_Name, RFID)
        st.success("Successfully added")


def create_shopkeeper():
    col1, col2 = st.columns(2)
    with col1:
        Shopkeeper_id = st.text_input("Shopkeeper id:")
        S_Fname = st.text_input("First Name:")
        S_Lname = st.text_input("Last Name:")
        Store_name = st.text_input("Store Name:")
    with col2:
        Street_No = st.text_input("Street number:")
        City = st.text_input("City:")
        PIN = st.text_input("PIN:")
        Admin_id = st.text_input("Admin id:")
    if st.button("Add Shopkeeper"):
        add_data_shopkeeper(Shopkeeper_id, S_Fname, S_Lname, Store_name, Street_No, City, PIN, Admin_id)
        st.success("Successfully added Shopkeeper: {}".format(S_Fname))

def create_shopkeeper_phone():
    Shopkeeper_id = st.text_input("Shopkeeper id:")
    Phone_no = st.text_input("Phone no:")
    if st.button("Add Shopkeeper Phone No"):
        add_data_shopkeeper_phone(Shopkeeper_id, Phone_no)
        st.success("Successfully added Shopkeeper Phone for Shopkeeper id: {}".format(Shopkeeper_id))

def create_shopkeeper_product():
    Shopkeeper_id = st.text_input("Shopkeeper id:")
    P_Name = st.text_input("Product Name:")
    Initial_Quantity = st.text_input("Initial Quantity:")
    Present_Quantity = st.text_input("Present Quantity:")
    if st.button("Add Shopkeeper Product No"):
        add_data_shopkeeper_product(Shopkeeper_id, P_Name, Initial_Quantity, Present_Quantity)
        st.success("Successfully added")
