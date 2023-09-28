CREATE TABLE IF NOT EXISTS `%s` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date_import` date NOT NULL,
  `department` varchar(100) NOT NULL,
  `type_of_furniture` varchar(100) NOT NULL,
  `price` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;