import pandas as pd
import streamlit as st
from database import *

def update_product():
    result = view_product_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "P_Name",
            "Cost_per_unit",
            "Unit",
        ],
    )
    with st.expander("Current Product Data"):
        st.dataframe(df)
    list_of_products = [i[0] for i in view_only_product_names()]
    selected_product = st.selectbox("Select Product to Edit", list_of_products)
    selected_result = get_product(selected_product)
    # st.write(selected_result)
    if selected_result:
        P_Name = selected_result[0][0]
        Cost_per_unit = selected_result[0][1]
        Unit = selected_result[0][2]
        
        
        new_P_Name = st.text_input("P_Name:", P_Name)
        new_Cost_per_unit = st.text_input("Cost per unit:", Cost_per_unit)
        new_Unit = st.text_input("Unit:", Unit)
        if st.button("Update Product"):
            edit_product_data(
                new_P_Name,
                new_Cost_per_unit,
                new_Unit,
                P_Name,
                Cost_per_unit,
                Unit,
            )
            st.success(
                "Successfully updated Product {}".format(P_Name)
            )

    result2 = view_product_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "P_Name",
            "Cost_per_unit",
            "Unit",
        ],
    )
    with st.expander("Updated Product data"):
        st.dataframe(df2)



def update_customer():
    result = view_customer_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "C_Fname", "C_Lname", "C_Email_id", "DOB", "Gender", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("Current Customer Data"):
        st.dataframe(df)
    list_of_customers = [i[0] for i in view_only_rfid()]
    selected_customer = st.selectbox("Select Customer to Edit", list_of_customers)
    selected_result = get_customer(selected_customer)
    # st.write(selected_result)
    if selected_result:
        RFID = selected_result[0][0]
        C_Fname = selected_result[0][1]
        C_Lname = selected_result[0][2]
        C_Email_id = selected_result[0][3]
        DOB = selected_result[0][4]
        Gender = selected_result[0][5]
        Street_No = selected_result[0][6]
        City = selected_result[0][7]
        PIN = selected_result[0][8]
        Admin_id = selected_result[0][9]

        # Layout of Create
        genders = ["M", "F", "Others"]
        col1, col2 = st.columns(2)
        with col1:
            new_RFID = st.text_input("RFID:", RFID)
            new_C_Fname = st.text_input("First Name:", C_Fname)
            new_C_Lname = st.text_input("Last Name:", C_Lname)
            new_C_Email_id = st.text_input("Email id:", C_Email_id)
            new_DOB = st.text_input("Date of birth:", DOB)
        with col2:
            new_Gender = st.selectbox("Gender", genders, index = genders.index(Gender))
            new_Street_No = st.text_input("Street number:", Street_No)
            new_City = st.text_input("City:", City)
            new_PIN = st.text_input("PIN:", PIN)
            new_Admin_id = st.text_input("Admin id:", Admin_id)
        if st.button("Update Customer"):
            edit_customer_data(
                new_RFID, new_C_Fname, new_C_Lname, new_C_Email_id, new_DOB, new_Gender, new_Street_No, new_City, new_PIN, new_Admin_id, 
                RFID, C_Fname, C_Lname, C_Email_id, DOB, Gender, Street_No, City, PIN, Admin_id,
            )
            st.success(
                "Successfully updated Customer {}".format(C_Fname)
            )

    result2 = view_customer_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "RFID", "C_Fname", "C_Lname", "C_Email_id", "DOB", "Gender", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("Updated Customer data"):
        st.dataframe(df2)



def update_bill():
    result = view_bill_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "Bill_id", "Total_cost", "Issued_date", "Last_valid_date", "Present_date", "Validity", "Shopkeeper_id", "RFID",
        ],
    )
    with st.expander("Current Bill Data"):
        st.dataframe(df)
    list_of_bills = [i[0] for i in view_only_bill_id()]
    selected_bill = st.selectbox("Select Bill to Edit", list_of_bills)
    selected_result = get_bill(selected_bill)
    # st.write(selected_result)
    if selected_result:
        Bill_id = selected_result[0][0]
        Total_cost = selected_result[0][1]
        Issued_date = selected_result[0][2]
        Last_valid_date = selected_result[0][3]
        Present_date = selected_result[0][4]
        Validity = selected_result[0][5]
        Shopkeeper_id = selected_result[0][6]
        RFID = selected_result[0][7]
        
        
        col1, col2 = st.columns(2)
        with col1:
            new_Bill_id= st.text_input("Bill id:", Bill_id)
            new_Total_cost = st.text_input("Total cost:", Total_cost)
            new_Issued_date = st.text_input("Issued date:", Issued_date)
            new_Last_valid_date = st.text_input("Last Valid Date:", Last_valid_date)
        with col2:
            new_Present_date = st.text_input("Present Date:", Present_date)
            new_Validity = st.text_input("Validity:", Validity)
            new_Shopkeeper_id = st.text_input("Shopkeeper id:", Shopkeeper_id)
            new_RFID = st.text_input("RFID:", RFID)
        if st.button("Update Bill"):
            edit_bill_data(
                new_Bill_id, new_Total_cost, new_Issued_date, new_Last_valid_date, new_Present_date, new_Validity, new_Shopkeeper_id, new_RFID, 
                Bill_id, Total_cost, Issued_date, Last_valid_date, Present_date, Validity, Shopkeeper_id, RFID
            )
            st.success(
                "Successfully updated Bill {}".format(Bill_id)
            )

    result2 = view_bill_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "Bill_id", "Total_cost", "Issued_date", "Last_valid_date", "Present_date", "Validity", "Shopkeeper_id", "RFID",
        ],
    )
    with st.expander("Updated Bill data"):
        st.dataframe(df2)



def update_bill_product():
    result = view_bill_product_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "Bill_id", "P_Name", "Quantity", "Total_cost_per_product",
        ],
    )
    with st.expander("Current bill product Data"):
        st.dataframe(df)
    list_of_bill_id = [i[0] for i in view_only_bill_id()]
    selected_bill_id = st.selectbox("Bill id", list_of_bill_id)
    list_of_bill_products = [i[0] for i in view_only_bill_product_names(selected_bill_id)]
    selected_bill_product = st.selectbox("Bill Product to Edit", list_of_bill_products)
    selected_result = get_bill_product(selected_bill_id, selected_bill_product)
    # st.write(selected_result)
    if selected_result:
        Bill_id= selected_result[0][0]
        P_Name = selected_result[0][1]
        Quantity = selected_result[0][2]
        Total_cost_per_product = selected_result[0][3]

        new_Bill_id= st.text_input("Bill id:", Bill_id)
        new_P_Name = st.text_input("Product Name:", P_Name)
        new_Quantity = st.text_input("Quantity:", Quantity)
        new_Total_cost_per_product = st.text_input("Total cost per product:", Total_cost_per_product)
        if st.button("Update bill product"):
            edit_bill_product_data(
                new_Bill_id, new_P_Name, new_Quantity, new_Total_cost_per_product,
                Bill_id, P_Name, Quantity, Total_cost_per_product
            )
            st.success(
                "Successfully updated bill product"
            )

    result2 = view_bill_product_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "Bill_id", "P_Name", "Quantity", "Total_cost_per_product",
        ],
    )
    with st.expander("Updated bill product data"):
        st.dataframe(df2)


def update_customer_phone():
    result = view_customer_phone_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "Phone_no",
        ],
    )
    with st.expander("Current Customer phone Data"):
        st.dataframe(df)
    list_of_rfid = [i[0] for i in view_only_rfid()]
    selected_customer_rfid = st.selectbox("Customer", list_of_rfid)
    list_of_customer_phone = [i[0] for i in view_only_customer_phone(selected_customer_rfid)]
    selected_customer_phone = st.selectbox("Customer Phone to Edit", list_of_customer_phone)
    selected_result = get_customer_phone(selected_customer_rfid, selected_customer_phone)
    # st.write(selected_result)
    if selected_result:
        RFID = selected_result[0][0]
        Phone_no = selected_result[0][1]
    
        new_RFID = st.text_input("RFID:", RFID)
        new_Phone_no = st.text_input("Phone no:", Phone_no)
        if st.button("Update Customer phone"):
            edit_customer_phone_data(
                new_RFID, new_Phone_no,
                RFID, Phone_no
            )
            st.success(
                "Successfully updated Customer phone for RFID{}".format(RFID)
            )

    result2 = view_customer_phone_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "RFID", "Phone_no",
        ],
    )
    with st.expander("Updated Customer phone data"):
        st.dataframe(df2)



def update_dependent():
    result = view_dependent_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "RFID", "D_Name", "DOB", "Gender", "Age", "Relation",
        ],
    )
    with st.expander("Current Dependent Data"):
        st.dataframe(df)
    list_of_rfid = [i[0] for i in view_only_rfid()]
    selected_rfid = st.selectbox("Customer", list_of_rfid)
    list_of_dependents = [i[0] for i in view_only_dependent(selected_rfid)]
    selected_dependent = st.selectbox("Dependent to Edit", list_of_dependents)
    selected_result = get_dependent(selected_dependent, selected_rfid)
    
    genders = ["M", "F", "Others"]
    # st.write(selected_result)
    if selected_result:
        RFID = selected_result[0][0]
        D_Name = selected_result[0][1]
        DOB = selected_result[0][2]
        Gender = selected_result[0][3]
        Age = selected_result[0][4]
        Relation = selected_result[0][5]

        new_RFID = st.text_input("RFID:", RFID)
        new_D_Name = st.text_input("Dependent Name:", D_Name)
        new_DOB = st.text_input("Date of birth:", DOB)
        new_Gender = st.selectbox("Gender", genders, index = genders.index(Gender))
        new_Age = st.text_input("Age:", Age)
        new_Relation = st.text_input("Relation:", Relation)
        if st.button("Update Dependent"):
            edit_dependent_data(
                new_RFID, new_D_Name, new_DOB, new_Gender, new_Age, new_Relation,
                RFID, D_Name, DOB, Gender, Age, Relation
            )
            st.success(
                "Successfully updated Dependent {}".format(D_Name)
            )

    result2 = view_dependent_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "RFID", "D_Name", "DOB", "Gender", "Age", "Relation",
        ],
    )
    with st.expander("Updated Dependent data"):
        st.dataframe(df2)


def update_product_customer():
    result = view_product_customer_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "P_Name",
            "RFID",
        ],
    )
    with st.expander("Current Product customer Data"):
        st.dataframe(df)
    list_of_rfid= [i[0] for i in view_only_rfid()]
    selected_product_customer_rfid = st.selectbox("Customer", list_of_rfid)
    list_of_product= [i[0] for i in view_only_customer_product_name(selected_product_customer_rfid)]
    selected_product_customer = st.selectbox("Product to Edit", list_of_product)
    selected_result = get_product_customer(selected_product_customer, selected_product_customer_rfid)
    # st.write(selected_result)
    if selected_result:
        RFID = selected_result[0][1]
        P_Name = selected_result[0][0]
        
        
        new_RFID= st.text_input("RFID:", RFID)
        new_P_Name = st.text_input("P_Name:", P_Name)
        if st.button("Update Product customer"):
            edit_product_customer_data(
                new_P_Name, new_RFID, 
                P_Name, RFID
            )
            st.success(
                "Successfully updated Product customer {}".format(P_Name)
            )

    result2 = view_product_customer_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "P_Name",
            "RFID",
        ],
    )
    with st.expander("Updated Product customer data"):
        st.dataframe(df2)



def update_shopkeeper():
    result = view_shopkeeper_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "S_Fname", "S_Lname", "Store_name", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("Current Shopkeeper Data"):
        st.dataframe(df)
    list_of_shopkeepers = [i[0] for i in view_only_shopkeeper_id()]
    selected_shopkeeper = st.selectbox("Select Shopkeeper to Edit", list_of_shopkeepers)
    selected_result = get_shopkeeper(selected_shopkeeper)
    # st.write(selected_result)
    if selected_result:
        Shopkeeper_id = selected_result[0][0]
        S_Fname = selected_result[0][1]
        S_Lname = selected_result[0][2]
        Store_name = selected_result[0][3]
        Street_No = selected_result[0][4]
        City = selected_result[0][5]
        PIN = selected_result[0][6]
        Admin_id = selected_result[0][7]

        # Layout of Create
        genders = ["Male", "Female", "Others"]
        col1, col2 = st.columns(2)
        with col1:
            new_Shopkeeper_id = st.text_input("Shopkeeper id:", Shopkeeper_id)
            new_S_Fname = st.text_input("First Name:", S_Fname)
            new_S_Lname = st.text_input("Last Name:", S_Lname)
            new_Store_name = st.text_input("Store Name:", Store_name)
        with col2:
            new_Street_No = st.text_input("Street number:", Street_No)
            new_City = st.text_input("City:", City)
            new_PIN = st.text_input("PIN:", PIN)
            new_Admin_id = st.text_input("Admin id:", Admin_id)
        if st.button("Update Shopkeeper"):
            edit_shopkeeper_data(
                new_Shopkeeper_id, new_S_Fname, new_S_Lname, new_Store_name, new_Street_No, new_City, new_PIN, new_Admin_id,
                Shopkeeper_id, S_Fname, S_Lname, Store_name, Street_No, City, PIN, Admin_id
            )
            st.success(
                "Successfully updated Shopkeeper {}".format(S_Fname)
            )

    result2 = view_shopkeeper_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "Shopkeeper_id", "S_Fname", "S_Lname", "Store_name", "Street_No", "City", "PIN", "Admin_id",
        ],
    )
    with st.expander("Updated Shopkeeper data"):
        st.dataframe(df2)



def update_shopkeeper_product():
    result = view_shopkeeper_product_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "P_Name", "Initial_Quantity", "Present_Quantity",
        ],
    )
    with st.expander("Current Shopkeeper product Data"):
        st.dataframe(df)
    list_of_shopkeeper = [i[0] for i in view_only_shopkeeper_id()]
    selected_shopkeeper = st.selectbox("Shopkeeper", list_of_shopkeeper)
    list_of_shopkeeper_products = [i[0] for i in view_shopkeeper_product_name(selected_shopkeeper)]
    selected_shopkeeper_product = st.selectbox("Shopkeeper product to Edit", list_of_shopkeeper_products)
    selected_result = get_shopkeeper_product(selected_shopkeeper, selected_shopkeeper_product)
    # st.write(selected_result)
    if selected_result:
        Shopkeeper_id = selected_result[0][0]
        P_Name = selected_result[0][1]
        Initial_Quantity = selected_result[0][2]
        Present_Quantity = selected_result[0][3]
        
        new_Shopkeeper_id = st.text_input("Shopkeeper id:", Shopkeeper_id)
        new_P_Name = st.text_input("P_Name:", P_Name)
        new_Initial_Quantity = st.text_input("Quantity:", Initial_Quantity)
        new_Present_Quantity = st.text_input("Quantity:", Present_Quantity)
        if st.button("Update Shopkeeper product"):
            edit_shopkeeper_product_data(
                new_Shopkeeper_id, new_P_Name, new_Initial_Quantity, new_Present_Quantity,
                Shopkeeper_id, P_Name, Initial_Quantity, Present_Quantity
            )
            st.success(
                "Successfully updated Shopkeeper product for shopkeeper_id{}".format(Shopkeeper_id)
            )

    result2 = view_shopkeeper_product_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "Shopkeeper_id", "P_Name","Initial_Quantity", "Present_Quantity",
        ],
    )
    with st.expander("Updated Shopkeeper product data"):
        st.dataframe(df2)



def update_shopkeeper_phone():
    result = view_shopkeeper_phone_data()
    # st.write(result)
    df = pd.DataFrame(
        result,
        columns=[
            "Shopkeeper_id", "Phone_no",
        ],
    )
    with st.expander("Current Shopkeeper phone Data"):
        st.dataframe(df)
    list_of_shopkeeper = [i[0] for i in view_only_shopkeeper_id()]
    selected_shopkeeper = st.selectbox("Shopkeeper", list_of_shopkeeper)
    list_of_shopkeeper_phones = [i[0] for i in view_only_shopkeeper_phone(selected_shopkeeper)]
    selected_shopkeeper_phone = st.selectbox("Shopkeeper phone toEdit", list_of_shopkeeper_phones)
    selected_result = get_shopkeeper_phone(selected_shopkeeper, selected_shopkeeper_phone)
    # st.write(selected_result)
    if selected_result:
        Shopkeeper_id = selected_result[0][0]
        Phone_no = selected_result[0][1]
    
        new_Shopkeeper_id = st.text_input("Shopkeeper id:", Shopkeeper_id)
        new_Phone_no = st.text_input("Phone no:", Phone_no)
        if st.button("Update Shopkeeper phone"):
            edit_shopkeeper_phone_data(
                new_Shopkeeper_id, new_Phone_no,
                Shopkeeper_id, Phone_no
            )
            st.success(
                "Successfully updated Shopkeeper phone for shopkeeper id {}".format(Shopkeeper_id)
            )

    result2 = view_shopkeeper_phone_data()
    df2 = pd.DataFrame(
        result2,
        columns=[
            "Shopkeeper_id", "Phone_no",
        ],
    )
    with st.expander("Updated Shopkeeper phone data"):
        st.dataframe(df2)


