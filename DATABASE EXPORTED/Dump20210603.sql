-- MySQL dump 10.13  Distrib 8.0.21, for Win64 (x86_64)
--
-- Host: localhost    Database: aadhaar
-- ------------------------------------------------------
-- Server version	8.0.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `aadhar_card`
--

DROP TABLE IF EXISTS `aadhar_card`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `aadhar_card` (
  `uid` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `address` varchar(150) NOT NULL,
  `gender` varchar(40) NOT NULL,
  `email` varchar(50) NOT NULL,
  `phno` bigint NOT NULL,
  `biometric_data` varchar(30) NOT NULL,
  `poi_no` bigint DEFAULT NULL,
  `centre_id` bigint DEFAULT NULL,
  PRIMARY KEY (`uid`),
  KEY `poi_no` (`poi_no`),
  KEY `centre_id` (`centre_id`),
  CONSTRAINT `aadhar_card_ibfk_1` FOREIGN KEY (`poi_no`) REFERENCES `citizen` (`poi_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `aadhar_card_ibfk_2` FOREIGN KEY (`centre_id`) REFERENCES `enrollment_centre` (`centre_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aadhar_card`
--

LOCK TABLES `aadhar_card` WRITE;
/*!40000 ALTER TABLE `aadhar_card` DISABLE KEYS */;
INSERT INTO `aadhar_card` VALUES (100000000001,'RAHUL KUMAR','1999-09-12','Kengeri,Bengaluru-560060\n','Male','rahul@gmail.com',1234567890,'Successful',1000000001,1001),(100000000002,'VIVEK ','1999-09-12','Powai,Mumbai-400076\n','Male','vivek@gmail.com',1234567891,'Successful',1000000002,1002),(100000000003,'SUMIT PRAKASH','1999-09-12','Pune,Maharashtra-411047\n','Male','sumit@gmail.com',1234567892,'Successful',1000000003,1003);
/*!40000 ALTER TABLE `aadhar_card` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_insert` BEFORE INSERT ON `aadhar_card` FOR EACH ROW set new.name=upper(new.name) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_update` BEFORE UPDATE ON `aadhar_card` FOR EACH ROW set new.name=upper(new.name) */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `citizen`
--

DROP TABLE IF EXISTS `citizen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citizen` (
  `poi_no` bigint NOT NULL,
  `name` varchar(50) NOT NULL,
  `address` varchar(150) NOT NULL,
  PRIMARY KEY (`poi_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citizen`
--

LOCK TABLES `citizen` WRITE;
/*!40000 ALTER TABLE `citizen` DISABLE KEYS */;
INSERT INTO `citizen` VALUES (1000000001,'Rahul kumar','Kengeri,Bengaluru-560060\n'),(1000000002,'Vivek','Powai,Mumbai-400076\n\n'),(1000000003,'Sumit Prakash','Pune,Maharashtra-411047\n\n\n'),(1000000004,'Amit','Karol Bagh,New Delhi-560037\n');
/*!40000 ALTER TABLE `citizen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrollment_centre`
--

DROP TABLE IF EXISTS `enrollment_centre`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollment_centre` (
  `centre_id` bigint NOT NULL,
  `centre_name` varchar(100) NOT NULL,
  `centre_address` varchar(150) NOT NULL,
  `type` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`centre_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollment_centre`
--

LOCK TABLES `enrollment_centre` WRITE;
/*!40000 ALTER TABLE `enrollment_centre` DISABLE KEYS */;
INSERT INTO `enrollment_centre` VALUES (1001,'Govt Of Karnataka','kengeri s.o., kengeri post office, Bengaluru, Bangalore South, Kengeri, Karnataka - 560060\n','Permanent'),(1002,'Indiapost','POWAI IIT, Mumbai Suburban, Kurla, Mumbai, Maharashtra - 400076\n','Permanent'),(1003,'Govt of Maharashtra','Government Aadhar Seva Kendra 12625,Pune City, Maharashtra - 411047   \n','Camp Mode'),(1004,'Axis Bank Ltd','AXIS BANK LTD, KARTHIKNAGAR, Bengaluru, Bangalore North, Doddanekkundi, Karnataka - 560037\n','Permanent');
/*!40000 ALTER TABLE `enrollment_centre` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrolls`
--

DROP TABLE IF EXISTS `enrolls`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrolls` (
  `poi_no` bigint NOT NULL,
  `centre_id` bigint NOT NULL,
  PRIMARY KEY (`poi_no`,`centre_id`),
  KEY `centre_id` (`centre_id`),
  CONSTRAINT `enrolls_ibfk_1` FOREIGN KEY (`poi_no`) REFERENCES `citizen` (`poi_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `enrolls_ibfk_2` FOREIGN KEY (`centre_id`) REFERENCES `enrollment_centre` (`centre_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrolls`
--

LOCK TABLES `enrolls` WRITE;
/*!40000 ALTER TABLE `enrolls` DISABLE KEYS */;
INSERT INTO `enrolls` VALUES (1000000001,1001),(1000000002,1002),(1000000003,1003);
/*!40000 ALTER TABLE `enrolls` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `family`
--

DROP TABLE IF EXISTS `family`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `family` (
  `por_id` bigint NOT NULL,
  `poi_no` bigint NOT NULL,
  `relation` varchar(10) NOT NULL,
  `uid_of_member` bigint NOT NULL,
  PRIMARY KEY (`por_id`,`poi_no`),
  KEY `poi_no` (`poi_no`),
  CONSTRAINT `family_ibfk_1` FOREIGN KEY (`poi_no`) REFERENCES `citizen` (`poi_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `family`
--

LOCK TABLES `family` WRITE;
/*!40000 ALTER TABLE `family` DISABLE KEYS */;
INSERT INTO `family` VALUES (2000000001,1000000001,'S/O',100000000002);
/*!40000 ALTER TABLE `family` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `operator`
--

DROP TABLE IF EXISTS `operator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `operator` (
  `emp_id` bigint NOT NULL,
  `emp_name` varchar(50) NOT NULL,
  `poi_no` bigint DEFAULT NULL,
  `centre_id` bigint DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
  KEY `centre_id` (`centre_id`),
  KEY `poi_no` (`poi_no`),
  CONSTRAINT `operator_ibfk_1` FOREIGN KEY (`centre_id`) REFERENCES `enrollment_centre` (`centre_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `operator_ibfk_2` FOREIGN KEY (`poi_no`) REFERENCES `citizen` (`poi_no`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `operator`
--

LOCK TABLES `operator` WRITE;
/*!40000 ALTER TABLE `operator` DISABLE KEYS */;
INSERT INTO `operator` VALUES (10001,'Rahul kumar',1000000001,1001),(10002,'Vivek',1000000002,1002);
/*!40000 ALTER TABLE `operator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'aadhaar'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-03 20:02:13
