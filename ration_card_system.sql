-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 30, 2022 at 09:44 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ration_card_system`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `count_valid_bills` (OUT `p1` INT)   BEGIN 
    select COUNT(Bill_id)INTO p1 from BILL WHERE Validity = 'Valid';
    END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `create_email_list` ()   BEGIN
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

CREATE DEFINER=`root`@`localhost` PROCEDURE `get_customer_admin` (IN `Adm` VARCHAR(10))   BEGIN
    select C_Fname, C_Lname, RFID
    from CUSTOMER WHERE CUSTOMER.Admin_id = Adm;
end$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `get_customer_limit` (IN `var1` INT)   BEGIN
    select * from CUSTOMER limit var1;
    select count(RFID) as total_customer from CUSTOMER;
    END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `get_valid_bills` ()   BEGIN
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

CREATE DEFINER=`root`@`localhost` PROCEDURE `sale_pro` (IN `date1` VARCHAR(20), IN `date2` VARCHAR(20))   BEGIN
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

--
-- Functions
--
CREATE DEFINER=`root`@`localhost` FUNCTION `eligible` (`Age` INT) RETURNS VARCHAR(20) CHARSET utf8mb4 DETERMINISTIC BEGIN
    IF Age > 10 THEN
    RETURN ("yes");
    ELSE
    RETURN ("No");
    END IF;
    end$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `Admin_id` varchar(10) NOT NULL,
  `A_Fname` varchar(20) DEFAULT NULL,
  `A_Lname` varchar(20) DEFAULT NULL,
  `A_Email_id` varchar(50) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Age` int(3) DEFAULT NULL,
  `Street_no` varchar(40) DEFAULT NULL,
  `PIN` int(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`Admin_id`, `A_Fname`, `A_Lname`, `A_Email_id`, `DOB`, `Age`, `Street_no`, `PIN`) VALUES
('ADM_001', 'Narendra ', 'Modi', 'modinarendra@gmail.com', '1966-04-14', NULL, 'Old Jail Road', 600047),
('ADM_002', 'Droupadi', 'Murmu', 'muramdroupadi@gamil.com', '1967-04-14', NULL, 'High Street', 640012),
('ADM_003', 'Manmohan ', 'Singh', 'singhmanmohan@gamil.com', '1970-04-08', NULL, 'Pumpwell Road', 575003);

-- --------------------------------------------------------

--
-- Table structure for table `admin_phone`
--

CREATE TABLE `admin_phone` (
  `Admin_id` varchar(10) NOT NULL,
  `Phone_no` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin_phone`
--

INSERT INTO `admin_phone` (`Admin_id`, `Phone_no`) VALUES
('ADM_001', 7555012345),
('ADM_001', 9900456456),
('ADM_002', 7555012345),
('ADM_002', 9900456456),
('ADM_003', 7555012345),
('ADM_003', 9900456456);

-- --------------------------------------------------------

--
-- Table structure for table `bill`
--

CREATE TABLE `bill` (
  `Bill_id` varchar(10) NOT NULL,
  `Total_cost` float(5,2) DEFAULT NULL,
  `Issued_date` date DEFAULT NULL,
  `Last_valid_date` date DEFAULT NULL,
  `Present_date` date DEFAULT NULL,
  `Validity` varchar(20) DEFAULT NULL,
  `Shopkeeper_id` varchar(10) DEFAULT NULL,
  `RFID` bigint(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill`
--

INSERT INTO `bill` (`Bill_id`, `Total_cost`, `Issued_date`, `Last_valid_date`, `Present_date`, `Validity`, `Shopkeeper_id`, `RFID`) VALUES
('B_001', 140.00, '2021-06-07', '2021-06-09', '2021-06-07', 'Valid', 'SHK_001', 3453484810),
('B_002', 170.00, '2021-02-14', '2021-02-17', '2021-02-16', 'Valid', 'SHK_001', 3453484810),
('B_003', 105.00, '2021-07-13', '2021-07-16', '2021-07-14', 'Valid', 'SHK_003', 6815974590),
('B_004', 135.00, '2021-05-24', '2021-05-27', '2021-05-28', 'Invalid', 'SHK_003', 6815974590),
('B_005', 170.00, '2021-10-10', '2021-10-13', '2021-10-10', 'Valid', 'SHK_004', 5483807477),
('B_006', 55.00, '2021-12-22', '2021-12-25', '2021-12-24', 'Valid', 'SHK_004', 5483807477),
('B_007', 70.00, '2021-11-09', '2021-11-12', '2021-11-10', 'Valid', 'SHK_001', 9187065308),
('B_008', 115.00, '2021-07-29', '2021-08-01', '2021-07-29', 'Valid', 'SHK_001', 9187065308),
('B_009', 170.00, '2021-01-06', '2021-01-09', '2021-01-09', 'Valid', 'SHK_005', 1700494946),
('B_010', 45.00, '2021-07-26', '2021-07-29', '2021-07-30', 'Invalid', 'SHK_005', 1700494946),
('B_011', 100.00, '2021-05-08', '2021-05-11', '2021-05-11', 'Valid', 'SHK_006', 4478160351),
('B_012', 35.00, '2021-07-23', '2021-07-26', '2021-07-23', 'Valid', 'SHK_006', 4478160351),
('B_013', 10.00, '2021-07-08', '2021-07-11', '2021-07-09', 'Valid', 'SHK_001', 6977990400),
('B_014', 95.00, '2021-08-16', '2021-08-19', '2021-08-16', 'Valid', 'SHK_001', 6977990400),
('B_015', 30.00, '2021-10-31', '2021-11-03', '2021-11-04', 'Invalid', 'SHK_005', 7575833003),
('B_016', 35.00, '2021-05-06', '2021-05-09', '2021-05-09', 'Valid', 'SHK_005', 7575833003),
('B_017', 65.00, '2021-11-29', '2021-12-02', '2021-11-30', 'Valid', 'SHK_002', 8727666988),
('B_018', 75.00, '2021-06-09', '2021-06-12', '2021-06-09', 'Valid', 'SHK_002', 8727666988),
('B_019', 30.00, '2021-05-02', '2021-05-05', '2021-05-02', 'Valid', 'SHK_006', 2192227997),
('B_020', 130.00, '2021-08-19', '2021-08-22', '2021-08-23', 'Invalid', 'SHK_006', 2192227997),
('B_021', 40.00, '2021-01-03', '2021-01-06', '2021-01-03', 'Valid', 'SHK_003', 8979106724),
('B_022', 40.00, '2021-06-25', '2021-06-28', '2021-06-28', 'Valid', 'SHK_003', 8979106724),
('B_023', 30.00, '2021-03-15', '2021-03-18', '2021-03-17', 'Valid', 'SHK_004', 6597759624),
('B_024', 35.00, '2021-05-14', '2021-05-17', '2021-05-14', 'Valid', 'SHK_004', 6597759624),
('B_025', 170.00, '2021-02-16', '2021-02-19', '2021-02-19', 'Valid', 'SHK_001', 6283738531),
('B_026', 170.00, '2021-09-21', '2021-09-24', '2021-09-22', 'Valid', 'SHK_001', 6283738531),
('B_027', 25.00, '2021-09-08', '2021-09-11', '2021-09-09', 'Valid', 'SHK_005', 8646892910),
('B_028', 40.00, '2021-03-11', '2021-03-14', '2021-03-13', 'Valid', 'SHK_005', 8646892910),
('B_029', 30.00, '2021-03-30', '2021-04-02', '2021-04-03', 'Invalid', 'SHK_002', 9579531991),
('B_030', 75.00, '2021-02-01', '2021-02-04', '2021-02-01', 'Valid', 'SHK_002', 9579531991),
('B_031', 55.00, '2021-12-12', '2021-12-15', '2021-12-12', 'Valid', 'SHK_003', 7243413566),
('B_032', 100.00, '2021-06-24', '2021-06-27', '2021-06-24', 'Valid', 'SHK_003', 7243413566),
('B_033', 40.00, '2021-03-19', '2021-03-22', '2021-03-19', 'Valid', 'SHK_006', 8565854116),
('B_034', 30.00, '2021-10-10', '2021-10-13', '2021-10-11', 'Valid', 'SHK_006', 8565854116),
('B_035', 35.00, '2021-08-28', '2021-08-31', '2021-08-28', 'Valid', 'SHK_001', 6107074114),
('B_036', 10.00, '2021-10-04', '2021-10-07', '2021-10-08', 'Invalid', 'SHK_001', 6107074114),
('B_037', 30.00, '2021-01-29', '2021-02-01', '2021-01-29', 'Valid', 'SHK_004', 3740546453),
('B_038', 140.00, '2021-05-17', '2021-05-20', '2021-05-17', 'Valid', 'SHK_004', 3740546453),
('B_039', 70.00, '2021-09-25', '2021-09-28', '2021-09-28', 'Valid', 'SHK_002', 1637382417),
('B_040', 75.00, '2021-12-10', '2021-12-13', '2021-12-10', 'Valid', 'SHK_002', 1637382417),
('B_041', 115.00, '2021-06-12', '2021-06-15', '2021-06-14', 'Valid', 'SHK_006', 8808967440),
('B_042', 160.00, '2021-07-12', '2021-07-15', '2021-07-12', 'Valid', 'SHK_006', 8808967440),
('B_043', 10.00, '2021-03-02', '2021-03-05', '2021-03-03', 'Valid', 'SHK_002', 2624574553),
('B_044', 30.00, '2021-02-24', '2021-02-27', '2021-02-28', 'Invalid', 'SHK_002', 2624574553),
('B_045', 25.00, '2021-02-07', '2021-02-10', '2021-02-09', 'Valid', 'SHK_005', 8945871085),
('B_046', 30.00, '2021-09-20', '2021-09-23', '2021-09-23', 'Valid', 'SHK_005', 8945871085),
('B_047', 75.00, '2021-01-28', '2021-01-31', '2021-01-28', 'Valid', 'SHK_004', 4693726418),
('B_048', 25.00, '2021-06-14', '2021-06-17', '2021-06-17', 'Valid', 'SHK_004', 4693726418),
('B_049', 90.00, '2022-11-26', '2022-11-29', '2022-11-29', 'Valid', 'SHK_001', 1637382417),
('B_050', 10.00, '2022-11-26', '2022-11-29', '2022-11-30', 'Invalid', 'SHK_001', 1637382417);

--
-- Triggers `bill`
--
DELIMITER $$
CREATE TRIGGER `buying_date` BEFORE INSERT ON `bill` FOR EACH ROW BEGIN
    IF new.Present_date > new.Last_valid_date THEN SET new.Validity = 'Invalid';
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `bill_product`
--

CREATE TABLE `bill_product` (
  `Bill_id` varchar(10) NOT NULL,
  `P_Name` varchar(20) NOT NULL,
  `Quantity` float(5,2) DEFAULT NULL,
  `Total_cost_per_product` float(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bill_product`
--

INSERT INTO `bill_product` (`Bill_id`, `P_Name`, `Quantity`, `Total_cost_per_product`) VALUES
('B_001', 'Kerosene', 1.00, 10.00),
('B_001', 'Oil', 1.00, 40.00),
('B_001', 'Rice', 1.00, 30.00),
('B_001', 'Sugar', 1.00, 25.00),
('B_001', 'Wheat', 1.00, 35.00),
('B_002', 'Daal', 1.00, 30.00),
('B_002', 'Kerosene', 1.00, 10.00),
('B_002', 'Rice', 1.00, 30.00),
('B_002', 'Wheat', 1.00, 35.00),
('B_003', 'Oil', 1.00, 40.00),
('B_003', 'Rice', 1.00, 30.00),
('B_003', 'Wheat', 1.00, 35.00),
('B_004', 'Daal', 1.00, 30.00),
('B_004', 'Kerosene', 1.00, 10.00),
('B_004', 'Oil', 1.00, 40.00),
('B_004', 'Rice', 1.00, 30.00),
('B_004', 'Sugar', 1.00, 25.00),
('B_005', 'Daal', 1.00, 30.00),
('B_005', 'Kerosene', 1.00, 10.00),
('B_005', 'Oil', 1.00, 40.00),
('B_005', 'Rice', 1.00, 30.00),
('B_005', 'Sugar', 1.00, 25.00),
('B_005', 'Wheat', 1.00, 35.00),
('B_006', 'Daal', 1.00, 30.00),
('B_006', 'Kerosene', 1.00, 10.00),
('B_006', 'Sugar', 1.00, 25.00),
('B_007', 'Oil', 1.00, 40.00),
('B_007', 'Rice', 1.00, 30.00),
('B_008', 'Daal', 1.00, 30.00),
('B_008', 'Kerosene', 1.00, 10.00),
('B_008', 'Oil', 1.00, 40.00),
('B_008', 'Wheat', 1.00, 35.00),
('B_009', 'Daal', 1.00, 30.00),
('B_009', 'Kerosene', 1.00, 10.00),
('B_009', 'Oil', 1.00, 40.00),
('B_009', 'Rice', 1.00, 30.00),
('B_009', 'Sugar', 1.00, 25.00),
('B_009', 'Wheat', 1.00, 35.00),
('B_010', 'Kerosene', 1.00, 10.00),
('B_010', 'Wheat', 1.00, 35.00),
('B_011', 'Daal', 1.00, 30.00),
('B_011', 'Oil', 1.00, 40.00),
('B_011', 'Rice', 1.00, 30.00),
('B_012', 'Wheat', 1.00, 35.00),
('B_013', 'Kerosene', 1.00, 10.00),
('B_014', 'Daal', 1.00, 30.00),
('B_014', 'Oil', 1.00, 40.00),
('B_014', 'Sugar', 1.00, 25.00),
('B_015', 'Rice', 1.00, 30.00),
('B_016', 'Wheat', 1.00, 35.00),
('B_017', 'Daal', 1.00, 30.00),
('B_017', 'Kerosene', 1.00, 10.00),
('B_017', 'Sugar', 1.00, 25.00),
('B_018', 'Kerosene', 1.00, 10.00),
('B_018', 'Rice', 1.00, 30.00),
('B_018', 'Wheat', 1.00, 35.00),
('B_019', 'Daal', 1.00, 30.00),
('B_020', 'Oil', 1.00, 40.00),
('B_020', 'Rice', 1.00, 30.00),
('B_020', 'Sugar', 1.00, 25.00),
('B_020', 'Wheat', 1.00, 35.00),
('B_021', 'Daal', 1.00, 30.00),
('B_021', 'Kerosene', 1.00, 10.00),
('B_022', 'Oil', 1.00, 40.00),
('B_023', 'Rice', 1.00, 30.00),
('B_024', 'Wheat', 1.00, 35.00),
('B_025', 'Daal', 1.00, 30.00),
('B_025', 'Kerosene', 1.00, 10.00),
('B_025', 'Oil', 1.00, 40.00),
('B_025', 'Rice', 1.00, 30.00),
('B_025', 'Sugar', 1.00, 25.00),
('B_025', 'Wheat', 1.00, 35.00),
('B_026', 'Daal', 1.00, 30.00),
('B_026', 'Kerosene', 1.00, 10.00),
('B_026', 'Oil', 1.00, 40.00),
('B_026', 'Rice', 1.00, 30.00),
('B_026', 'Sugar', 1.00, 25.00),
('B_026', 'Wheat', 1.00, 35.00),
('B_027', 'Sugar', 1.00, 25.00),
('B_028', 'Oil', 1.00, 40.00),
('B_029', 'Rice', 1.00, 30.00),
('B_030', 'Daal', 1.00, 30.00),
('B_030', 'Kerosene', 1.00, 10.00),
('B_030', 'Wheat', 1.00, 35.00),
('B_031', 'Rice', 1.00, 30.00),
('B_031', 'Sugar', 1.00, 25.00),
('B_032', 'Daal', 1.00, 30.00),
('B_032', 'Kerosene', 1.00, 10.00),
('B_032', 'Sugar', 1.00, 25.00),
('B_032', 'Wheat', 1.00, 35.00),
('B_033', 'Oil', 1.00, 40.00),
('B_034', 'Rice', 1.00, 30.00),
('B_035', 'Wheat', 1.00, 35.00),
('B_036', 'Kerosene', 1.00, 10.00),
('B_037', 'Daal', 1.00, 30.00),
('B_038', 'Kerosene', 1.00, 10.00),
('B_038', 'Oil', 1.00, 40.00),
('B_038', 'Rice', 1.00, 30.00),
('B_038', 'Sugar', 1.00, 25.00),
('B_038', 'Wheat', 1.00, 35.00),
('B_039', 'Oil', 1.00, 40.00),
('B_039', 'Rice', 1.00, 30.00),
('B_040', 'Daal', 1.00, 30.00),
('B_040', 'Kerosene', 1.00, 10.00),
('B_040', 'Wheat', 1.00, 35.00),
('B_041', 'Kerosene', 1.00, 10.00),
('B_041', 'Oil', 1.00, 40.00),
('B_041', 'Rice', 1.00, 30.00),
('B_041', 'Wheat', 1.00, 35.00),
('B_042', 'Daal', 1.00, 30.00),
('B_042', 'Oil', 1.00, 40.00),
('B_042', 'Rice', 1.00, 30.00),
('B_042', 'Sugar', 1.00, 25.00),
('B_042', 'Wheat', 1.00, 35.00),
('B_043', 'Kerosene', 1.00, 10.00),
('B_044', 'Daal', 1.00, 30.00),
('B_045', 'Sugar', 1.00, 25.00),
('B_046', 'Rice', 1.00, 30.00),
('B_047', 'Daal', 1.00, 30.00),
('B_047', 'Kerosene', 1.00, 10.00),
('B_047', 'Wheat', 1.00, 35.00),
('B_048', 'Sugar', 1.00, 25.00),
('B_049', 'Kerosene', 1.00, 10.00),
('B_049', 'Oil', 2.00, 80.00);

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `RFID` bigint(20) NOT NULL,
  `C_Fname` varchar(20) DEFAULT NULL,
  `C_Lname` varchar(20) DEFAULT NULL,
  `C_Email_id` varchar(50) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Street_no` varchar(40) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `PIN` int(6) DEFAULT NULL,
  `Admin_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`RFID`, `C_Fname`, `C_Lname`, `C_Email_id`, `DOB`, `Gender`, `Street_no`, `City`, `PIN`, `Admin_id`) VALUES
(1637382417, 'Anshu', 'Bhardwaj', 'bhardwajanshu@gmail.com', '1978-04-14', 'F', 'KSR Road', 'Hubbali', 575001, 'ADM_003'),
(1700494946, 'Rahul', 'Khanna', 'khannarahul@gmail.com', '1997-12-14', 'M', '1 Pink Street', 'Belagavi', 600067, 'ADM_001'),
(2192227997, 'Samanta', 'Prabhu', 'prabhusamanta@gmail.com', '1968-04-14', 'F', '8 Clone Colony', 'Belagavi', 600042, 'ADM_001'),
(2624574553, 'Srihari', 'Udupa', 'udupasrihari@gmail.com', '1980-04-14', 'M', 'Suranjan Das Road', 'Hubbali', 560015, 'ADM_001'),
(3453484810, ' Ajit', 'Ullal', 'ullalajit@gmail.com', '1971-01-01', 'M', '10 Janpath', 'Bengaluru', 560001, 'ADM_001'),
(3740546453, 'Arun', 'Kumar', 'kumararun@gmail.com', '1977-04-14', 'M', 'Mint Street', 'Bengaluru', 600046, 'ADM_003'),
(4478160351, 'Nirmala', 'Seturaman', 'seturamannirmala@gmail.com', '1998-12-15', 'F', '3 Blue Avenue', 'Mangaluru', 560105, 'ADM_002'),
(4693726418, 'Shradha', 'Nayar', 'nayarshradha@gmail.com', '1982-04-08', 'F', 'M G Road Bangalore', 'Belagavi', 560006, 'ADM_003'),
(5483807477, 'Sai Deepak', 'Reddy', 'reddysai@gmail.com', '1996-12-12', 'F', '14 Kailsh Marg', 'Belagavi', 600001, 'ADM_002'),
(6107074114, 'Margaret', 'Alva', 'alvamargaret@gmail.com', '1976-04-14', 'F', 'New BEL Road', 'Hubbali', 560008, 'ADM_003'),
(6283738531, 'Rashkit ', 'Shetty', 'shettyrashkit@gmail.com', '1971-04-14', 'M', 'JC Road', 'Belagavi', 560009, 'ADM_003'),
(6597759624, 'Rahul ', 'Gandhi', 'gandhirahul@gmail.com', '1970-04-08', 'M', 'Mirza road', 'Mangaluru', 475001, 'ADM_002'),
(6815974590, 'Muhammed ', 'Ali', 'alimihammed@gmail.com', '2000-10-09', 'M', '10 Downing', 'Mangaluru', 560003, 'ADM_002'),
(6977990400, 'Smriti', 'Irani', 'iranismriti@gmail.com', '1999-12-16', 'F', '4 Banyan Avenie', 'Mangaluru', 575014, 'ADM_003'),
(7243413566, 'Subbu', 'Saravana', 'saravanasubbu@gmail.com', '1974-04-14', 'F', 'American Street', 'Belagavi', 600043, 'ADM_003'),
(7575833003, 'Ajit', 'Sethi', 'sethiajit@gmail.com', '1966-04-14', 'M', '6 Poes Garden', 'Hubbali', 575001, 'ADM_002'),
(8565854116, 'Sheela', 'Dixit', 'dixitsheela@gmail.com', '1975-04-08', 'F', 'Kasturba Road', 'Mangaluru', 560048, 'ADM_001'),
(8646892910, 'Rishi', 'Sunak', 'sunakrishi@gmail.com', '1972-04-14', 'M', 'Anna Sali', 'Bengaluru', 600034, 'ADM_002'),
(8727666988, 'Arjun', 'Allu', 'alluarjun@gmail.com', '1967-04-08', 'M', '7 Dhamaka street', 'Bengaluru', 575020, 'ADM_003'),
(8808967440, 'Suma', 'Sampat', 'sampatsuma@gmail.com', '1979-04-08', 'F', 'Old Airport Road Bangalore', 'Mangaluru', 560012, 'ADM_001'),
(8945871085, 'Satish', 'Kotian', 'kotiansatish@gmail.com', '1981-04-14', 'M', 'T Nagar', 'Mangaluru', 600044, 'ADM_002'),
(8979106724, 'Kiran ', 'Bedi', 'bedikiran@gmail.com', '1969-04-14', 'F', '56 Brigade Road', 'Bengaluru', 560003, 'ADM_003'),
(9187065308, 'Rudra', 'Agarwal', 'agarwalrudra@gmail.com', '1996-12-13', 'F', '5 Lohia Garden', 'Bengaluru', 600042, 'ADM_001'),
(9579531991, 'Vedavalli', 'Srinath', 'srinathvedavalli@gmail.com', '1973-04-14', 'F', 'Church Street Bangalore', 'Hubbali', 560054, 'ADM_001');

-- --------------------------------------------------------

--
-- Table structure for table `customer_email`
--

CREATE TABLE `customer_email` (
  `Fname` varchar(10) DEFAULT NULL,
  `Lname` varchar(10) DEFAULT NULL,
  `Email_id` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_email`
--

INSERT INTO `customer_email` (`Fname`, `Lname`, `Email_id`) VALUES
('Anshu', 'Bhardwaj', 'bhardwajanshu@gmail.com'),
('Rahul', 'Khanna', 'khannarahul@gmail.com'),
('Samanta', 'Prabhu', 'prabhusamanta@gmail.com'),
('Srihari', 'Udupa', 'udupasrihari@gmail.com'),
(' Ajit', 'Ullal', 'ullalajit@gmail.com'),
('Arun', 'Kumar', 'kumararun@gmail.com'),
('Nirmala', 'Seturaman', 'seturamannirmala@gmail.com'),
('Shradha', 'Nayar', 'nayarshradha@gmail.com'),
('Sai Deepak', 'Reddy', 'reddysai@gmail.com'),
('Margaret', 'Alva', 'alvamargaret@gmail.com'),
('Rashkit ', 'Shetty', 'shettyrashkit@gmail.com'),
('Rahul ', 'Gandhi', 'gandhirahul@gmail.com'),
('Muhammed ', 'Ali', 'alimihammed@gmail.com'),
('Smriti', 'Irani', 'iranismriti@gmail.com'),
('Subbu', 'Saravana', 'saravanasubbu@gmail.com'),
('Ajit', 'Sethi', 'sethiajit@gmail.com'),
('Sheela', 'Dixit', 'dixitsheela@gmail.com'),
('Rishi', 'Sunak', 'sunakrishi@gmail.com'),
('Arjun', 'Allu', 'alluarjun@gmail.com'),
('Suma', 'Sampat', 'sampatsuma@gmail.com'),
('Satish', 'Kotian', 'kotiansatish@gmail.com'),
('Kiran ', 'Bedi', 'bedikiran@gmail.com'),
('Rudra', 'Agarwal', 'agarwalrudra@gmail.com'),
('Vedavalli', 'Srinath', 'srinathvedavalli@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `customer_phone`
--

CREATE TABLE `customer_phone` (
  `RFID` bigint(20) NOT NULL,
  `Phone_no` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer_phone`
--

INSERT INTO `customer_phone` (`RFID`, `Phone_no`) VALUES
(1637382417, 9845012345),
(1637382417, 9900123456),
(1700494946, 9845012345),
(1700494946, 9900123456),
(2192227997, 9845012345),
(2192227997, 9900123456),
(2624574553, 9845012345),
(2624574553, 9900123456),
(3453484810, 9845012345),
(3453484810, 9900123456),
(3740546453, 9845012345),
(3740546453, 9900123456),
(4478160351, 9845012345),
(4478160351, 9900123456),
(4693726418, 9845012345),
(4693726418, 9900123456),
(5483807477, 9845012345),
(5483807477, 9900123456),
(6107074114, 9845012345),
(6107074114, 9900123456),
(6283738531, 9845012345),
(6283738531, 9900123456),
(6597759624, 9845012345),
(6597759624, 9900123456),
(6815974590, 9845012345),
(6815974590, 9900123456),
(6977990400, 9845012345),
(6977990400, 9900123456),
(7243413566, 9845012345),
(7243413566, 9900123456),
(7575833003, 9845012345),
(7575833003, 9900123456),
(8565854116, 9845012345),
(8565854116, 9900123456),
(8646892910, 9845012345),
(8646892910, 9900123456),
(8727666988, 9845012345),
(8727666988, 9900123456),
(8808967440, 9845012345),
(8808967440, 9900123456),
(8945871085, 9845012345),
(8945871085, 9900123456),
(8979106724, 9845012345),
(8979106724, 9900123456),
(9187065308, 9845012345),
(9187065308, 9900123456),
(9579531991, 9845012345),
(9579531991, 9900123456);

-- --------------------------------------------------------

--
-- Table structure for table `dependent`
--

CREATE TABLE `dependent` (
  `RFID` bigint(10) DEFAULT NULL,
  `D_Name` varchar(20) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Gender` varchar(10) DEFAULT NULL,
  `Age` int(3) DEFAULT NULL,
  `Relation` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dependent`
--

INSERT INTO `dependent` (`RFID`, `D_Name`, `DOB`, `Gender`, `Age`, `Relation`) VALUES
(3453484810, 'Aashvi', '1980-01-01', 'F', NULL, 'Wife'),
(3453484810, 'Arjun', '2000-01-01', 'M', NULL, 'Son'),
(6815974590, 'Lakshmi ', '1981-02-02', 'F', NULL, 'Wife'),
(6815974590, 'Aum', '2000-07-02', 'M', NULL, 'Son'),
(5483807477, 'Meera', '2001-01-03', 'F', NULL, 'Daughter'),
(5483807477, 'Ishan', '1982-03-03', 'M', NULL, 'Husband'),
(9187065308, 'Saanvi', '2001-07-04', 'F', NULL, 'Daughter'),
(9187065308, 'Krish', '1983-04-04', 'M', NULL, 'Husband'),
(1700494946, 'Sarika', '1984-05-05', 'F', NULL, 'Wife'),
(1700494946, 'Moksh', '2003-07-08', 'M', NULL, 'Son'),
(4478160351, 'Shyla', '2006-01-13', 'F', NULL, 'Daughter'),
(4478160351, 'Rishi', '1985-06-06', 'M', NULL, 'Husband'),
(6977990400, 'Sita', '2002-01-05', 'F', NULL, 'Daughter'),
(6977990400, 'Veer', '1986-07-07', 'M', NULL, 'Husband'),
(7575833003, 'Uma', '1987-08-08', 'F', NULL, 'Wife'),
(7575833003, 'Laksh', '2006-01-13', 'M', NULL, 'Son'),
(8727666988, 'Aarya', '1988-09-09', 'F', NULL, 'Wife'),
(8727666988, 'Moksh', '2011-07-24', 'M', NULL, 'Son'),
(2192227997, 'Divya', '2011-01-23', 'F', NULL, 'Daughter'),
(2192227997, 'Sajan', '1989-10-10', 'M', NULL, 'Husband'),
(8979106724, 'Jaya', '2010-01-21', 'F', NULL, 'Daughter'),
(8979106724, 'Samay', '1990-11-11', 'M', NULL, 'Husband'),
(6597759624, 'Lavanya', '1991-12-12', 'F', NULL, 'Wife'),
(6597759624, 'Siddh', '2009-07-20', 'M', NULL, 'Son'),
(6283738531, 'Kimaya', '1985-01-11', 'F', NULL, 'Wife'),
(6283738531, 'Ari', '2009-01-19', 'M', NULL, 'Son'),
(8646892910, 'Saumya', '1985-07-12', 'F', NULL, 'Wife'),
(8646892910, 'Dev', '2008-07-18', 'M', NULL, 'Son'),
(9579531991, 'Satya', '2007-01-15', 'F', NULL, 'Daughter'),
(9579531991, 'Jaiden', '1986-01-13', 'M', NULL, 'Husband'),
(7243413566, 'Zoya', '2008-01-17', 'F', NULL, 'Daughter'),
(7243413566, 'Jay', '1986-07-14', 'M', NULL, 'Husband'),
(8565854116, 'Aadhavi', '2007-01-15', 'F', NULL, 'Daughter'),
(8565854116, 'Kalpen', '1987-01-15', 'M', NULL, 'Husband'),
(6107074114, 'Aanya', '2003-01-07', 'F', NULL, 'Daughter'),
(6107074114, 'Sai', '1987-07-16', 'M', NULL, 'Husband'),
(3740546453, 'Aarya', '1988-01-17', 'F', NULL, 'Wife'),
(3740546453, 'Zayn', '2003-07-08', 'M', NULL, 'Son'),
(1637382417, 'Aashvi', '2004-01-09', 'F', NULL, 'Daughter'),
(1637382417, 'Aaditya', '1988-07-18', 'M', NULL, 'Husband'),
(8808967440, 'Alani', '2008-07-18', 'F', NULL, 'Daughter'),
(8808967440, 'Aarav', '1989-01-19', 'M', NULL, 'Husband'),
(2624574553, 'Amara', '1989-07-20', 'F', NULL, 'Wife'),
(2624574553, 'Ajay', '2007-01-15', 'M', NULL, 'Son'),
(8945871085, 'Amulya', '1990-01-21', 'F', NULL, 'Wife'),
(8945871085, 'Akash', '2008-07-18', 'M', NULL, 'Son'),
(4693726418, 'Aniya', '2005-07-12', 'F', NULL, 'Daughter'),
(4693726418, 'Akhil', '1991-01-23', 'M', NULL, 'Husband');

--
-- Triggers `dependent`
--
DELIMITER $$
CREATE TRIGGER `dependent_age` BEFORE INSERT ON `dependent` FOR EACH ROW BEGIN
    DECLARE error_msg VARCHAR(300);
    SET error_msg = ("Age of the dependent should be 10 or more");
    IF new.Age < 10 THEN 
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = error_msg;
    END IF;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `P_Name` varchar(20) NOT NULL,
  `Cost_per_unit` float(5,2) DEFAULT NULL,
  `Unit` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`P_Name`, `Cost_per_unit`, `Unit`) VALUES
('Daal', 30.00, 'KG'),
('Kerosene', 10.00, 'L'),
('Oil', 40.00, 'L'),
('Rice', 30.00, 'KG'),
('Sugar', 25.00, 'KG'),
('Wheat', 35.00, 'KG');

-- --------------------------------------------------------

--
-- Table structure for table `product_customer`
--

CREATE TABLE `product_customer` (
  `P_Name` varchar(10) NOT NULL,
  `RFID` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `product_customer`
--

INSERT INTO `product_customer` (`P_Name`, `RFID`) VALUES
('Daal', 1637382417),
('Daal', 1700494946),
('Daal', 2192227997),
('Daal', 2624574553),
('Daal', 3453484810),
('Daal', 3740546453),
('Daal', 4478160351),
('Daal', 4693726418),
('Daal', 5483807477),
('Daal', 6283738531),
('Daal', 6815974590),
('Daal', 6977990400),
('Daal', 7243413566),
('Daal', 8727666988),
('Daal', 8808967440),
('Daal', 8979106724),
('Daal', 9187065308),
('Daal', 9579531991),
('Kerosene', 1637382417),
('Kerosene', 1700494946),
('Kerosene', 2624574553),
('Kerosene', 3453484810),
('Kerosene', 3740546453),
('Kerosene', 4693726418),
('Kerosene', 5483807477),
('Kerosene', 6107074114),
('Kerosene', 6283738531),
('Kerosene', 6815974590),
('Kerosene', 6977990400),
('Kerosene', 7243413566),
('Kerosene', 8727666988),
('Kerosene', 8808967440),
('Kerosene', 8979106724),
('Kerosene', 9187065308),
('Kerosene', 9579531991),
('Oil', 1637382417),
('Oil', 1700494946),
('Oil', 2192227997),
('Oil', 3453484810),
('Oil', 3740546453),
('Oil', 4478160351),
('Oil', 5483807477),
('Oil', 6283738531),
('Oil', 6815974590),
('Oil', 6977990400),
('Oil', 8565854116),
('Oil', 8646892910),
('Oil', 8808967440),
('Oil', 8979106724),
('Oil', 9187065308),
('Rice', 1637382417),
('Rice', 1700494946),
('Rice', 2192227997),
('Rice', 3453484810),
('Rice', 3740546453),
('Rice', 4478160351),
('Rice', 5483807477),
('Rice', 6283738531),
('Rice', 6597759624),
('Rice', 6815974590),
('Rice', 7243413566),
('Rice', 7575833003),
('Rice', 8565854116),
('Rice', 8727666988),
('Rice', 8808967440),
('Rice', 8945871085),
('Rice', 9187065308),
('Rice', 9579531991),
('Sugar', 1700494946),
('Sugar', 2192227997),
('Sugar', 3453484810),
('Sugar', 3740546453),
('Sugar', 4693726418),
('Sugar', 5483807477),
('Sugar', 6283738531),
('Sugar', 6815974590),
('Sugar', 6977990400),
('Sugar', 7243413566),
('Sugar', 8646892910),
('Sugar', 8727666988),
('Sugar', 8808967440),
('Sugar', 8945871085),
('Wheat', 1637382417),
('Wheat', 1700494946),
('Wheat', 2192227997),
('Wheat', 3453484810),
('Wheat', 3740546453),
('Wheat', 4478160351),
('Wheat', 4693726418),
('Wheat', 5483807477),
('Wheat', 6107074114),
('Wheat', 6283738531),
('Wheat', 6597759624),
('Wheat', 6815974590),
('Wheat', 7243413566),
('Wheat', 7575833003),
('Wheat', 8727666988),
('Wheat', 8808967440),
('Wheat', 9187065308),
('Wheat', 9579531991);

-- --------------------------------------------------------

--
-- Table structure for table `sale`
--

CREATE TABLE `sale` (
  `P_Name` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sale`
--

INSERT INTO `sale` (`P_Name`) VALUES
('Kerosene'),
('Oil');

-- --------------------------------------------------------

--
-- Table structure for table `shopkeeper`
--

CREATE TABLE `shopkeeper` (
  `Shopkeeper_id` varchar(10) NOT NULL,
  `S_Fname` varchar(20) DEFAULT NULL,
  `S_Lname` varchar(20) DEFAULT NULL,
  `Store_name` varchar(20) DEFAULT NULL,
  `Street_no` varchar(40) DEFAULT NULL,
  `City` varchar(20) DEFAULT NULL,
  `PIN` int(6) DEFAULT NULL,
  `Admin_id` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shopkeeper`
--

INSERT INTO `shopkeeper` (`Shopkeeper_id`, `S_Fname`, `S_Lname`, `Store_name`, `Street_no`, `City`, `PIN`, `Admin_id`) VALUES
('SHK_001', 'Manisha', 'Solanki', 'Lakshmi FPS', 'M G Road', 'Bengaluru', 575030, 'ADM_001'),
('SHK_002', 'Bharti', 'Devgan', 'Mahaveer FPS', 'NAL Wind Tunnel Road', 'Mangaluru', 560059, 'ADM_003'),
('SHK_003', 'Roopa', 'Ram', 'Goudra FPS', 'Bunder Road', 'Belagavi', 575023, 'ADM_002'),
('SHK_004', 'Pallavi', 'Ram', 'Mirje FPS', 'Lavelle Road', 'Kalaburgi', 560044, 'ADM_003'),
('SHK_005', 'Ravi', 'Naik', 'Padmavati FPS', 'Thiru V ka Salai', 'Udupi', 600045, 'ADM_001'),
('SHK_006', 'Virat', 'Murthy', 'Munnoli FPS', 'Bejai New Road', 'KGF', 575011, 'ADM_002');

-- --------------------------------------------------------

--
-- Table structure for table `shopkeeper_phone`
--

CREATE TABLE `shopkeeper_phone` (
  `Shopkeeper_id` varchar(10) NOT NULL,
  `Phone_no` bigint(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shopkeeper_phone`
--

INSERT INTO `shopkeeper_phone` (`Shopkeeper_id`, `Phone_no`) VALUES
('SHK_001', 6347012345),
('SHK_001', 7346123456),
('SHK_002', 6347012345),
('SHK_002', 7346123456),
('SHK_003', 6347012345),
('SHK_003', 7346123456),
('SHK_004', 6347012345),
('SHK_004', 7346123456),
('SHK_005', 6347012345),
('SHK_005', 7346123456),
('SHK_006', 6347012345),
('SHK_006', 7346123456);

-- --------------------------------------------------------

--
-- Table structure for table `shopkeeper_product`
--

CREATE TABLE `shopkeeper_product` (
  `Shopkeeper_id` varchar(10) NOT NULL,
  `P_Name` varchar(20) NOT NULL,
  `Initial_Quantity` float(5,2) DEFAULT NULL,
  `Present_Quantity` float(5,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shopkeeper_product`
--

INSERT INTO `shopkeeper_product` (`Shopkeeper_id`, `P_Name`, `Initial_Quantity`, `Present_Quantity`) VALUES
('SHK_001', 'Kerosene', 140.00, 138.00),
('SHK_001', 'Oil', 90.00, 86.00),
('SHK_001', 'Rice', 100.00, 100.00),
('SHK_001', 'Sugar', 130.00, 130.00),
('SHK_001', 'Wheat', 120.00, 120.00),
('SHK_002', 'Daal', 130.00, 130.00),
('SHK_002', 'Kerosene', 140.00, 140.00),
('SHK_002', 'Oil', 90.00, 90.00),
('SHK_002', 'Rice', 100.00, 100.00),
('SHK_002', 'Wheat', 120.00, 120.00),
('SHK_003', 'Daal', 130.00, 130.00),
('SHK_003', 'Kerosene', 140.00, 140.00),
('SHK_003', 'Oil', 100.00, 100.00),
('SHK_003', 'Rice', 100.00, 100.00),
('SHK_003', 'Sugar', 90.00, 90.00),
('SHK_003', 'Wheat', 120.00, 120.00),
('SHK_004', 'Daal', 90.00, 90.00),
('SHK_004', 'Kerosene', 130.00, 130.00),
('SHK_004', 'Rice', 120.00, 120.00),
('SHK_004', 'Sugar', 100.00, 100.00),
('SHK_004', 'Wheat', 140.00, 140.00),
('SHK_005', 'Daal', 90.00, 90.00),
('SHK_005', 'Kerosene', 130.00, 130.00),
('SHK_005', 'Oil', 120.00, 120.00),
('SHK_005', 'Rice', 120.00, 120.00),
('SHK_005', 'Sugar', 100.00, 100.00),
('SHK_005', 'Wheat', 140.00, 140.00),
('SHK_006', 'Daal', 100.00, 100.00),
('SHK_006', 'Kerosene', 90.00, 90.00),
('SHK_006', 'Oil', 120.00, 120.00),
('SHK_006', 'Rice', 140.00, 140.00),
('SHK_006', 'Wheat', 130.00, 130.00);

-- --------------------------------------------------------

--
-- Table structure for table `valid_bills`
--

CREATE TABLE `valid_bills` (
  `Bill_id` varchar(10) DEFAULT NULL,
  `Total_cost` int(5) DEFAULT NULL,
  `Issued_date` date DEFAULT NULL,
  `Last_valid_date` date DEFAULT NULL,
  `Present_date` date DEFAULT NULL,
  `Validity` varchar(20) DEFAULT NULL,
  `Shopkeeper_id` varchar(10) DEFAULT NULL,
  `RFID` bigint(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `valid_bills`
--

INSERT INTO `valid_bills` (`Bill_id`, `Total_cost`, `Issued_date`, `Last_valid_date`, `Present_date`, `Validity`, `Shopkeeper_id`, `RFID`) VALUES
('B_001', 140, '2021-06-07', '2021-06-09', '2021-06-07', 'Valid', 'SHK_001', 3453484810),
('B_002', 170, '2021-02-14', '2021-02-17', '2021-02-16', 'Valid', 'SHK_001', 3453484810),
('B_003', 105, '2021-07-13', '2021-07-16', '2021-07-14', 'Valid', 'SHK_003', 6815974590),
('B_005', 170, '2021-10-10', '2021-10-13', '2021-10-10', 'Valid', 'SHK_004', 5483807477),
('B_006', 55, '2021-12-22', '2021-12-25', '2021-12-24', 'Valid', 'SHK_004', 5483807477),
('B_007', 70, '2021-11-09', '2021-11-12', '2021-11-10', 'Valid', 'SHK_001', 9187065308),
('B_008', 115, '2021-07-29', '2021-08-01', '2021-07-29', 'Valid', 'SHK_001', 9187065308),
('B_009', 170, '2021-01-06', '2021-01-09', '2021-01-09', 'Valid', 'SHK_005', 1700494946),
('B_011', 100, '2021-05-08', '2021-05-11', '2021-05-11', 'Valid', 'SHK_006', 4478160351),
('B_012', 35, '2021-07-23', '2021-07-26', '2021-07-23', 'Valid', 'SHK_006', 4478160351),
('B_013', 10, '2021-07-08', '2021-07-11', '2021-07-09', 'Valid', 'SHK_001', 6977990400),
('B_014', 95, '2021-08-16', '2021-08-19', '2021-08-16', 'Valid', 'SHK_001', 6977990400),
('B_016', 35, '2021-05-06', '2021-05-09', '2021-05-09', 'Valid', 'SHK_005', 7575833003),
('B_017', 65, '2021-11-29', '2021-12-02', '2021-11-30', 'Valid', 'SHK_002', 8727666988),
('B_018', 75, '2021-06-09', '2021-06-12', '2021-06-09', 'Valid', 'SHK_002', 8727666988),
('B_019', 30, '2021-05-02', '2021-05-05', '2021-05-02', 'Valid', 'SHK_006', 2192227997),
('B_021', 40, '2021-01-03', '2021-01-06', '2021-01-03', 'Valid', 'SHK_003', 8979106724),
('B_022', 40, '2021-06-25', '2021-06-28', '2021-06-28', 'Valid', 'SHK_003', 8979106724),
('B_023', 30, '2021-03-15', '2021-03-18', '2021-03-17', 'Valid', 'SHK_004', 6597759624),
('B_024', 35, '2021-05-14', '2021-05-17', '2021-05-14', 'Valid', 'SHK_004', 6597759624),
('B_025', 170, '2021-02-16', '2021-02-19', '2021-02-19', 'Valid', 'SHK_001', 6283738531),
('B_026', 170, '2021-09-21', '2021-09-24', '2021-09-22', 'Valid', 'SHK_001', 6283738531),
('B_027', 25, '2021-09-08', '2021-09-11', '2021-09-09', 'Valid', 'SHK_005', 8646892910),
('B_028', 40, '2021-03-11', '2021-03-14', '2021-03-13', 'Valid', 'SHK_005', 8646892910),
('B_030', 75, '2021-02-01', '2021-02-04', '2021-02-01', 'Valid', 'SHK_002', 9579531991),
('B_031', 55, '2021-12-12', '2021-12-15', '2021-12-12', 'Valid', 'SHK_003', 7243413566),
('B_032', 100, '2021-06-24', '2021-06-27', '2021-06-24', 'Valid', 'SHK_003', 7243413566),
('B_033', 40, '2021-03-19', '2021-03-22', '2021-03-19', 'Valid', 'SHK_006', 8565854116),
('B_034', 30, '2021-10-10', '2021-10-13', '2021-10-11', 'Valid', 'SHK_006', 8565854116),
('B_035', 35, '2021-08-28', '2021-08-31', '2021-08-28', 'Valid', 'SHK_001', 6107074114),
('B_037', 30, '2021-01-29', '2021-02-01', '2021-01-29', 'Valid', 'SHK_004', 3740546453),
('B_038', 140, '2021-05-17', '2021-05-20', '2021-05-17', 'Valid', 'SHK_004', 3740546453),
('B_039', 70, '2021-09-25', '2021-09-28', '2021-09-28', 'Valid', 'SHK_002', 1637382417),
('B_040', 75, '2021-12-10', '2021-12-13', '2021-12-10', 'Valid', 'SHK_002', 1637382417),
('B_041', 115, '2021-06-12', '2021-06-15', '2021-06-14', 'Valid', 'SHK_006', 8808967440),
('B_042', 160, '2021-07-12', '2021-07-15', '2021-07-12', 'Valid', 'SHK_006', 8808967440),
('B_043', 10, '2021-03-02', '2021-03-05', '2021-03-03', 'Valid', 'SHK_002', 2624574553),
('B_045', 25, '2021-02-07', '2021-02-10', '2021-02-09', 'Valid', 'SHK_005', 8945871085),
('B_046', 30, '2021-09-20', '2021-09-23', '2021-09-23', 'Valid', 'SHK_005', 8945871085),
('B_047', 75, '2021-01-28', '2021-01-31', '2021-01-28', 'Valid', 'SHK_004', 4693726418),
('B_048', 25, '2021-06-14', '2021-06-17', '2021-06-17', 'Valid', 'SHK_004', 4693726418),
('B_049', 90, '2022-11-26', '2022-11-29', '2022-11-29', 'Valid', 'SHK_001', 1637382417);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`Admin_id`);

--
-- Indexes for table `admin_phone`
--
ALTER TABLE `admin_phone`
  ADD PRIMARY KEY (`Admin_id`,`Phone_no`);

--
-- Indexes for table `bill`
--
ALTER TABLE `bill`
  ADD PRIMARY KEY (`Bill_id`),
  ADD KEY `Shopkeeper_id` (`Shopkeeper_id`),
  ADD KEY `RFID` (`RFID`);

--
-- Indexes for table `bill_product`
--
ALTER TABLE `bill_product`
  ADD PRIMARY KEY (`Bill_id`,`P_Name`),
  ADD KEY `P_Name` (`P_Name`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`RFID`),
  ADD KEY `Admin_id` (`Admin_id`);

--
-- Indexes for table `customer_phone`
--
ALTER TABLE `customer_phone`
  ADD PRIMARY KEY (`RFID`,`Phone_no`);

--
-- Indexes for table `dependent`
--
ALTER TABLE `dependent`
  ADD KEY `RFID` (`RFID`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`P_Name`);

--
-- Indexes for table `product_customer`
--
ALTER TABLE `product_customer`
  ADD PRIMARY KEY (`P_Name`,`RFID`),
  ADD KEY `RFID` (`RFID`);

--
-- Indexes for table `shopkeeper`
--
ALTER TABLE `shopkeeper`
  ADD PRIMARY KEY (`Shopkeeper_id`),
  ADD KEY `Admin_id` (`Admin_id`);

--
-- Indexes for table `shopkeeper_phone`
--
ALTER TABLE `shopkeeper_phone`
  ADD PRIMARY KEY (`Shopkeeper_id`,`Phone_no`);

--
-- Indexes for table `shopkeeper_product`
--
ALTER TABLE `shopkeeper_product`
  ADD PRIMARY KEY (`Shopkeeper_id`,`P_Name`),
  ADD KEY `P_Name` (`P_Name`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `admin_phone`
--
ALTER TABLE `admin_phone`
  ADD CONSTRAINT `admin_phone_ibfk_1` FOREIGN KEY (`Admin_id`) REFERENCES `admin` (`Admin_id`) ON DELETE CASCADE;

--
-- Constraints for table `bill`
--
ALTER TABLE `bill`
  ADD CONSTRAINT `bill_ibfk_1` FOREIGN KEY (`Shopkeeper_id`) REFERENCES `shopkeeper` (`Shopkeeper_id`),
  ADD CONSTRAINT `bill_ibfk_2` FOREIGN KEY (`RFID`) REFERENCES `customer` (`RFID`) ON DELETE CASCADE;

--
-- Constraints for table `bill_product`
--
ALTER TABLE `bill_product`
  ADD CONSTRAINT `BILL_PRODUCT_ibfk_1` FOREIGN KEY (`Bill_id`) REFERENCES `bill` (`Bill_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `bill_product_ibfk_2` FOREIGN KEY (`P_Name`) REFERENCES `product` (`P_Name`) ON DELETE CASCADE;

--
-- Constraints for table `customer`
--
ALTER TABLE `customer`
  ADD CONSTRAINT `customer_ibfk_1` FOREIGN KEY (`Admin_id`) REFERENCES `admin` (`Admin_id`);

--
-- Constraints for table `customer_phone`
--
ALTER TABLE `customer_phone`
  ADD CONSTRAINT `customer_phone_ibfk_1` FOREIGN KEY (`RFID`) REFERENCES `customer` (`RFID`) ON DELETE CASCADE;

--
-- Constraints for table `dependent`
--
ALTER TABLE `dependent`
  ADD CONSTRAINT `dependent_ibfk_1` FOREIGN KEY (`RFID`) REFERENCES `customer` (`RFID`) ON DELETE CASCADE;

--
-- Constraints for table `product_customer`
--
ALTER TABLE `product_customer`
  ADD CONSTRAINT `product_customer_ibfk_1` FOREIGN KEY (`P_Name`) REFERENCES `product` (`P_Name`),
  ADD CONSTRAINT `product_customer_ibfk_2` FOREIGN KEY (`RFID`) REFERENCES `customer` (`RFID`) ON DELETE CASCADE;

--
-- Constraints for table `shopkeeper`
--
ALTER TABLE `shopkeeper`
  ADD CONSTRAINT `shopkeeper_ibfk_1` FOREIGN KEY (`Admin_id`) REFERENCES `admin` (`Admin_id`);

--
-- Constraints for table `shopkeeper_phone`
--
ALTER TABLE `shopkeeper_phone`
  ADD CONSTRAINT `shopkeeper_phone_ibfk_1` FOREIGN KEY (`Shopkeeper_id`) REFERENCES `shopkeeper` (`Shopkeeper_id`) ON DELETE CASCADE;

--
-- Constraints for table `shopkeeper_product`
--
ALTER TABLE `shopkeeper_product`
  ADD CONSTRAINT `shopkeeper_product_ibfk_1` FOREIGN KEY (`Shopkeeper_id`) REFERENCES `shopkeeper` (`Shopkeeper_id`),
  ADD CONSTRAINT `shopkeeper_product_ibfk_2` FOREIGN KEY (`P_Name`) REFERENCES `product` (`P_Name`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
