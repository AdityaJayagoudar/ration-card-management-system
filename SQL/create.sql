CREATE TABLE ADMIN(
    Admin_id VARCHAR(10),
    A_Fname VARCHAR(20),
    A_Lname VARCHAR(20),
    A_Email_id VARCHAR(50),
    DOB DATE,
    Age INT(3),
    Street_no VARCHAR(40),
    PIN INT(6),
    PRIMARY KEY (Admin_id)
);

CREATE TABLE SHOPKEEPER(
    Shopkeeper_id VARCHAR(10),
    S_Fname VARCHAR(20),
    S_Lname VARCHAR(20),
    Store_name VARCHAR(20),
    Street_no VARCHAR(40),
    City VARCHAR(20),
    PIN INT(6),
    Admin_id VARCHAR(10),
    PRIMARY KEY (Shopkeeper_id),
    FOREIGN KEY (Admin_id) REFERENCES ADMIN (Admin_id)
);

CREATE TABLE PRODUCT(
    P_Name VARCHAR(20),
    Cost_per_unit float(5, 2),
    Unit VARCHAR(20),
    PRIMARY KEY (P_Name)
);

CREATE TABLE CUSTOMER(
    RFID BIGINT(20),
    C_Fname VARCHAR(20),
    C_Lname VARCHAR(20),
    C_Email_id VARCHAR(50),
    DOB DATE,
    Gender VARCHAR(10),
    Street_no VARCHAR(40),
    City VARCHAR(20),
    PIN INT(6),
    Admin_id VARCHAR(10),
    PRIMARY KEY (RFID),
    FOREIGN KEY (Admin_id) REFERENCES ADMIN (Admin_id)
);

CREATE TABLE DEPENDENT(
    RFID BIGINT(10),
    D_Name VARCHAR(20),
    DOB DATE,
    Gender VARCHAR(10),
    Age INT(3),
    Relation VARCHAR(20),
    FOREIGN KEY (RFID) REFERENCES CUSTOMER (RFID)
    ON DELETE CASCADE
);

CREATE TABLE BILL(
    Bill_id VARCHAR(10),
    Total_cost float(5, 2),
    Issued_date DATE,
    Last_valid_date DATE,
    Present_date DATE,
    Validity VARCHAR(20),
    Shopkeeper_id VARCHAR(10),
    RFID BIGINT(10),
    PRIMARY KEY (Bill_id),
    FOREIGN KEY (Shopkeeper_id) REFERENCES SHOPKEEPER (Shopkeeper_id),
    FOREIGN KEY (RFID) REFERENCES CUSTOMER (RFID)
    ON DELETE CASCADE
);

CREATE TABLE SHOPKEEPER_PRODUCT(
    Shopkeeper_id VARCHAR(10),
    P_Name VARCHAR(20),
    Initial_Quantity float(5, 2),
    Present_Quantity float(5, 2),
    PRIMARY KEY (Shopkeeper_id, P_Name),
    FOREIGN KEY (Shopkeeper_id) REFERENCES SHOPKEEPER (Shopkeeper_id),
    FOREIGN KEY (P_Name) REFERENCES PRODUCT (P_Name)
    ON DELETE CASCADE
);

CREATE TABLE BILL_PRODUCT(
    Bill_id VARCHAR(10),
    P_Name VARCHAR(20),
    Quantity float(5, 2),
    Total_cost_per_product float(5, 2),
    PRIMARY KEY (Bill_id, P_Name),
    FOREIGN KEY (Bill_id) REFERENCES BILL (Bill_id),
    FOREIGN KEY (P_Name) REFERENCES PRODUCT (P_Name)
    ON DELETE CASCADE
);

CREATE TABLE PRODUCT_CUSTOMER(
    P_Name VARCHAR(10),
    RFID BIGINT(20),
    PRIMARY KEY (P_Name, RFID),
    FOREIGN KEY (P_Name) REFERENCES PRODUCT (P_Name),
    FOREIGN KEY (RFID) REFERENCES CUSTOMER (RFID)
    ON DELETE CASCADE
);

CREATE TABLE CUSTOMER_PHONE(
    RFID BIGINT(20),
    Phone_no BIGINT(10),
    PRIMARY KEY (RFID, Phone_no),
    FOREIGN KEY (RFID) REFERENCES CUSTOMER (RFID)
    ON DELETE CASCADE
);

CREATE TABLE ADMIN_PHONE(
    Admin_id VARCHAR(10),
    Phone_no BIGINT(10),
    PRIMARY KEY (Admin_id, Phone_no),
    FOREIGN KEY (Admin_id) REFERENCES ADMIN (Admin_id)
    ON DELETE CASCADE
);

CREATE TABLE SHOPKEEPER_PHONE(
    Shopkeeper_id VARCHAR(10),
    Phone_no BIGINT(10),
    PRIMARY KEY (Shopkeeper_id, Phone_no),
    FOREIGN KEY (Shopkeeper_id) REFERENCES SHOPKEEPER (Shopkeeper_id)
    ON DELETE CASCADE
);



