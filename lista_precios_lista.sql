-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: lista_precios
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lista`
--

DROP TABLE IF EXISTS `lista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lista` (
  `producto` varchar(45) DEFAULT NULL,
  `precio` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lista`
--

LOCK TABLES `lista` WRITE;
/*!40000 ALTER TABLE `lista` DISABLE KEYS */;
INSERT INTO `lista` VALUES ('Inka Kola 500 ml',2.5),('Inka Kola 500 ml',2.5),('CocaCola 500 ml',2.5),('Fanta 500 ml',1.5),('Gatorade 500 ml',2.8),('Volt 450 ml',2),('Pepsi 500 ml',1.8),('FreeTea 500 ml',2.5),('Agua San Luis 625 ml',2.2),('Agua Cielo 625 ml',1.8),('Sporade 500 ml',2.8),('Galleta Picaras',0.8),('Papas Lays',0.5),('Doritos',0.8),('Galleta SodaField',0.5),('Chocolate Iberica',3),('Chocolate Sublime',1),('Piqueo Snack',1),('Doña Pepa',1.8),('Barra energitca Cereal bar',1.5),('Galleta Chokis',1.5),('Donofrio Lucuma 1L',5),('Nestle beso de moza 1L',5.5),('Nestle morochas 1L',5.5),('Donofrio Tornado  Lucuma 1L',5),('Donofrio Tornado Vainilla 1L',5.5),('San Fernando 15 Nuggets',10),('San Fernando 6 hamburguesas',12.5),('Pizza Peperoni',9),('Pizza Americana',9),('Pack de Ravioles',10),('Hamburguesa de carne',3.5),('Hamburguesa de pollo',3.5),('Empanada de carne',2.5),('Empanada de pollo',2.5),('Pollo frito',6),('Wrap de pollo',5),('Wrap de carne',5),('Choripan',3),('Siu May',2.5),('Min Pao',3.5),('Jabon Dove',4),('Shampoo H&S Old Spice',7),('Pasta dental Colgate',5),('Cepillo dental Colgate',5),('Hoja de afeitar gillete',5.5),('Toallas femeninas LadySoft',6.5),('Enjuague Bucal Listerine 500ml',8),('Pasta dental Dento',5),('Crema de afeitar Gillete',8),('Shampoo H&S de menta 375ml',6);
/*!40000 ALTER TABLE `lista` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-11 20:59:46
