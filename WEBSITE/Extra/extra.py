  # st.title("Ration Card System")
        # if st.button("SQL Query"):
        #     INPUT = st.text_input("Query :")
        #     c.execute(INPUT)














# create_table_admin()
        # create_table_customer()
        # create_table_shopkeeper()
        # create_table_product()
        # create_table_admin_phone()
        # create_table_shopkeeper_phone()
        # create_table_customer_phone()
        # create_table_bill()
        # create_table_bill_product()
        # create_table_dependent()
        # create_table_product_customer()
        # create_table_shopkeeper_product()

        # if choice == "Admin":
        #     Operations =["Add", "View", "Edit", "Remove"]
        #     selected1 = st.sidebar.selectbox("Operations", Operations)

        #     if selected1 == "Add":
        #         st.subheader("View all Product")
        #         create_admin()
        
        #     elif selected1 == "View":
        #         st.subheader("View all Product")
        #         read_admin()

        #     elif selected1 == "Edit":
        #         st.subheader("Update Product details:")
        #         update_admin()
        
        #     elif selected1 == "Remove":
        #         st.subheader("Delete Product details:")
        #         delete_admin()
        
        # elif choice == "Admin Phone":
        #     Operations =["Add", "View", "Edit", "Remove"]
        #     selected1 = st.sidebar.selectbox("Operations", Operations)

        #     if selected1 == "Add":
        #         st.subheader("View all Product")
        #         create_admin_phone()
        
        #     elif selected1 == "View":
        #         st.subheader("View all Product")
        #         read_admin_phone()

        #     elif selected1 == "Edit":
        #         st.subheader("Update Product details:")
        #         update_admin_phone()
        
        #     elif selected1 == "Remove":
        #         st.subheader("Delete Product details:")
        #         delete_admin_phone()







# names = ["Narendra Modi", "Droupadi Murmu", "Manmohan Singh"]
# usernames = ["ADM_001", "ADM_002", "ADM_003"]

# file_path = Path(__file__).parent / "hashed_pw.pkl"
# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)

# authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "sales_dashboard", "1234")

# name, authentication_status, username = authenticator.login("Login", "main")


# if authentication_status == False :
#         st.error("Username/password is incorrect")

# if authentication_status == None :
#         st.warning("Please enrer your username and password")

# if authentication_status :

#authenticator.logout("Logout", "sidebar")









# def create_table_admin():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS product(Admin_id TEXT, A_Fname TEXT, A_Lname TEXT, A_Email_id TEXT, DOB DATE, Age INT, Street_No TEXT, PIN INT)"
#     )

# def create_table_customer():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS customer(RFID BIGINT(20), FName TEXT, LName TEXT, Email_id TEXT, DOB DATE, Gender TEXT, Street_No TEXT, City TEXT, PIN INT, Admin_id TEXT)"
#     )

# def create_table_product():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS product(P_Name TEXT, Cost_per_unit TEXT, Unit TEXT)"
#     )

# def create_table_shopkeeper():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS customer(Shopkeeper_id TEXT, S_Fname TEXT, S_Lname TEXT, Store_name TEXT, Street_No TEXT, City TEXT, PIN INT, Admin_id TEXT)"
#     )

# def create_table_product():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS product(P_Name TEXT, Cost_per_unit TEXT, Unit TEXT)"
#     )

# def create_table_customer():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS customer(RFID TEXT, FName TEXT, LName TEXT, Email_id TEXT, DOB TEXT, Gender TEXT, Street_No TEXT, City TEXT, PIN TEXT, Admin_id TEXT)"
#     )
# def create_table_product():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS product(P_Name TEXT, Cost_per_unit TEXT, Unit TEXT)"
#     )

# def create_table_customer():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS customer(RFID TEXT, FName TEXT, LName TEXT, Email_id TEXT, DOB TEXT, Gender TEXT, Street_No TEXT, City TEXT, PIN TEXT, Admin_id TEXT)"
#     )

# def create_table_product():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS product(P_Name TEXT, Cost_per_unit TEXT, Unit TEXT)"
#     )

# def create_table_customer():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS customer(RFID TEXT, FName TEXT, LName TEXT, Email_id TEXT, DOB TEXT, Gender TEXT, Street_No TEXT, City TEXT, PIN TEXT, Admin_id TEXT)"
#     )
# def create_table_product():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS product(P_Name TEXT, Cost_per_unit TEXT, Unit TEXT)"
#     )

# def create_table_customer():
#     c.execute(
#         "CREATE TABLE IF NOT EXISTS customer(RFID TEXT, FName TEXT, LName TEXT, Email_id TEXT, DOB TEXT, Gender TEXT, Street_No TEXT, City TEXT, PIN TEXT, Admin_id TEXT)"
#     )













# def update_admin():
#     result = view_admin_data()
#     # st.write(result)
#     df = pd.DataFrame(
#         result,
#         columns=[
#             "Admin_id", "A_Fname", "A_Lname", "A_Email_id", "DOB", "Age","Street_No", "PIN",
#         ],
#     )
#     with st.expander("Current Admin Data"):
#         st.dataframe(df)
#     list_of_admins = [i[0] for i in view_only_admin_id()]
#     selected_admin = st.selectbox("Select Product to Edit", list_of_admins)
#     selected_result = get_admin(selected_admin)
#     # st.write(selected_result)
#     if selected_result:
#         Admin_id = selected_result[0][0]
#         A_Fname = selected_result[0][1]
#         A_Lname = selected_result[0][2]
#         A_Email_id = selected_result[0][3]
#         DOB = selected_result[0][4]
#         Age = selected_result[0][5]
#         Street_No = selected_result[0][6]
#         PIN = selected_result[0][7]

        
#         col1, col2 = st.columns(2)
#         with col1:
#             new_Admin_id = st.text_input("Admin id:", Admin_id)
#             new_A_Fname = st.text_input("First Name:", A_Fname)
#             new_A_Lname = st.text_input("Last Name:", A_Lname)
#             new_A_Email_id = st.text_input("Email id:", A_Email_id)
#         with col2:
#             new_DOB = st.text_input("Date of birth:", DOB)
#             new_Age = st.text_input("Age", Age)
#             new_Street_No = st.text_input("Street number:", Street_No)
#             new_PIN = st.text_input("PIN:", PIN)
#         if st.button("Update Admin"):
#             edit_admin_data(
#                 new_Admin_id, new_A_Fname, new_A_Lname, new_A_Email_id, new_DOB, new_Age, new_Street_No, new_PIN,
#                 Admin_id, A_Fname, A_Lname, A_Email_id, DOB, Age, Street_No, PIN
#             )
#             st.success(
#                 "Successfully updated Admin {}".format(A_Fname)
#             )

#     result2 = view_admin_data()
#     df2 = pd.DataFrame(
#         result2,
#         columns=[
#             "Admin_id", "A_Fname", "A_Lname", "A_Email_id", "DOB", "Age","Street_No", "PIN",
#         ],
#     )
#     with st.expander("Updated Admin data"):
#         st.dataframe(df2)



# def update_admin_phone():
#     result = view_admin_phone_data()
#     # st.write(result)
#     df = pd.DataFrame(
#         result,
#         columns=[
#             "Admin_id", "Phone_no",
#         ],
#     )
#     with st.expander("Current Admin phone Data"):
#         st.dataframe(df)
#     list_of_admin_phones = [i[0] for i in view_admin_phone_data()]
#     selected_admin_phone = st.selectbox("Select Admin phone to Edit", list_of_admin_phones)
#     selected_result = get_admin_phone(selected_admin_phone)
#     # st.write(selected_result)
#     if selected_result:
#         Admin_id = selected_result[0][0]
#         Phone_no = selected_result[0][1]
    
#         new_Admin_id = st.text_input("Admin id:", Admin_id)
#         new_Phone_no = st.text_input("Phone no:", Phone_no)
#         if st.button("Update Admin phone"):
#             edit_admin_phone_data(
#                 new_Admin_id, new_Phone_no,
#                 Admin_id, Phone_no
#             )
#             st.success(
#                 "Successfully updated Admin phone for admin id {}".format(Admin_id)
#             )

#     result2 = view_admin_phone_data()
#     df2 = pd.DataFrame(
#         result2,
#         columns=[
#             "Admin_id", "Phone_no",
#         ],
#     )
#     with st.expander("Updated Admin phone data"):
#         st.dataframe(df2)




# def delete_admin():
#     result = view_admin_data()
#     df = pd.DataFrame(
#         result,
#         columns=[
#             "Admin_id", "A_Fname", "A_Lname", "A_Email_id", "DOB", "Age","Street_No", "PIN",
#         ],
#     )
#     with st.expander("Current admin data"):
#         st.dataframe(df)

#     list_of_admins = [i[0] for i in view_only_admin_id()]
#     selected_admin = st.selectbox("Admin to Delete", list_of_admins)
#     if(selected_admin):
#         st.warning("Do you want to delete Admin {}? This action cannot be reversed!".format(selected_admin))
#     if st.button("DELETE ADMIN"):
#         delete_data_admin(selected_admin)
#         st.success("Admin {} has been deleted successfully, see Updated data below.".format(selected_admin))
#     new_result = view_admin_data()
#     df2 = pd.DataFrame(
#         new_result,
#         columns=[
#             "Admin_id", "A_Fname", "A_Lname", "A_Email_id", "DOB", "Age","Street_No", "PIN",
#         ],
#     )
#     with st.expander("Updated admin data"):
#         st.dataframe(df2)



# def delete_admin_phone():
#     result = view_admin_phone_data()
#     df = pd.DataFrame(
#         result,
#         columns=[
#             "Admin_id", "Phone_no",
#         ],
#     )
#     with st.expander("Current Admin phone data"):
#         st.dataframe(df)

#     list_of_admin_ids = [i[0] for i in view_only_admin_id()]
#     selected_admin_id = st.selectbox("Admin id", list_of_admin_ids)
#     list_of_admin_phones = [i[0] for i in view_only_admin_phone(selected_admin_id)]
#     selected_admin_phone = st.selectbox("Admin phone to Delete", list_of_admin_phones)
#     if(selected_admin_phone):
#         st.warning("Do you want to delete admin phone {}? This action cannot be reversed!".format(selected_admin_phone))
#     if st.button("DELETE ADMIN PHONE NO"):
#         delete_data_admin_phone(selected_admin_phone)
#         st.success("Admin phone {} has been deleted successfully, see Updated data below.".format(selected_admin_phone))
#     new_result = view_admin_phone_data()
#     df2 = pd.DataFrame(
#         new_result,
#         columns=[
#             "Admin_id", "Phone_no",
#         ],
#     )
#     with st.expander("Updated Admin phone data"):
#         st.dataframe(df2)





# def delete_data_admin(Admin_id):
#     c.execute('DELETE FROM ADMIN WHERE Admin_id="{}"'.format(Admin_id))
#     mydb.commit()

# def delete_data_admin_phone(Admin_id, Phone_no):
#     c.execute('DELETE FROM ADMIN_PHONE WHERE Admin_id="{}" and Phone_no="{}"'.format(Admin_id, Phone_no))
#     mydb.commit()

# def edit_admin_data(
#     new_Admin_id, new_A_Fname, new_A_Lname, new_A_Email_id, new_DOB, new_Age, new_Street_No, new_PIN,
#     Admin_id, A_Fname, A_Lname, A_Email_id, DOB, Age, Street_No, PIN
# ):
#     c.execute(
#         "UPDATE ADMIN SET Admin_id=%s, A_Fname=%s, A_Lname=%s, A_Email_id=%s, DOB=%s, Age=%s, Street_No=%s, PIN=%s WHERE "
#         "Admin_id=%s and A_Fname=%s and A_Lname=%s and A_Email_id=%s and DOB=%s and Age=%s and Street_No=%s and PIN=%s",
#         (
#             new_Admin_id, new_A_Fname, new_A_Lname, new_A_Email_id, new_DOB, new_Age, new_Street_No, new_PIN,
#             Admin_id, A_Fname, A_Lname, A_Email_id, DOB, Age, Street_No, PIN
#         ),
#     )
#     mydb.commit()


# def edit_admin_phone_data(
#     new_Admin_id, new_Phone_no,
#     Admin_id, Phone_no
# ):
#     c.execute(
#         "UPDATE ADMIN_PHONE SET  Admin_id=%s, Phone_no=%s WHERE "
#         "Admin_id=%s and Phone_no=%s",
#         (
#             new_Admin_id, new_Phone_no,
#             Admin_id, Phone_no
#         ),
#     )
#     mydb.commit()


# def get_admin(Admin_id):
#     c.execute('SELECT * FROM ADMIN WHERE Admin_id="{}"'.format(Admin_id))
#     data = c.fetchall()
#     return data


# def get_admin_phone(Admin_id, Phone_no):
#     c.execute('SELECT * FROM ADMIN_PHONE WHERE Admin_id="{}" AND Phone_no="{}"'.format(Admin_id, Phone_no))
#     data = c.fetchall()
#     return data






