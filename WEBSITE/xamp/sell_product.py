import streamlit as st
from database import *
from update import *

def sell_product():
    col4, col2 = st.columns(2)
    with col4:
        Bill_id = st.text_input("Bill id:")
        Shopkeeper_id = st.text_input("Shopkeeper id:")
    with col2:
        RFID = st.text_input("RFID:")
    Total_cost = get_total_cost(Bill_id)
    Issued_date = st.date_input("Issued date:")
    Last_valid_date = st.date_input("Last Valid Date:")     
    Present_date = st.date_input("Present Date:")
    Validity = st.text_input("Validity:")
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
                list_of_product1 = [i[0] for i in view_shopkeeper_product_name_quantity(Shopkeeper_id)]
                selected_product1 = st.selectbox("Products", list_of_product1, key="P11")
                P_Name1 = st.text_input("Product name :", selected_product1, key="P12")
                cus_Quantity1 = st.number_input("Buying Quantity:", value=0, step=1, key="P13")
                Price1 = st.number_input("Price : ", step=1, key="P14")
                Total_cost_per_product1 = st.number_input("Total cost per product:", Price1 * cus_Quantity1, key="P15")
    with col2:
                list_of_product2 = [i[0] for i in view_shopkeeper_product_name_quantity(Shopkeeper_id)]
                selected_product2 = st.selectbox("Products", list_of_product2, key="P21")
                P_Name2 = st.text_input("Product name :", selected_product2, key="P22")
                cus_Quantity2 = st.number_input("Buying Quantity:", value=0, step=1, key="P23")
                Price2 = st.number_input("Price : ", step=1, key="P24")
                Total_cost_per_product2 = st.number_input("Total cost per product:", Price2 * cus_Quantity2, key="P25")
    with col3:
                list_of_product3 = [i[0] for i in view_shopkeeper_product_name_quantity(Shopkeeper_id)]
                selected_product3 = st.selectbox("Products", list_of_product3, key="P31")
                P_Name3 = st.text_input("Product name :", selected_product3, key="P32")
                cus_Quantity3 = st.number_input("Buying Quantity:", value=0, step=1, key="P33")
                Price3 = st.number_input("Price : ", step=1, key="P34")
                Total_cost_per_product3 = st.number_input("Total cost per product:", Price3 * cus_Quantity3, key="P35")
    with col4:
                list_of_product4 = [i[0] for i in view_shopkeeper_product_name_quantity(Shopkeeper_id)]
                selected_product4 = st.selectbox("Products", list_of_product4, key="P41")
                P_Name4 = st.text_input("Product name :", selected_product4, key="P42")
                cus_Quantity4 = st.number_input("Buying Quantity:", value=0, step=1, key="P43")
                Price4 = st.number_input("Price : ", step=1, key="P44")
                Total_cost_per_product4 = st.number_input("Total cost per product:", Price4 * cus_Quantity4, key="P45")
    with col5:
                list_of_product5 = [i[0] for i in view_shopkeeper_product_name_quantity(Shopkeeper_id)]
                selected_product5 = st.selectbox("Products", list_of_product5, key="P51")
                P_Name5 = st.text_input("Product name :", selected_product5, key="P52")
                cus_Quantity5 = st.number_input("Buying Quantity:", value=0, step=1, key="P53")
                Price5 = st.number_input("Price : ", step=1, key="P54")
                Total_cost_per_product5 = st.number_input("Total cost per product:", Price5 * cus_Quantity5, key="P55")
    with col6:
                list_of_product6 = [i[0] for i in view_shopkeeper_product_name_quantity(Shopkeeper_id)]
                selected_product6 = st.selectbox("Products", list_of_product6, key="P61")
                P_Name6 = st.text_input("Product name :", selected_product6, key="P62")
                cus_Quantity6 = st.number_input("Buying Quantity:", value=0, step=1, key="P63")
                Price6 = st.number_input("Price : ", step=1, key="P64")
                Total_cost_per_product6 = st.number_input("Total cost per product:", Price6 * cus_Quantity6, key="P65")
    Total = Total_cost_per_product1+Total_cost_per_product2+Total_cost_per_product3+Total_cost_per_product4+Total_cost_per_product5+Total_cost_per_product6
    Total_cost = st.text_input("Total cost : ", Total)
    if st.button("Add Product"):
                add_data_bill(Bill_id, Total_cost, Issued_date, Last_valid_date, Present_date, Validity, Shopkeeper_id, RFID)
                st.success("Successfully added Bill: {}".format(Bill_id))
                if(Last_valid_date >= Present_date):
                    if(cus_Quantity1!=0):
                        add_data_bill_product(Bill_id, P_Name1, cus_Quantity1, Total_cost_per_product1)
                        st.success('Successfully added Bill: "{}" and Product :"{}"'.format(Bill_id, P_Name1))
                        update_product_quantity(Shopkeeper_id, P_Name1, cus_Quantity1)
                        st.success('Successfully updated quantity of Product: "{}" for Shopkeeper  :"{}"'.format(P_Name1, Shopkeeper_id))
                    if(cus_Quantity2!=0):
                        add_data_bill_product(Bill_id, P_Name2, cus_Quantity2, Total_cost_per_product2)
                        st.success('Successfully added Bill: "{}" and Product :"{}"'.format(Bill_id, P_Name2))
                        update_product_quantity(Shopkeeper_id, P_Name2, cus_Quantity2)
                        st.success('Successfully updated quantity of Product: "{}" for Shopkeeper  :"{}"'.format(P_Name2, Shopkeeper_id))
                    if(cus_Quantity3!=0):
                        add_data_bill_product(Bill_id, P_Name3, cus_Quantity3, Total_cost_per_product3)
                        st.success('Successfully added Bill: "{}" and Product :"{}"'.format(Bill_id, P_Name3))
                        update_product_quantity(Shopkeeper_id, P_Name3, cus_Quantity3)
                        st.success('Successfully updated quantity of Product: "{}" for Shopkeeper  :"{}"'.format(P_Name3, Shopkeeper_id))
                    if(cus_Quantity4!=0):
                        add_data_bill_product(Bill_id, P_Name4, cus_Quantity4, Total_cost_per_product4)
                        st.success('Successfully added Bill: "{}" and Product :"{}"'.format(Bill_id, P_Name4))
                        update_product_quantity(Shopkeeper_id, P_Name4, cus_Quantity4)
                        st.success('Successfully updated quantity of Product: "{}" for Shopkeeper  :"{}"'.format(P_Name4, Shopkeeper_id))
                    if(cus_Quantity5!=0):
                        add_data_bill_product(Bill_id, P_Name5, cus_Quantity5, Total_cost_per_product5)
                        st.success('Successfully added Bill: "{}" and Product :"{}"'.format(Bill_id, P_Name5))
                        update_product_quantity(Shopkeeper_id, P_Name5, cus_Quantity5)
                        st.success('Successfully updated quantity of Product: "{}" for Shopkeeper  :"{}"'.format(P_Name5, Shopkeeper_id))
                    if(cus_Quantity6!=0):
                        add_data_bill_product(Bill_id, P_Name6, cus_Quantity6, Total_cost_per_product6)
                        st.success('Successfully added Bill: "{}" and Product :"{}"'.format(Bill_id, P_Name6))
                        update_product_quantity(Shopkeeper_id, P_Name6, cus_Quantity6)
                        st.success('Successfully updated quantity of Product: "{}" for Shopkeeper  :"{}"'.format(P_Name6, Shopkeeper_id))