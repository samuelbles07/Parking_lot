-- MySQL dump 10.16  Distrib 10.1.38-MariaDB, for debian-linux-gnueabihf (armv7l)
--
-- Host: localhost    Database: parking_lot
-- ------------------------------------------------------
-- Server version	10.1.38-MariaDB-0+deb9u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `keluar`
--

DROP TABLE IF EXISTS `keluar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `keluar` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `no_masuk` int(4) unsigned zerofill NOT NULL,
  `jam_keluar` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `durasi_parkir` int(5) DEFAULT NULL,
  `total_rupiah` int(7) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `no_masuk` (`no_masuk`),
  CONSTRAINT `keluar_ibfk_1` FOREIGN KEY (`no_masuk`) REFERENCES `masuk` (`no_urut`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `keluar`
--

LOCK TABLES `keluar` WRITE;
/*!40000 ALTER TABLE `keluar` DISABLE KEYS */;
INSERT INTO `keluar` VALUES (4,0007,'2019-06-17 14:13:20',7,3000),(5,0008,'2019-06-17 14:24:32',9,3000),(6,0009,'2019-06-17 14:35:18',4,3000),(7,0010,'2019-06-17 14:36:02',12,3000);
/*!40000 ALTER TABLE `keluar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `masuk`
--

DROP TABLE IF EXISTS `masuk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `masuk` (
  `no_urut` int(4) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `kode_barcode` varchar(50) DEFAULT NULL,
  `jam_masuk` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`no_urut`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `masuk`
--

LOCK TABLES `masuk` WRITE;
/*!40000 ALTER TABLE `masuk` DISABLE KEYS */;
INSERT INTO `masuk` VALUES (0001,'25897529527','2019-06-17 07:26:45'),(0006,'00011560800897.0','2019-06-17 12:48:17'),(0007,'00061560806000','2019-06-17 14:13:20'),(0008,'00071560806672','2019-06-17 14:24:32'),(0009,'00081560807318','2019-06-17 14:35:18'),(0010,'00091560807362','2019-06-17 14:36:02');
/*!40000 ALTER TABLE `masuk` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-06-23 16:33:39
