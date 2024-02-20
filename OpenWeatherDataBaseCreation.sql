-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db
-- Erstellungszeit: 20. Feb 2024 um 20:50
-- Server-Version: 8.3.0
-- PHP-Version: 8.2.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Datenbank: `OpenWeatherMap`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `weather_data`
--

CREATE TABLE `weather_data` (
  `id` int NOT NULL,
  `city` varchar(40) DEFAULT NULL,
  `lon` float DEFAULT NULL,
  `lat` float DEFAULT NULL,
  `weather_main` varchar(25) DEFAULT NULL,
  `weather_desc` varchar(25) DEFAULT NULL,
  `temperature` float DEFAULT NULL,
  `temperature_min` float DEFAULT NULL,
  `temperature_max` float DEFAULT NULL,
  `temperature_feels_like` float DEFAULT NULL,
  `humidity` float DEFAULT NULL,
  `pressure` float DEFAULT NULL,
  `wind_speed` float DEFAULT NULL,
  `wind_direction` float DEFAULT NULL,
  `rain_down_1h` float DEFAULT NULL,
  `clouds` float DEFAULT NULL,
  `country` varchar(25) DEFAULT NULL,
  `canton` varchar(25) DEFAULT NULL,
  `dt` timestamp NULL DEFAULT NULL,
  `sunrise` timestamp NULL DEFAULT NULL,
  `sunset` timestamp NULL DEFAULT NULL,
  `tz` float DEFAULT NULL,
  `time_inserted` timestamp NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indizes der exportierten Tabellen
--

--
-- Indizes für die Tabelle `weather_data`
--
ALTER TABLE `weather_data`
  ADD PRIMARY KEY (`id`),
  ADD KEY `city` (`city`),
  ADD KEY `time_inserted` (`time_inserted`),
  ADD KEY `time_messung` (`dt`),
  ADD KEY `canton` (`canton`) USING BTREE;

--
-- AUTO_INCREMENT für exportierte Tabellen
--

--
-- AUTO_INCREMENT für Tabelle `weather_data`
--
ALTER TABLE `weather_data`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
