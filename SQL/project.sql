------POPULATE THE TABLE------

--USING INSERT COMMAND--
INSERT INTO SHOPKEEPER(Shopkeeper_id, S_Fname, S_Lname, Store_name, Street_No, City, PIN, Admin_id) VALUES
('SHK_001',	'Manisha',	'Solanki',	'Lakshmi FPS',	'M G Road',	'Bengaluru',	575030,	'ADM_001'),
('SHK_002',	'Bharti',	'Devgan',	'Mahaveer FPS',	'NAL Wind Tunnel Road',	'Mangaluru',	560059,	'ADM_003'),
('SHK_003',	'Roopa',	'Ram',	'Goudra FPS',	'Bunder Road',	'Belagavi',	575023,	'ADM_002'),
('SHK_004',	'Pallavi',	'Ram',	'Mirje FPS',	'Lavelle Road',	'Kalaburgi',	560044,	'ADM_003'),
('SHK_005',	'Ravi',	'Naik',	'Padmavati FPS',	'Thiru V ka Salai',	'Udupi',	600045,	'ADM_001'),
('SHK_006',	'Virat',	'Murthy',	'Munnoli FPS',	'Bejai New Road',	'KGF',	575011,	'ADM_002');


--USING LOAD COMMAND--
LOAD DATA INFILE "C:\\Users\\Sanam\\Desktop\\Study\\DBMS\\Project\\Final\\Data\\ADMIN.csv" INTO TABLE ADMIN
COLUMNS TERMINATED BY ',' 
OPTIONALLY ENCLOSED BY '"' 
ESCAPED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 0 LINES;




------JOIN------

--1--
--Retrieve Customer name and son name iff customer has a son--
SELECT C_Fname, C_Lname, D_Name AS Son_Name FROM CUSTOMER JOIN DEPENDENTS ON CUSTOMER.RFID = DEPENDENTS.RFID WHERE DEPENDENTS.Relation = 'Son'; 


--2 RIGHT JOIN--
--Retrieve the customer name and dependent ame if customer has an dependents--
SELECT  D_Name, C_Fname, C_Lname FROM DEPENDENTS RIGHT JOIN CUSTOMER ON CUSTOMER.RFID = DEPENDENTS.RFID;


--3 LEFT JOIN--
--Retrieve the customer name and dependent ame if customer has an dependents--
SELECT C_Fname, C_Lname, D_Name FROM CUSTOMER LEFT JOIN DEPENDENTS ON CUSTOMER.RFID = DEPENDENTS.RFID;


--4--
--Retrieve the customer name and products bought date for thosa customers who bought the products between 28th feb 2021 and 3rd oct 2021--
SELECT C_Fname, C_Lname, Present_date AS Bought_date FROM CUSTOMER JOIN BILL ON CUSTOMER.RFID = BILL.RFID WHERE BILL.Present_date BETWEEN '2021-02-28' AND '2021-10-03';




------Aggregate Functions------

--1 SUM--
--Retrieve the total amount spent by each customer--
SELECT SUM(Total_cost) FROM bill GROUP BY RFID;


--2 MAX--
--Retrieve the bill id which has the maximum value for total cost--
SELECT Bill_id, Total_cost from bill where bill.Total_cost IN (SELECT MAX(Total_cost) FROM BILL);


--3 MIN--
--Retrieve the bill id which has the minimum value for total cost--
SELECT Bill_id, Total_cost from bill where bill.Total_cost IN (SELECT MIN(Total_cost) FROM BILL);


--4 COUNT--
--Retrieve the number of bills which has the total cost equal to 170--
SELECT COUNT(Total_cost) from bill WHERE Total_cost IN (SELECT MAX(Total_cost) FROM BILL);


--5 AVG--
--Retrieve the RFID of customer and there average cost spent by them--
SELECT RFID, AVG(Total_cost) from bill GROUP BY RFID;




------SET Operations------

--1 UNION--
--Retrive the phone numbers that are present in either admin or shopkeepers table--
SELECT ADMIN_PHONE.Phone_no FROM ADMIN_PHONE
UNION
SELECT SHOPKEEPER_PHONE.Phone_no FROM SHOPKEEPER_PHONE;

--2 ALL UNION--
--Retrive all the phone numbers that are present in admin or shopkeepers table--
SELECT ADMIN_PHONE.Phone_no FROM ADMIN_PHONE
UNION ALL
SELECT SHOPKEEPER_PHONE.Phone_no FROM SHOPKEEPER_PHONE;


--3 INTERSECT--
--Retrieve the first names which are present in both customer and shopkeeper table--
SELECT C.C_Fname FROM CUSTOMER C
INTERSECT
SELECT S.S_Fname FROM SHOPKEEPER S;


--4 INTERSECT--
--Retrieve the Cities which are present in both customer and shopkeeper table--
SELECT S.City FROM SHOPKEEPER S
INTERSECT
SELECT C.City FROM CUSTOMER C;




------Functions and Procedures------

--1 FUNCTION--
--Create a function to check the eligibility of a particular age for ration card-- 
DELIMITER $$
create function eligible(Age int)
	RETURNS varchar(20)
    DETERMINISTIC
    BEGIN
    IF Age > 10 THEN
    RETURN ("yes");
    ELSE
    RETURN ("No");
    END IF;
    end$$
DELIMITER ;
select eligible(11);
select eligible(9);


--2 procedure--
--Create a procedure to count valid bills--
DELIMITER $$
CREATE PROCEDURE count_valid_bills(OUT p1 INT)
    BEGIN 
    select COUNT(Bill_id)INTO p1 from BILL WHERE Validity = 'Valid';
    END $$
DELIMITER ;
CALL count_valid_bills(@p);
SELECT @p;


--3 procudere--
--Create a procedure to retrieve given number of cutomers(number of customers to be retrieved shuold be given as input)--
DELIMITER $$
CREATE PROCEDURE get_customer_limit(IN var1 INT)
    BEGIN
    select * from CUSTOMER limit var1;
    select count(RFID) as total_customer from CUSTOMER;
    END $$
DELIMITER ;
CALL get_customer_limit(10);


--4 PROCEDURE--
--Create a procedure to retrieve all the customers managed by given admin(admin id shuold be given as input)--
DELIMITER $$
CREATE PROCEDURE get_customer_admin(in Adm varchar(10))
    BEGIN
    select C_Fname, C_Lname, RFID
    from CUSTOMER WHERE CUSTOMER.Admin_id = Adm;
end $$
DELIMITER ;
CALL get_customer_admin('ADM_001');




------Triggers and cursors------

--1 trigger BUYING DATE--
--Create a trigger to check the validity of newly inserting bill--
DELIMITER $$
CREATE TRIGGER buying_date 
BEFORE INSERT
ON BILL
FOR EACH ROW
BEGIN
    IF new.Present_date > new.Last_valid_date THEN SET new.Validity = 'Invalid';
    END IF;
END$$
DELIMITER ;
INSERT INTO BILL VALUES('B_049', 160, '2022-11-14', '2022-11-17', '2022-11-18', 'Valid', 'SHK_003', 3453484810);


--2 trigger DEPENDENT AGE--
--Create a trigger to show error when the age of the newly inserting dependent is less than 10--
DELIMITER $$
CREATE TRIGGER dependent_age 
BEFORE INSERT 
ON DEPENDENT
FOR EACH ROW
BEGIN
    DECLARE error_msg VARCHAR(300);
    SET error_msg = ("Age of the dependent should be 10 or more");
    IF new.Age < 10 THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = error_msg;
    END IF;
END $$
DELIMITER ;
INSERT INTO DEPENDENT VALUES(3453484810, 'Aniket', '2013-12-3', 'M', '9', 'Son');
INSERT INTO DEPENDENT VALUES(3453484810, 'Aniket', '2011-12-3', 'M', '10', 'Son');


--3 cursor valid bills--
--Use cursor to add valid bills to the newly created table--
CREATE TABLE VALID_BILLS(
    Bill_id VARCHAR(10),
    Total_cost INT(5),
    Issued_date DATE,
    Last_valid_date DATE,
    Present_date DATE,
    Validity VARCHAR(20),
    Shopkeeper_id VARCHAR(10),
    RFID BIGINT(10)
);

DELIMITER $$
CREATE PROCEDURE get_valid_bills()
BEGIN
    DECLARE done int default 0;
    DECLARE b_total_cost INTEGER;
    DECLARE b_RFID bigint;
    DECLARE b_bill_id, b_validity, b_shopkeeper_id varchar(20);
    DECLARE b_issued_date, b_last_valid_date, b_present_date date;
    DECLARE cur cursor for select * from BILL WHERE BILL.VALIDITY = 'Valid';
    DECLARE continue handler for not found set done = 1;
    
    OPEN cur;
    
    label: LOOP
    fetch cur into b_bill_id, b_total_cost, b_issued_date, b_last_valid_date, b_present_date, b_validity, b_shopkeeper_id, b_RFID;
    if done = 1 then leave label;
    end if;
    INSERT INTO VALID_BILLS VALUES(b_bill_id, b_total_cost, b_issued_date, b_last_valid_date, b_present_date, b_validity, b_shopkeeper_id, b_RFID);
    end loop;

    close cur;
end$$

DELIMITER ;
CALL get_valid_bills;


--4 cursor customer email--
--Use cursor to add name a email id of customers to the newly created table--
CREATE TABLE CUSTOMER_EMAIL(
    Fname varchar(10),
    Lname varchar(10),
    Email_id VARCHAR(50)
);

DELIMITER $$
CREATE PROCEDURE create_email_list ()
BEGIN
	DECLARE done INTEGER DEFAULT 0;
    DECLARE Fname varchar(10) ;
    DECLARE Lname varchar(10) ;
	DECLARE emailAddress varchar(100) ;
	DEClARE curEmail CURSOR FOR SELECT C_Fname, C_Lname, C_Email_id FROM CUSTOMER;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	OPEN curEmail;

	LABLE: LOOP
	FETCH curEmail INTO Fname, Lname, emailAddress;
	IF done = 1 THEN 
	LEAVE LABLE;
	END IF;
	INSERT INTO CUSTOMER_EMAIL VALUES(Fname, Lname, emailAddress);
	END LOOP;

	CLOSE curEmail;
END$$

DELIMITER ;
CALL create_email_list();






-----------------------------------

ALTER TABLE CUSTOMER
drop CONSTRAINT CUSTOMER_ibfk_1;

ALTER TABLE CUSTOMER
    add constraint CUSTOMER_ibfk_1
    FOREIGN KEY (Bill_id)
    REFERENCES BILL(Bill_id)
    ON DELETE CASCADE;

SELECT P_Name, Sum(Quantity) FROM (SELECT P_Name, Quantity from BILL JOIN BILL_PRODUCT ON BILL.Bill_id=BILL_PRODUCT.Bill_id WHERE Present_date BETWEEN "2022-11-01" AND "2022-11-30") AS A GROUP BY P_Name ;

SELECT RFID, P_Name, Quantity from BILL JOIN BILL_PRODUCT ON BILL.Bill_id=BILL_PRODUCT.Bill_id WHERE Present_date BETWEEN "2021-11-01" AND "2021-11-30";



----------------------------------------------------------

CREATE TABLE SALE(
    P_Name VARCHAR(20)
);

DELIMITER $$
CREATE PROCEDURE sale_pro(in date1 VARCHAR(20),in date2 VARCHAR(20))
BEGIN
	DECLARE done INTEGER DEFAULT 0;
    DECLARE b_P_Name VARCHAR(20);
	DEClARE curSale CURSOR FOR SELECT P_Name from BILL JOIN BILL_PRODUCT ON BILL.Bill_id=BILL_PRODUCT.Bill_id WHERE Present_date BETWEEN date1 AND date2;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	OPEN curSale;

	LABLE: LOOP
	FETCH curSale INTO b_P_Name;
	IF done = 1 THEN 
	LEAVE LABLE;
	END IF;
	INSERT INTO SALE VALUES(b_P_Name);
	END LOOP;

	CLOSE curSale;
END$$

DELIMITER ;
CALL sale_pro();


SELECT P_Name from BILL JOIN BILL_PRODUCT ON BILL.Bill_id=BILL_PRODUCT.Bill_id WHERE Present_date BETWEEN "2022-11-01" AND "2022-11-30";

SELECT C_Fname, C_Lname, P_Name, Present_date, Shopkeeper_id FROM CUSTOMER NATURAL JOIN BILL NATURAL JOIN PRODUCT_CUSTOMER WHERE BILL.Shopkeeper_id = "SHK_001";

-----------------------------------------------------------------------


CREATE TABLE Shopkeeper_customer_bill(
    C_Fname VARCHAR(20),
    C_Lname VARCHAR(20),
    P_Name VARCHAR(20),
    Present_date DATE,
    Shopkeeper_id VARCHAR(20)
);


DELIMITER $$
CREATE PROCEDURE customer_product_bill(in shk_id varchar(10))
BEGIN
	DECLARE done INTEGER DEFAULT 0;
    DECLARE b_C_Fname VARCHAR(20);
    DECLARE b_C_Lname VARCHAR(20);
    DECLARE b_P_Name VARCHAR(20);
    DECLARE b_Present_date DATE;
    DECLARE b_Shopkeeper_id VARCHAR(20);
	DEClARE cur1 CURSOR FOR  SELECT C_Fname, C_Lname, P_Name, Present_date, Shopkeeper_id FROM CUSTOMER NATURAL JOIN BILL NATURAL JOIN PRODUCT_CUSTOMER WHERE BILL.Shopkeeper_id = shk_id;
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	OPEN cur1;

	LABLE: LOOP
	FETCH cur1 INTO b_C_Fname, b_C_Lname, b_P_Name, b_Present_date, b_Shopkeeper_id;
	IF done = 1 THEN 
	LEAVE LABLE;
	END IF;
	INSERT INTO Shopkeeper_customer_bill VALUES(b_C_Fname, b_C_Lname, b_P_Name, b_Present_date, b_Shopkeeper_id);
	END LOOP;

	CLOSE cur1;
END$$

DELIMITER ;