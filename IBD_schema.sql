-- phpMyAdmin SQL Dump
-- version 3.5.8.2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Czas wygenerowania: 11 Lis 2015, 11:59
-- Wersja serwera: 5.5.45-log
-- Wersja PHP: 5.3.29

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Baza danych: `stuntman_proj`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Egzemplarz`
--

CREATE TABLE IF NOT EXISTS `Egzemplarz` (
  `id` varchar(6) NOT NULL,
  `DATA_ZAKUPU` date NOT NULL,
  `ID_SPRZET` varchar(4) NOT NULL,
  `ID_SERWIS` varchar(6) NOT NULL,
  `DATA_OST_PRZEG` date NOT NULL,
  `WYCOFANY` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

--
-- Zrzut danych tabeli `Egzemplarz`
--

INSERT INTO `Egzemplarz` (`id`, `DATA_ZAKUPU`, `ID_SPRZET`, `ID_SERWIS`, `DATA_OST_PRZEG`, `WYCOFANY`) VALUES
('2', '2015-11-01', '22', '2', '2015-11-09', 0),
('3', '2015-11-10', '1', '2', '2015-11-09', 0);

--
-- Wyzwalacze `Egzemplarz`
--
DROP TRIGGER IF EXISTS `EGZEMPLARZ_ADD`;
DELIMITER //
CREATE TRIGGER `EGZEMPLARZ_ADD` AFTER INSERT ON `Egzemplarz`
 FOR EACH ROW INSERT INTO Log (TABELA, ID_KROTKI, RODZAJ_OPER, DATA)
VALUES ('EGZEMPLARZ', new.ID, 'Dodanie', CURRENT_TIMESTAMP)
//
DELIMITER ;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Faktury`
--

CREATE TABLE IF NOT EXISTS `Faktury` (
  `ID_FAKTURY` varchar(11) NOT NULL COMMENT 'FORMAT: NR_FAKTURY/ROK',
  `PESEL_PRAC` varchar(11) NOT NULL,
  `PESEL_KLIENTA` varchar(11) NOT NULL,
  `DATA_WYST` date NOT NULL,
  `KWOTA` float NOT NULL,
  PRIMARY KEY (`ID_FAKTURY`),
  UNIQUE KEY `PESEL_PRAC` (`PESEL_PRAC`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Klienci`
--

CREATE TABLE IF NOT EXISTS `Klienci` (
  `PESEL` varchar(11) NOT NULL,
  `IMIE` varchar(20) NOT NULL,
  `NAZWISKO` varchar(30) NOT NULL,
  `NR_DOWODU` varchar(10) NOT NULL COMMENT 'BO SPACJA, TO 10 ZNAKÓW',
  `UWAGI` varchar(100) DEFAULT NULL,
  `ILOSC_TRANSAKCJI` int(11) NOT NULL COMMENT 'AGREGOWANE TRIGGEREM',
  `NR_TELEFONU` varchar(11) NOT NULL,
  PRIMARY KEY (`PESEL`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Log`
--

CREATE TABLE IF NOT EXISTS `Log` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `TABELA` varchar(15) NOT NULL,
  `ID_KROTKI` int(11) NOT NULL,
  `RODZAJ_OPER` varchar(11) NOT NULL,
  `DATA` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin2 AUTO_INCREMENT=5 ;

--
-- Zrzut danych tabeli `Log`
--

INSERT INTO `Log` (`ID`, `TABELA`, `ID_KROTKI`, `RODZAJ_OPER`, `DATA`) VALUES
(3, 'EGZEMPLARZ', 2, 'Dodanie', '2015-11-11'),
(4, 'EGZEMPLARZ', 3, 'Dodanie', '2015-11-11');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `LOGOWANIE`
--

CREATE TABLE IF NOT EXISTS `LOGOWANIE` (
  `PESEL` varchar(11) NOT NULL,
  `LOGIN` varchar(30) NOT NULL,
  `HASLO` varchar(30) NOT NULL,
  PRIMARY KEY (`PESEL`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Pracownicy`
--

CREATE TABLE IF NOT EXISTS `Pracownicy` (
  `PESEL_PRAC` varchar(11) NOT NULL,
  `IMIE` varchar(20) NOT NULL,
  `NAZWISKO` varchar(30) NOT NULL,
  `DATA_STARTU` date NOT NULL,
  `STANOWISKO` varchar(25) NOT NULL,
  `ZWOLNIONY` date DEFAULT NULL,
  `ADRES_EMAIL` varchar(40) NOT NULL,
  PRIMARY KEY (`PESEL_PRAC`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Producent`
--

CREATE TABLE IF NOT EXISTS `Producent` (
  `ID` varchar(6) NOT NULL,
  `NAZWA` varchar(40) NOT NULL,
  `ADRES` varchar(40) NOT NULL,
  `TELEFON` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `rezerwacja`
--

CREATE TABLE IF NOT EXISTS `rezerwacja` (
  `ID` varchar(6) NOT NULL,
  `PESEL_PRAC` varchar(11) NOT NULL,
  `ID_EGZEMPLARZ` varchar(6) NOT NULL,
  `PESEL_KLIENTA` varchar(11) NOT NULL,
  `DATA_START` date NOT NULL,
  `DATA_KONIEC` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Serwis`
--

CREATE TABLE IF NOT EXISTS `Serwis` (
  `ID` varchar(6) NOT NULL,
  `NAZWA` varchar(40) NOT NULL,
  `ADRES` varchar(40) NOT NULL,
  `TELEFON` varchar(10) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Sprzet`
--

CREATE TABLE IF NOT EXISTS `Sprzet` (
  `ID` varchar(4) NOT NULL,
  `NAZWA` varchar(20) NOT NULL,
  `MARKA` varchar(30) NOT NULL,
  `ID_PRODUCENT` varchar(6) NOT NULL,
  `KATEGORIA` varchar(20) NOT NULL,
  `DATA_ZAKUPU` date NOT NULL,
  `ILOSC` int(11) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `Wypozyczenia`
--

CREATE TABLE IF NOT EXISTS `Wypozyczenia` (
  `ID_EGZEMPLARZA` varchar(6) NOT NULL,
  `ID_FAKTURY` varchar(11) NOT NULL,
  `PESEL_KLIENTA` varchar(11) NOT NULL,
  `PESEL_PRAC` varchar(11) NOT NULL,
  `DATA_WYP` date NOT NULL,
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2 COMMENT='Kilka wypożyczeń może być na jednej fakturze' AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `WypozyczeniaArchiwum`
--

CREATE TABLE IF NOT EXISTS `WypozyczeniaArchiwum` (
  `ID` varchar(6) NOT NULL,
  `ID_SPRZETU` varchar(4) NOT NULL,
  `ID_FAKTURY` varchar(11) NOT NULL,
  `PESEL_KLIENTA` varchar(11) NOT NULL,
  `PESEL_PRAC` varchar(11) NOT NULL,
  `DATA_WYP` date NOT NULL,
  `DATA_ZWROTU` date NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin2;

--
-- Ograniczenia dla zrzutów tabel
--

--
-- Ograniczenia dla tabeli `Faktury`
--
ALTER TABLE `Faktury`
  ADD CONSTRAINT `Faktury_ibfk_1` FOREIGN KEY (`PESEL_PRAC`) REFERENCES `Pracownicy` (`PESEL_PRAC`);

--
-- Ograniczenia dla tabeli `LOGOWANIE`
--
ALTER TABLE `LOGOWANIE`
  ADD CONSTRAINT `LOGOWANIE_ibfk_1` FOREIGN KEY (`PESEL`) REFERENCES `Pracownicy` (`PESEL_PRAC`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
