-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 10, 2021 at 08:40 AM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `cust_booking`
--

CREATE TABLE `cust_booking` (
  `book_id` int(5) NOT NULL,
  `cust_contact` int(10) NOT NULL,
  `cust_ema` varchar(50) NOT NULL,
  `chein_date` varchar(10) NOT NULL,
  `cheout_date` varchar(10) NOT NULL,
  `rm_type` varchar(20) NOT NULL,
  `av_room` int(10) NOT NULL,
  `n_day` int(10) NOT NULL,
  `n_eld` int(10) NOT NULL,
  `n_chld` int(10) NOT NULL,
  `status` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cust_booking`
--

INSERT INTO `cust_booking` (`book_id`, `cust_contact`, `cust_ema`, `chein_date`, `cheout_date`, `rm_type`, `av_room`, `n_day`, `n_eld`, `n_chld`, `status`) VALUES
(10, 2147483647, '', '16/09/2021', '18/09/2021', 'Deluxe Room', 306, 2, 2, 0, 'avialable'),
(12, 2147483647, '', '14/09/2021', '15/09/2021', 'Twin Room', 104, 2, 2, 0, 'avialable'),
(13, 2147483647, '', '15/09/2021', '17/09/2021', 'Duplex Room', 301, 2, 2, 0, 'avialable'),
(14, 2147483647, '', '14/09/2021', '16/09/2021', 'Double Room', 102, 2, 2, 0, 'avialable'),
(15, 951047552, 'himan@gmail.com', '15/09/2021', '15/09/2021', 'Deluxe Room', 201, 1, 2, 0, 'booking pending'),
(16, 2147483647, 'him', '14/09/2021', '15/09/2021', 'Single Room', 103, 1, 2, 0, 'booking pending'),
(17, 0, '', '13/09/2021', '13/09/2021', 'select', 0, 0, 0, 0, 'booking pending'),
(18, 2147483647, 'himan@gmail.com', '14/09/2021', '15/09/2021', 'Twin Room', 103, 1, 1, 0, 'booking pending'),
(20, 2147483647, 'himan@gmail.com', '14/09/2021', '16/09/2021', 'Deluxe Room', 305, 1, 1, 0, 'booking pending'),
(21, 2147483647, 'himan@gmail.com', '14/09/2021', '16/09/2021', 'Double Room', 104, 2, 2, 0, 'booking confirm'),
(22, 2147483647, 'jaimal@gmail.com', '14/09/2021', '17/09/2021', 'Twin Room', 103, 3, 2, 0, 'booking pending'),
(23, 2147483647, 'himan@gmail.com', '14/09/2021', '16/09/2021', 'Double Room', 106, 2, 1, 0, 'booking pending'),
(24, 2147483647, 'himan@gmail.com', '15/09/2021', '16/09/2021', 'Single Room', 103, 1, 1, 0, 'booking pending'),
(25, 2147483647, 'himan@gmail.com', '15/09/2021', '17/09/2021', 'Single Room', 301, 2, 1, 0, 'booking pending');

-- --------------------------------------------------------

--
-- Table structure for table `cust_reg`
--

CREATE TABLE `cust_reg` (
  `cust_id` int(3) NOT NULL,
  `fname` varchar(30) NOT NULL,
  `lname` varchar(30) NOT NULL,
  `email` varchar(40) NOT NULL,
  `mobile_no` int(12) NOT NULL,
  `security_question` varchar(100) NOT NULL,
  `security_answer` varchar(100) NOT NULL,
  `password` varchar(30) NOT NULL,
  `confirm_password` varchar(30) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `nationality` varchar(30) NOT NULL,
  `idpf` varchar(30) NOT NULL,
  `Address` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cust_reg`
--

INSERT INTO `cust_reg` (`cust_id`, `fname`, `lname`, `email`, `mobile_no`, `security_question`, `security_answer`, `password`, `confirm_password`, `gender`, `nationality`, `idpf`, `Address`) VALUES
(17, 'himanshu', 'patil', 'himan@gmail.com', 2147483647, 'your birth place', 'pune', 'him23', 'him23', 'male', 'biblewadi,pune', 'Indian', 'DrivingLicence'),
(18, 'nalini', 'patil', 'nalini@gmail.com', 2147483647, 'your birth place', 'nandurbar', 'nal79', 'nal79', 'male', 'nandurbar', 'Indian', 'AadharCard'),
(19, 'abhishek', 'pande', 'abhishek@gmail.com', 2147483647, 'your favourite game', 'cricket', 'abhi', 'abhi', 'male', 'nanded', 'Indian', 'AadharCard'),
(20, 'dinesh', 'patil', 'dinesh@gmail.com', 2147483647, 'Your pet name', 'dinu', 'din23', 'din23', 'male', 'nanded', 'Indian', 'AadharCard'),
(21, 'aditya', 'deshpande', 'deshpande@gmail.com', 2147483647, 'your birth place', 'pune', 'adit17', 'adit17', 'male', 'laxmi nagar,nanded', 'Indian', 'AadharCard'),
(22, 'tushar', 'sharma', 'tushar@gmail.com', 2147483647, 'your favourite game', 'chess', 'tus@', 'tus@', 'male', 'pune', 'Indian', 'AadharCard');

-- --------------------------------------------------------

--
-- Table structure for table `dinner`
--

CREATE TABLE `dinner` (
  `dinner_id` int(5) NOT NULL,
  `rm_no` int(3) NOT NULL,
  `meal_type` varchar(20) NOT NULL,
  `meal` varchar(30) NOT NULL,
  `quantity` int(5) NOT NULL,
  `status` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dinner`
--

INSERT INTO `dinner` (`dinner_id`, `rm_no`, `meal_type`, `meal`, `quantity`, `status`) VALUES
(12, 301, 'Dinner', 'pav bhaji', 2, 'pending');

-- --------------------------------------------------------

--
-- Table structure for table `room_details`
--

CREATE TABLE `room_details` (
  `rm_id` int(4) NOT NULL,
  `price` int(20) NOT NULL,
  `select_room` varchar(50) NOT NULL,
  `desc` varchar(300) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room_details`
--

INSERT INTO `room_details` (`rm_id`, `price`, `select_room`, `desc`) VALUES
(16, 3000, 'Single Room', 'This is single room'),
(17, 6000, 'Double Room', 'This is double room'),
(18, 8000, 'Deluxe Room', 'This is delux room'),
(19, 10000, 'Double-Double (Twin ', 'This is double-double room'),
(20, 11000, 'Duplex Room', 'This is duplex room'),
(21, 11000, 'Double-Double (Twin Double) Room', 'This is double-twin room'),
(22, 8000, 'Twin Room', 'This is twin room');

-- --------------------------------------------------------

--
-- Table structure for table `room_service`
--

CREATE TABLE `room_service` (
  `ser_id` int(3) NOT NULL,
  `rm_no` int(3) NOT NULL,
  `des` varchar(500) NOT NULL,
  `status` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room_service`
--

INSERT INTO `room_service` (`ser_id`, `rm_no`, `des`, `status`) VALUES
(2, 102, 'this ia room 102', 'request accepted'),
(3, 103, 'This is 103', 'request accepted'),
(6, 102, 'Our basing is not clean please clean it', 'request pending'),
(7, 103, 'Please clean the room floor immediately', 'request pending'),
(8, 102, 'cleaning', 'request accepted'),
(9, 301, 'please clean bathroom sink', 'request pending');

-- --------------------------------------------------------

--
-- Table structure for table `staff_details`
--

CREATE TABLE `staff_details` (
  `staff_id` int(3) NOT NULL,
  `fl_name` varchar(60) NOT NULL,
  `idno` int(12) NOT NULL,
  `mob_no` int(10) NOT NULL,
  `address` varchar(200) NOT NULL,
  `age` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `position` varchar(20) NOT NULL,
  `username` varchar(12) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff_details`
--

INSERT INTO `staff_details` (`staff_id`, `fl_name`, `idno`, `mob_no`, `address`, `age`, `gender`, `position`, `username`, `password`) VALUES
(6, 'himanshu patil', 477532578, 2147483647, 'pune', '10/09/1998', 'Male', 'Recieptionist', 'himan', 'him23'),
(7, 'rokesh patil', 7837, 2147483647, 'parandwadi ,pune', '05/09/1996', 'Male', 'Recieptionist', 'rok', 'rok23'),
(8, 'prakash pande', 7878, 2147483647, 'biblewadi,pune', '10/09/1993', 'Male', 'Room service', 'prak', 'prak23'),
(9, 'ujawal kaushik', 7865, 934656375, 'parandwadi,pune', '20/09/1990', 'Male', 'Kitchen staff', 'ujava24', 'ujava23'),
(10, 'jatin patil', 7865, 934656375, 'parandwadi,pune', '22/09/1988', 'Male', 'Kitchen staff', 'jatin34', 'jatin53'),
(13, 'Nalini patil', 262900, 2147483647, 'nanded', '06/09/1989', 'Male', 'Kitchen staff', 'nal22', 'nal22');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cust_booking`
--
ALTER TABLE `cust_booking`
  ADD PRIMARY KEY (`book_id`);

--
-- Indexes for table `cust_reg`
--
ALTER TABLE `cust_reg`
  ADD PRIMARY KEY (`cust_id`);

--
-- Indexes for table `dinner`
--
ALTER TABLE `dinner`
  ADD PRIMARY KEY (`dinner_id`);

--
-- Indexes for table `room_details`
--
ALTER TABLE `room_details`
  ADD PRIMARY KEY (`rm_id`);

--
-- Indexes for table `room_service`
--
ALTER TABLE `room_service`
  ADD PRIMARY KEY (`ser_id`);

--
-- Indexes for table `staff_details`
--
ALTER TABLE `staff_details`
  ADD PRIMARY KEY (`staff_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cust_booking`
--
ALTER TABLE `cust_booking`
  MODIFY `book_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `cust_reg`
--
ALTER TABLE `cust_reg`
  MODIFY `cust_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `dinner`
--
ALTER TABLE `dinner`
  MODIFY `dinner_id` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `room_details`
--
ALTER TABLE `room_details`
  MODIFY `rm_id` int(4) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `room_service`
--
ALTER TABLE `room_service`
  MODIFY `ser_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `staff_details`
--
ALTER TABLE `staff_details`
  MODIFY `staff_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
