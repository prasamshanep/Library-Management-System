-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 04, 2020 at 09:03 AM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.2.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `collagelibrary`
--

-- --------------------------------------------------------

--
-- Table structure for table `bookss`
--

CREATE TABLE `bookss` (
  `id` int(255) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `quantity` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `bookss`
--

INSERT INTO `bookss` (`id`, `name`, `author`, `quantity`) VALUES
(1, 'The Digital Flood', 'James W. Cortada', '10'),
(4, 'Information System', 'Mahmoud', '2'),
(5, 'Python Algorythm', 'John', '9'),
(6, 'Forensics', 'Prem Gautam', '6'),
(7, 'Managing Cybersecurity ', 'Jonathan Reuvid', '2'),
(8, 'Cyber War', 'Julian Richard ', '2'),
(9, 'Java Design Pattlerns', 'Vaskaran Sarcar ', '1'),
(10, 'Fluent Python', 'Luciano Ramalho', '3'),
(11, 'Internet of Things ', 'Perry Lea', '4'),
(12, 'Building Web Application', 'Sumit Gupta', '5'),
(13, 'Career Counseling ', 'W.Bruce Wash', '2'),
(14, 'Django Web Development', 'Jake Kronika', '2'),
(15, 'C++ Programing for smartphone', 'Jo Stichbury', '3'),
(16, 'Mean Web Development ', 'Amos Q.Haviv', '1'),
(17, 'Unity 2D game development', 'Claudio Scolastici', '5'),
(18, 'Introduction to Game degine', 'Jeremy Gibson Bond', '6'),
(19, 'Amazon Machine Learning ', 'Alexis Perrier ', '7'),
(20, 'Get Programming ', 'Isaac Abraham', '3');

-- --------------------------------------------------------

--
-- Table structure for table `issue`
--

CREATE TABLE `issue` (
  `id` int(11) NOT NULL,
  `bookname` varchar(100) DEFAULT NULL,
  `bookid` varchar(100) DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  `issuedate` date DEFAULT NULL,
  `fine` int(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `issue`
--

INSERT INTO `issue` (`id`, `bookname`, `bookid`, `username`, `issuedate`, `fine`) VALUES
(2, 'Python Algorythm', '5', '5555', '2020-08-20', 10),
(3, 'Cyber War', '8', '0000', '2020-08-12', 10),
(4, 'Internet of Things ', '11', '09090', '2020-07-31', 10),
(5, 'Java Design Pattlerns', '9', '09090', '0202-07-30', 10),
(6, 'Get Programming ', '20', '5567', '2022-09-02', NULL),
(7, 'Mean Web Development ', '16', '22222', '0202-09-02', NULL),
(8, 'Amazon Machine Learning ', '19', '5555', '2020-09-02', NULL),
(9, 'Forensics', '6', '5555', '2020-08-29', NULL),
(10, 'Python Algorythm', '5', '22222', '2020-09-03', NULL),
(11, 'Cyber War', '8', '45678', '2020-09-04', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(255) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `gmail` varchar(100) DEFAULT NULL,
  `number` int(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `fullname`, `password`, `gmail`, `number`) VALUES
(1, '00909', 'Pranab Nepal', 'pranab', 'pranab@gmail.com', 6656565),
(2, '22222', 'Devi Guragain', 'devi', 'devi@gmail.com', 887788),
(5, '5555', 'Utsav Sitaula', 'Password', 'utsav@gmail.com', 8989898),
(7, '008002', 'Utsav Sitaula', 'Password', 'utsav@gmail.com', 8989898),
(8, '5567', 'Samjauta Aryal', 'Password', 'aryal@gmail.com', 9989898),
(10, '09090', 'Smriti Rai', 'smriti', 'smi@gmail.com', 73737),
(11, '0000', 'Prasamsha', 'Passwor', 'nepal@gmail.com', 23989898),
(12, '45678', 'Samikshya Aryal ', 'aryal', 'aryal@gmail.com', 721424);

-- --------------------------------------------------------

--
-- Table structure for table `user_admin`
--

CREATE TABLE `user_admin` (
  `id` int(255) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `fullname` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `gmail` varchar(100) DEFAULT NULL,
  `number` int(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_admin`
--

INSERT INTO `user_admin` (`id`, `username`, `fullname`, `password`, `gmail`, `number`) VALUES
(1, '123456', 'Prasamsha Nepal', 'admin', '88', 562341819);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `bookss`
--
ALTER TABLE `bookss`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `issue`
--
ALTER TABLE `issue`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `user_admin`
--
ALTER TABLE `user_admin`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `bookss`
--
ALTER TABLE `bookss`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `issue`
--
ALTER TABLE `issue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `user_admin`
--
ALTER TABLE `user_admin`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
