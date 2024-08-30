import mysql.connector
import streamlit as st
import pandas as pd
import plotly.express as px

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="ration_card_system"
)
c = mydb.cursor()


def add_data_admin(Admin_id, A_Fname, A_Lname, A_Email_id, DOB, Age, Street_No, PIN):
    c.execute(
        "INSERT INTO ADMIN(Admin_id, A_Fname, A_Lname, A_Email_id, DOB, Age, Street_No, PIN) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (Admin_id, A_Fname, A_Lname, A_Email_id, DOB, Age, Street_No, PIN),
    )
    mydb.commit()

def add_data_admin_phone(Admin_id, Phone_no):
    c.execute(
        "INSERT INTO ADMIN_PHONE(Admin_id, Phone_no) VALUES (%s,%s)",
        (Admin_id, Phone_no),
    )
    mydb.commit()

def add_data_bill(Bill_id, Total_cost, Issued_date, Last_valid_date, Present_date, Validity, Shopkeeper_id, RFID):
    c.execute(
        "INSERT INTO BILL(Bill_id, Total_cost, Issued_date, Last_valid_date, Present_date, Validity, Shopkeeper_id, RFID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (Bill_id, Total_cost, Issued_date, Last_valid_date, Present_date, Validity, Shopkeeper_id, RFID),
    )
    mydb.commit()

def add_data_bill_product(Bill_id, P_Name, Quantity, Total_cost_per_product):
    c.execute(
        "INSERT INTO BILL_PRODUCT(Bill_id, P_Name, Quantity, Total_cost_per_product) VALUES (%s,%s,%s,%s)",
        (Bill_id, P_Name, Quantity, Total_cost_per_product),
    )
    mydb.commit()

def add_data_customer(RFID, C_Fname, C_Lname, C_Email_id, DOB, Gender, Street_No, City, PIN, Admin_id):
    c.execute(
        "INSERT INTO CUSTOMER(RFID, C_Fname, C_Lname, C_Email_id, DOB, Gender, Street_No, City, PIN, Admin_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (RFID, C_Fname, C_Lname, C_Email_id, DOB, Gender, Street_No, City, PIN, Admin_id),
    )
    mydb.commit()

def add_data_customer_phone(RFID, Phone_no):
    c.execute(
        "INSERT INTO CUSTOMER_PHONE(RFID, Phone_no) VALUES (%s,%s)",
        (RFID, Phone_no),
    )
    mydb.commit()

def add_data_dependent(RFID, D_Name, DOB, Gender, Age, Relation):
    c.execute(
        "INSERT INTO DEPENDENT(RFID, D_Name, DOB, Gender, Age, Relation) VALUES (%s,%s,%s,%s,%s,%s)",
        (RFID, D_Name, DOB, Gender, Age, Relation),
    )
    mydb.commit()

def add_data_product(P_Name, Cost_per_unit, Unit):
    c.execute(
        "INSERT INTO PRODUCT(P_Name, Cost_per_unit, Unit) VALUES (%s,%s,%s)",
        (P_Name, Cost_per_unit, Unit),
    )
    mydb.commit()

def add_data_product_customer(P_Name, RFID):
    c.execute(
        "INSERT INTO PRODUCT_CUSTOMER(P_Name, RFID) VALUES (%s,%s)",
        (P_Name, RFID),
    )
    mydb.commit()

def add_data_shopkeeper(Shopkeeper_id, S_Fname, S_Lname, Store_name, Street_No, City, PIN, Admin_id):
    c.execute(
        "INSERT INTO SHOPKEEPER(Shopkeeper_id, S_Fname, S_Lname, Store_name, Street_No, City, PIN, Admin_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
        (Shopkeeper_id, S_Fname, S_Lname, Store_name, Street_No, City, PIN, Admin_id),
    )
    mydb.commit()

def add_data_shopkeeper_phone(Shopkeeper_id, Phone_no):
    c.execute(
        "INSERT INTO SHOPKEEPER_PHONE(Shopkeeper_id, Phone_no) VALUES (%s,%s)",
        (Shopkeeper_id, Phone_no),
    )
    mydb.commit()

def add_data_shopkeeper_product(Shopkeeper_id, P_Name, Initial_Quantity, Present_Quantity):
    c.execute(
        "INSERT INTO SHOPKEEPER_PRODUCT(Shopkeeper_id, P_Name, Initial_Quantity, Present_Quantity) VALUES (%s,%s,%s,%s)",
        (Shopkeeper_id, P_Name, Initial_Quantity, Present_Quantity),
    )
    mydb.commit()

##############################################################################################################3


def view_admin_data():
    c.execute("SELECT * FROM ADMIN")
    data = c.fetchall()
    return data

def view_admin_phone_data():
    c.execute("SELECT * FROM ADMIN_PHONE")
    data = c.fetchall()
    return data

def view_bill_data():
    c.execute("SELECT * FROM BILL")
    data = c.fetchall()
    return data

def view_bill_product_data():
    c.execute("SELECT * FROM BILL_PRODUCT")
    data = c.fetchall()
    return data

def view_customer_data():
    c.execute("SELECT * FROM customer")
    data = c.fetchall()
    return data

def view_customer_phone_data():
    c.execute("SELECT * FROM CUSTOMER_PHONE")
    data = c.fetchall()
    return data

def view_dependent_data():
    c.execute("SELECT * FROM DEPENDENT")
    data = c.fetchall()
    return data

def view_product_data():
    c.execute("SELECT * FROM PRODUCT")
    data = c.fetchall()
    return data

def view_product_customer_data():
    c.execute("SELECT * FROM PRODUCT_CUSTOMER")
    data = c.fetchall()
    return data

def view_shopkeeper_data():
    c.execute("SELECT * FROM SHOPKEEPER")
    data = c.fetchall()
    return data

def view_shopkeeper_product_data():
    c.execute("SELECT * FROM SHOPKEEPER_PRODUCT")
    data = c.fetchall()
    return data

def view_shopkeeper_phone_data():
    c.execute("SELECT * FROM SHOPKEEPER_PHONE")
    data = c.fetchall()
    return data

#########################################################################################################   
def view_only_admin_id():
    c.execute("SELECT Admin_id FROM ADMIN")
    data = c.fetchall()
    return data

def view_only_admin_phone(Admin_id):
    c.execute('SELECT Phone_no FROM ADMIN_PHONE WHERE Admin_id ="{}"'.format(Admin_id))
    data = c.fetchall()
    return data
    
def view_only_bill_id():
    c.execute("SELECT Bill_id FROM BILL")
    data = c.fetchall()
    return data

def view_only_bill_product_names(Bill_id):
    c.execute('SELECT P_Name FROM BILL_PRODUCT WHERE Bill_id = "{}"'.format(Bill_id))
    data = c.fetchall()
    return data


def view_only_rfid():
    c.execute("SELECT RFID FROM CUSTOMER")
    data = c.fetchall()
    return data

def view_only_customer_phone(rfid):
    c.execute('SELECT Phone_no FROM CUSTOMER_PHONE WHERE RFID ="{}"'.format(rfid))
    data = c.fetchall()
    return data

def view_only_dependent(RFID):
    c.execute('SELECT D_Name FROM DEPENDENT WHERE RFID = "{}"'.format(RFID))
    data = c.fetchall()
    return data

def view_only_product_names():
    c.execute("SELECT P_Name FROM PRODUCT")
    data = c.fetchall()
    return data

def view_only_shopkeeper_id():
    c.execute("SELECT Shopkeeper_id FROM SHOPKEEPER")
    data = c.fetchall()
    return data

def view_only_shopkeeper_phone(Shopkeeper_id):
    c.execute('SELECT Phone_no FROM SHOPKEEPER_PHONE WHERE Shopkeeper_id ="{}"'.format(Shopkeeper_id))
    data = c.fetchall()
    return data

def view_only_customer_product_name(rfid):
    c.execute('SELECT P_Name FROM PRODUCT_CUSTOMER WHERE RFID ="{}"'.format(rfid))
    data = c.fetchall()
    return data

def view_shopkeeper_product_name(Shopkeeper_id):
    c.execute('SELECT P_Name FROM SHOPKEEPER_PRODUCT WHERE  Shopkeeper_id="{}"'.format(Shopkeeper_id))
    data = c.fetchall()
    return data

# def view_only_bill_product():
#     c.execute("SELECT Bill_id, P_Name FROM BILL_PRODUCT")
#     data = c.fetchall()
#     return data
##############################################################################################################



def get_customer(RFID):
    c.execute('SELECT * FROM CUSTOMER WHERE RFID="{}"'.format(RFID))
    data = c.fetchall()
    return data

def get_bill(Bill_id):
    c.execute('SELECT * FROM BILL WHERE Bill_id="{}"'.format(Bill_id))
    data = c.fetchall()
    return data

def get_dependent(D_Name, RFID):
    c.execute('SELECT * FROM DEPENDENT WHERE D_Name = "{}" AND RFID="{}"'.format(D_Name, RFID))
    data = c.fetchall()
    return data

def get_product(P_Name):
    c.execute('SELECT * FROM product WHERE P_Name="{}"'.format(P_Name))
    data = c.fetchall()
    return data

def get_shopkeeper(Shopkeeper_id):
    c.execute('SELECT * FROM SHOPKEEPER WHERE Shopkeeper_id="{}"'.format(Shopkeeper_id))
    data = c.fetchall()
    return data

def get_shopkeeper_phone(Shopkeeper_id, Phone_no):
    c.execute('SELECT * FROM SHOPKEEPER_PHONE WHERE Shopkeeper_id="{}" AND Phone_no="{}"'.format(Shopkeeper_id, Phone_no))
    data = c.fetchall()
    return data

def get_customer_phone(RFID, Phone_no):
    c.execute('SELECT * FROM CUSTOMER_PHONE WHERE RFID="{}" AND Phone_no="{}"'.format(RFID, Phone_no))
    data = c.fetchall()
    return data

def get_bill_product(Bill_id, P_Name):
    c.execute('SELECT * FROM BILL_PRODUCT WHERE Bill_id="{}" AND P_Name="{}"'.format(Bill_id, P_Name))
    data = c.fetchall()
    return data

def get_product_customer(P_Name, RFID):
    c.execute('SELECT * FROM PRODUCT_CUSTOMER WHERE P_Name="{}" AND RFID = "{}"'.format(P_Name, RFID))
    data = c.fetchall()
    return data

def get_shopkeeper_product(Shopkeeper_id, P_Name):
    c.execute('SELECT * FROM SHOPKEEPER_PRODUCT WHERE Shopkeeper_id="{}" AND P_Name="{}"'.format(Shopkeeper_id, P_Name))
    data = c.fetchall()
    return data

###########################################################################################################
def edit_product_data(
    new_P_Name,
    new_Cost_per_unit,
    new_Unit,
    P_Name,
    Cost_per_unit,
    Unit,
):
    c.execute(
        "UPDATE PRODUCT SET P_Name=%s, Cost_per_unit=%s, Unit=%s WHERE "
        "P_Name=%s and Cost_per_unit=%s and Unit=%s",
        (
            new_P_Name,
            new_Cost_per_unit,
            new_Unit,
            P_Name,
            Cost_per_unit,
            Unit,
        ),
    )
    mydb.commit()

def edit_customer_data(
    new_RFID, new_C_Fname, new_C_Lname, new_C_Email_id, new_DOB, new_Gender, new_Street_No, new_City, new_PIN, new_Admin_id, 
    RFID, C_Fname, C_Lname, C_Email_id, DOB, Gender, Street_No, City, PIN, Admin_id,
):
    c.execute(
        "UPDATE CUSTOMER SET RFID=%s, C_Fname=%s, C_Lname=%s, C_Email_id=%s, DOB=%s, Gender=%s, Street_No=%s, City=%s, PIN=%s, Admin_id=%s WHERE "
        "RFID=%s and C_Fname=%s and C_Lname=%s and C_Email_id=%s and DOB=%s and Gender=%s and Street_No=%s and City=%s and PIN=%s and Admin_id=%s",
        (
            new_RFID, new_C_Fname, new_C_Lname, new_C_Email_id, new_DOB, new_Gender, new_Street_No, new_City, new_PIN, new_Admin_id, 
            RFID, C_Fname, C_Lname, C_Email_id, DOB, Gender, Street_No, City, PIN, Admin_id,
        ),
    )
    mydb.commit()


def edit_bill_data(
    new_Bill_id, new_Total_cost, new_Issued_date, new_Last_valid_date, new_Present_date, new_Validity, new_Shopkeeper_id, new_RFID, 
    Bill_id, Total_cost, Issued_date, Last_valid_date, Present_date, Validity, Shopkeeper_id, RFID
):
    c.execute(
        "UPDATE BILL SET Bill_id=%s, Total_cost=%s, Issued_date=%s, Last_valid_date=%s, Present_date=%s, Validity=%s, Shopkeeper_id=%s, RFID=%s WHERE "
        "Bill_id=%s and Total_cost=%s and Issued_date=%s and Last_valid_date=%s and Present_date=%s and Validity=%s and Shopkeeper_id=%s and RFID=%s",
        (
            new_Bill_id, new_Total_cost, new_Issued_date, new_Last_valid_date, new_Present_date, new_Validity, new_Shopkeeper_id, new_RFID, 
            Bill_id, Total_cost, Issued_date, Last_valid_date, Present_date, Validity, Shopkeeper_id, RFID
        ),
    )
    mydb.commit()

def edit_bill_product_data(
    new_Bill_id, new_P_Name, new_Quantity, new_Total_cost_per_product,
    Bill_id, P_Name, Quantity, Total_cost_per_product
):
    c.execute(
        "UPDATE BILL_PRODUCT SET Bill_id=%s, P_Name=%s, Quantity=%s, Total_cost_per_product=%s WHERE "
        "Bill_id=%s and P_Name=%s and Quantity=%s and Total_cost_per_product=%s",
        (
            new_Bill_id, new_P_Name, new_Quantity, new_Total_cost_per_product,
            Bill_id, P_Name, Quantity, Total_cost_per_product
        ),
    )
    mydb.commit()

def edit_customer_phone_data(
    new_RFID, new_Phone_no,
    RFID, Phone_no
):
    c.execute(
        "UPDATE CUSTOMER_PHONE SET  RFID=%s, Phone_no=%s WHERE "
        "RFID=%s and Phone_no=%s",
        (
            new_RFID, new_Phone_no,
            RFID, Phone_no
        ),
    )
    mydb.commit()

def edit_dependent_data(
    new_RFID, new_D_Name, new_DOB, new_Gender, new_Age, new_Relation,
    RFID, D_Name, DOB, Gender, Age, Relation
):
    c.execute(
        "UPDATE DEPENDENT SET RFID=%s, D_Name=%s, DOB=%s, Gender=%s, Age=%s, Relation=%s WHERE "
        "RFID=%s and D_Name=%s and DOB=%s and Gender=%s and Age=%s and Relation=%s",
        (
            new_RFID, new_D_Name, new_DOB, new_Gender, new_Age, new_Relation,
            RFID, D_Name, DOB, Gender, Age, Relation
        ),
    )
    mydb.commit()

def edit_product_customer_data(
    new_P_Name, new_RFID, 
    P_Name, RFID
):
    c.execute(
        "UPDATE PRODUCT_CUSTOMER SET P_Name=%s, RFID=%s WHERE "
        "P_Name=%s and RFID=%s",
        (
            new_P_Name, new_RFID, 
            P_Name, RFID
        ),
    )
    mydb.commit()


def edit_shopkeeper_data(
    new_Shopkeeper_id, new_S_Fname, new_S_Lname, new_Store_name, new_Street_No, new_City, new_PIN, new_Admin_id,
    Shopkeeper_id, S_Fname, S_Lname, Store_name, Street_No, City, PIN, Admin_id
):
    c.execute(
        "UPDATE SHOPKEEPER SET Shopkeeper_id=%s, S_Fname=%s, S_Lname=%s, Store_name=%s, Street_No=%s, City=%s, PIN=%s, Admin_id=%s WHERE "
        "Shopkeeper_id=%s and S_Fname=%s and S_Lname=%s and Store_name=%s and Street_No=%s and City=%s and PIN=%s and Admin_id=%s",
        (
            new_Shopkeeper_id, new_S_Fname, new_S_Lname, new_Store_name, new_Street_No, new_City, new_PIN, new_Admin_id,
            Shopkeeper_id, S_Fname, S_Lname, Store_name, Street_No, City, PIN, Admin_id
        ),
    )
    mydb.commit()

def edit_shopkeeper_product_data(
    new_Shopkeeper_id, new_P_Name, new_Initial_Quantity, new_Present_Quantity,
    Shopkeeper_id, P_Name, Initial_Quantity, Present_Quantity
):
    c.execute(
        "UPDATE SHOPKEEPER_PRODUCT SET Shopkeeper_id=%s, P_Name=%s, Initial_Quantity=%s, Present_Quantity=%s WHERE "
        "Shopkeeper_id=%s and P_Name=%s and Initial_Quantity=%s and Present_Quantity=%s",
        (
            new_Shopkeeper_id, new_P_Name, new_Initial_Quantity, new_Present_Quantity,
            Shopkeeper_id, P_Name, Initial_Quantity, Present_Quantity
        ),
    )
    mydb.commit()

def edit_shopkeeper_phone_data(
    new_Shopkeeper_id, new_Phone_no,
    Shopkeeper_id, Phone_no
):
    c.execute(
        "UPDATE SHOPKEEPER_PHONE SET  Shopkeeper_id=%s, Phone_no=%s WHERE "
        "Shopkeeper_id=%s and Phone_no=%s",
        (
            new_Shopkeeper_id, new_Phone_no,
            Shopkeeper_id, Phone_no
        ),
    )
    mydb.commit()
#######################################################################################################################

def delete_data_bill(Bill_id):
    c.execute('DELETE FROM BILL WHERE Bill_id="{}"'.format(Bill_id))
    mydb.commit()

def delete_data_bill_product(Bill_id, P_Name):
    c.execute('DELETE FROM BILL_PRODUCT WHERE Bill_id="{}" and P_Name="{}"'.format(Bill_id, P_Name))
    mydb.commit()

def delete_data_customer(RFID):
    c.execute('DELETE FROM CUSTOMER WHERE RFID="{}"'.format(RFID))
    mydb.commit()

def delete_data_customer_phone(RFID, Phone):
    c.execute('DELETE FROM CUSTOMER_PHONE WHERE RFID="{}" and Phone_no="{}"'.format(RFID, Phone))
    mydb.commit()

def delete_data_dependent(D_Name, RFID):
    c.execute('DELETE FROM DEPENDENT WHERE D_Name="{}" and RFID="{}"'.format(D_Name, RFID))
    mydb.commit()

def delete_data_product(P_Name):
    c.execute('DELETE FROM PRODUCT WHERE P_Name="{}"'.format(P_Name))
    mydb.commit()

def delete_data_product_customer(P_Name, RFID):
    c.execute('DELETE FROM PRODUCT_CUSTOMER WHERE P_Name="{}" AND RFID="{}"'.format(P_Name, RFID))
    mydb.commit()

def delete_data_shopkeeper(Shopkeeper_id):
    c.execute('DELETE FROM SHOPKEEPER WHERE Shopkeeper_id="{}"'.format(Shopkeeper_id))
    mydb.commit()

def delete_data_shopkeeper_product(Shopkeeper_id, P_Name):
    c.execute('DELETE FROM SHOPKEEPER_PRODUCT WHERE Shopkeeper_id="{}" and P_Name="{}"'.format(Shopkeeper_id, P_Name))
    mydb.commit()

def delete_data_shopkeeper_phone(Shopkeeper_id, Phone_no):
    c.execute('DELETE FROM SHOPKEEPER_PHONE WHERE Shopkeeper_id="{}" and Phone_no="{}"'.format(Shopkeeper_id, Phone_no))
    mydb.commit()

##########################################################################
def queryy(x):
    c.execute(x)
    data = c.fetchall()
    return data


def get_product_price(P_Name):
    c.execute('SELECT Cost_per_unit FROM PRODUCT WHERE P_Name = "{}"'.format(P_Name))
    data = c.fetchall()
    return data

def get_total_cost(Bill_id):
    c.execute('SELECT Total_cost FROM Bill WHERE Bill_id = "{}"'.format(Bill_id))
    data = c.fetchall()
    return data

def view_shopkeeper_product_name_quantity(Shopkeeper_id):
    c.execute('SELECT P_Name FROM SHOPKEEPER_PRODUCT WHERE Present_Quantity > 0 AND Shopkeeper_id = "{}"'.format(Shopkeeper_id))
    data = c.fetchall()
    return data

def update_product_quantity(Shopkeeper_id, P_Name, cus_quantity):
    c.execute(
        "UPDATE SHOPKEEPER_PRODUCT SET Present_Quantity=Present_Quantity-%s WHERE "
        "Shopkeeper_id=%s and P_Name=%s",
        (
             cus_quantity, Shopkeeper_id, P_Name
        ),
    )
    mydb.commit()


def view_sales():
    c.execute('SELECT * FROM SALE')
    data = c.fetchall()
    return data


def sales_between_dates():
    date1 = st.text_input("Starting date : ")
    date2 = st.text_input("Ending date : ")
    if st.button("View Result"):
        c.execute("TRUNCATE TABLE SALE")
        c.execute(
            "CALL sale_pro(%s,%s)",
            (
                date1, date2
            )
        )
        mydb.commit()
        result = view_sales()
        df = pd.DataFrame(
            result,
            columns=[
                "P_Name",
            ],
        )
        with st.expander("View Sales"):
            st.dataframe(df)
        with st.expander("Pie chart"):
            task_df = df["P_Name"].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1=px.pie(task_df, names="index", values="P_Name")
            st.plotly_chart(p1)
    


#########################################################################


def view_Shopkeeper_customer_bill():
    c.execute('SELECT * FROM Shopkeeper_customer_bill')
    data = c.fetchall()
    return data


def Shopkeeper_customer_bill():
    shk= st.text_input("Shopkeeper_id : ")
    if st.button("View Result"):
        #c.execute("TRUNCATE TABLE Shopkeeper_customer_bill")
        c.execute(
            "CALL customer_product_bill('%s');",
            (
                shk
            )
        )
        mydb.commit()
        result = view_Shopkeeper_customer_bill()
        df = pd.DataFrame(
            result,
            columns=[
                "C_Fname", "C_Lname","P_Name","Present_date", "Shopkeeper_id",
            ],
        )
        with st.expander("View Shopkeeper_customer_bill"):
            st.dataframe(df)