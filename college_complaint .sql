-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Jan 07, 2025 at 01:05 PM
-- Server version: 10.1.16-MariaDB
-- PHP Version: 7.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `college_complaint`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(255) NOT NULL,
  `admin_id` varchar(255) NOT NULL,
  `email_id` varchar(255) NOT NULL,
  `phoneno` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `admin_complaints`
--

CREATE TABLE `admin_complaints` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `complaint_type` varchar(255) NOT NULL,
  `faculty_name` varchar(255) NOT NULL,
  `complaint_details` text NOT NULL,
  `evidence` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT 'Pending',
  `action` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin_complaints`
--

INSERT INTO `admin_complaints` (`id`, `complaint_type`, `faculty_name`, `complaint_details`, `evidence`, `status`, `action`) VALUES
(1, 'Academic', 'Ayishath Safwana', '123', NULL, 'Approved', NULL),
(2, 'Personal', 'Ayishath Safwana', 'diya', NULL, 'Pending', NULL),
(3, 'Academic', 'Ayishath Safwana', 'diya1', NULL, 'Pending', NULL),
(4, 'Non-Academic', 'Sindhu', 'mydear kutty', NULL, 'Pending', NULL),
(5, 'Personal', 'Ayishath Safwana', 'hello1', NULL, 'Pending', NULL),
(6, 'Personal', 'Ayishath Safwana', '7777', NULL, 'Pending', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `complaints`
--

CREATE TABLE `complaints` (
  `id` int(11) NOT NULL,
  `complaint_type` varchar(100) NOT NULL,
  `category` varchar(100) NOT NULL,
  `faculty_name` varchar(100) NOT NULL,
  `complaint_details` text NOT NULL,
  `evidence` varchar(255) DEFAULT NULL,
  `status` varchar(255) DEFAULT 'Pending',
  `username` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `complaints`
--

INSERT INTO `complaints` (`id`, `complaint_type`, `category`, `faculty_name`, `complaint_details`, `evidence`, `status`, `username`) VALUES
(17, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'ss', NULL, 'Pending', ''),
(18, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'sss', NULL, 'Pending', ''),
(19, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'sss', NULL, 'Pending', ''),
(20, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'need holiday', NULL, 'Pending', ''),
(21, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'hello', NULL, 'Pending', ''),
(22, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'hello', NULL, 'Pending', ''),
(23, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'hello', NULL, 'Pending', ''),
(24, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'hello', NULL, 'Pending', ''),
(25, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 's', NULL, 'Pending', ''),
(26, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'hello1', NULL, 'Pending', ''),
(27, 'Academic', 'Faculty', 'Ayishath Safwana', 'fff', NULL, 'Pending', ''),
(28, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'wwww', NULL, 'Pending', ''),
(29, 'Personal', 'Faculty', 'Ayishath Safwana', 'wwww', NULL, 'Pending', ''),
(30, 'Academic', 'Faculty', 'Ayishath Safwana', 'qqqq', NULL, 'Pending', ''),
(31, 'Academic', 'Faculty', 'Ayishath Safwana', 'wwwww123', 'static/uploads\\images_1.jpeg', 'Pending', ''),
(32, 'Academic', 'Faculty', 'Ayishath Safwana', '1', NULL, 'Pending', ''),
(33, 'Academic', 'Faculty', 'Ayishath Safwana', '1', NULL, 'Pending', ''),
(34, 'Academic', 'Faculty', 'Ayishath Safwana', '1', NULL, 'Pending', ''),
(35, 'Academic', 'Faculty', 'Ayishath Safwana', '1', NULL, 'Pending', ''),
(36, 'Academic', 'Faculty', 'Ayishath Safwana', '1', NULL, 'Pending', ''),
(37, 'Academic', 'Faculty', 'Ayishath Safwana', '1', NULL, 'Pending', ''),
(38, 'Academic', 'Admins', 'Ayishath Safwana', 'ss', NULL, 'Pending', ''),
(39, 'Academic', 'Admins', 'Ayishath Safwana', 'dd', NULL, 'Pending', ''),
(45, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'qwerty123', NULL, 'Pending', 'jobin'),
(46, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'holiday', NULL, 'Pending', 'jobin'),
(47, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'holiday', NULL, 'Pending', 'jobin'),
(48, 'Non-Academic', 'Faculty', 'Ayishath Safwana', 'needed', NULL, 'Pending', 'jobin'),
(49, 'Academic', 'Faculty', 'Ayishath Safwana', 'rrr', NULL, 'Pending', 'jobin'),
(50, 'Academic', 'Admins', 'Manjula', 'admin', NULL, 'Pending', 'jobin'),
(51, 'Academic', 'Admins', 'Ayishath Safwana', 'alfa', NULL, 'Pending', 'jobin'),
(52, 'Academic', 'Admins', 'Ayishath Safwana', 'diya1', NULL, 'Pending', 'jobin'),
(53, 'Academic', 'Admins', 'Ayishath Safwana', 'mydear', NULL, 'Pending', 'jobin'),
(54, 'Non-Academic', 'Admins', 'Ayishath Safwana', 'mydear', NULL, 'Pending', 'jobin'),
(55, 'Non-Academic', 'Faculty', 'Manjula', 'hello123', NULL, 'Pending', 'jobin'),
(56, 'Non-Academic', 'Admins', 'Sindhu', 'mydear kutty', NULL, 'Pending', 'jobin'),
(57, 'Academic', 'Faculty', 'Ayishath Safwana', 'hano', 'static/uploads\\Screenshot_2024-12-31_114328.png', 'Pending', 'jobin'),
(58, 'Academic', 'Faculty', 'Ayishath Safwana', 'hello', NULL, 'Pending', 'jobin'),
(59, 'Academic', 'Faculty', 'Ayishath Safwana', 'hello345', NULL, 'Pending', 'jobin'),
(60, 'Academic', 'Faculty', 'Ayishath Safwana', 'hello', NULL, 'Pending', 'jobin'),
(61, 'Academic', 'Faculty', 'Ayishath Safwana', 'fff', NULL, 'Pending', 'jobin'),
(62, 'Academic', 'Faculty', 'Ayishath Safwana', 'd', NULL, 'Pending', 'jobin'),
(63, 'Academic', 'Faculty', 'Ayishath Safwana', 'd', NULL, 'Pending', 'jobin'),
(64, 'Academic', 'Faculty', 'Ayishath Safwana', 'd', NULL, 'Pending', 'jobin'),
(65, 'Academic', 'Faculty', 'Ayishath Safwana', '1', NULL, 'Pending', 'jobin'),
(66, 'Academic', 'Faculty', 'Ayishath Safwana', 'q', NULL, 'Pending', 'jobin'),
(67, 'Academic', 'Faculty', 'Ayishath Safwana', 's', NULL, 'Pending', 'jobin'),
(68, 'Academic', 'Admins', 'Ayishath Safwana', 'h345', NULL, 'Pending', 'jobin');

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `username` varchar(255) NOT NULL,
  `employee_id` varchar(255) NOT NULL,
  `email_id` varchar(255) NOT NULL,
  `phoneno` varchar(20) NOT NULL,
  `department` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`username`, `employee_id`, `email_id`, `phoneno`, `department`, `password`) VALUES
('jobin', '123', 'j@gmail.com', '9740319908', 'cse', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
('jobin', '234', 'j@gmail.com', '9740319908', 'mca', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
('jobin', '567', 'jj@gmail.com', '9740319908', 'cse', '35a9e381b1a27567549b5f8a6f783c167ebf809f1c4d6a9e367240484d8ce281'),
('rahul', '889', 'jj@gmail.com', '9740319908', 'mca', 'bdc5d8a48c23897906b09a9a3680bd2e9c8b3121edbda36f949800f0959c8d55');

-- --------------------------------------------------------

--
-- Table structure for table `faculty_complaints`
--

CREATE TABLE `faculty_complaints` (
  `id` int(11) NOT NULL,
  `complaint_type` varchar(255) DEFAULT NULL,
  `faculty_name` varchar(255) DEFAULT NULL,
  `complaint_details` text,
  `evidence` varchar(255) DEFAULT NULL,
  `username` varchar(255) NOT NULL,
  `status` varchar(20) DEFAULT 'Pending',
  `action` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `faculty_complaints`
--

INSERT INTO `faculty_complaints` (`id`, `complaint_type`, `faculty_name`, `complaint_details`, `evidence`, `username`, `status`, `action`) VALUES
(1, 'Non-Academic', 'Ayishath Safwana', 'hello', NULL, '', 'Approved', NULL),
(2, 'Non-Academic', 'Ayishath Safwana', 'hello', NULL, '', 'Rejected', NULL),
(3, 'Non-Academic', 'Ayishath Safwana', 'hello', NULL, '', 'Approved', NULL),
(4, 'Non-Academic', 'Ayishath Safwana', 's', NULL, '', 'Approved', NULL),
(5, 'Non-Academic', 'Ayishath Safwana', 'hello1', NULL, '', 'Approved', NULL),
(6, 'Academic', 'Ayishath Safwana', 'fff', NULL, '', 'Pending', NULL),
(7, 'Non-Academic', 'Ayishath Safwana', 'wwww', NULL, '', 'Pending', NULL),
(8, 'Personal', 'Ayishath Safwana', 'wwww', NULL, '', 'Pending', NULL),
(9, 'Academic', 'Ayishath Safwana', 'qqqq', NULL, '', 'Pending', NULL),
(10, 'Academic', 'Ayishath Safwana', 'wwwww123', 'static/uploads\\images_1.jpeg', '', 'Pending', NULL),
(11, 'Academic', 'Ayishath Safwana', '1', NULL, '', 'Pending', NULL),
(12, 'Academic', 'Ayishath Safwana', '1', NULL, '', 'Pending', NULL),
(13, 'Academic', 'Ayishath Safwana', '1', NULL, '', 'Pending', NULL),
(14, 'Academic', 'Ayishath Safwana', '1', NULL, '', 'Pending', NULL),
(15, 'Academic', 'Ayishath Safwana', '1', NULL, '', 'Approved', NULL),
(16, 'Academic', 'Ayishath Safwana', '1', NULL, '', 'Rejected', NULL),
(19, 'Non-Academic', 'Ayishath Safwana', 'qwerty123', NULL, 'jobin', 'Approved', NULL),
(20, 'Non-Academic', 'Ayishath Safwana', 'holiday', NULL, 'jobin', 'Approved', NULL),
(21, 'Non-Academic', 'Ayishath Safwana', 'holiday', NULL, 'jobin', 'Pending', NULL),
(22, 'Non-Academic', 'Ayishath Safwana', 'needed', NULL, 'jobin', 'Pending', NULL),
(23, 'Academic', 'Ayishath Safwana', 'rrr', NULL, 'jobin', 'Pending', NULL),
(24, 'Non-Academic', 'Manjula', 'hello123', NULL, 'jobin', 'Pending', NULL),
(25, 'Academic', 'Ayishath Safwana', 'hano', 'static/uploads\\Screenshot_2024-12-31_114328.png', 'jobin', 'Pending', NULL),
(26, 'Academic', 'Ayishath Safwana', 'hello', NULL, 'jobin', 'Pending', NULL),
(27, 'Academic', 'Ayishath Safwana', 'hello345', NULL, 'jobin', 'Pending', NULL),
(28, 'Academic', 'Ayishath Safwana', 'hello', NULL, 'jobin', 'Pending', NULL),
(29, 'Academic', 'Ayishath Safwana', 'fff', NULL, 'jobin', 'Pending', NULL),
(30, 'Academic', 'Ayishath Safwana', 'd', NULL, 'jobin', 'Pending', NULL),
(31, 'Academic', 'Ayishath Safwana', 'd', NULL, 'jobin', 'Pending', NULL),
(32, 'Academic', 'Ayishath Safwana', 'd', NULL, 'jobin', 'Pending', NULL),
(33, 'Academic', 'Ayishath Safwana', '1', NULL, 'jobin', 'Pending', NULL),
(34, 'Academic', 'Ayishath Safwana', 'q', NULL, 'jobin', 'Pending', NULL),
(35, 'Academic', 'Ayishath Safwana', 's', NULL, 'jobin', 'Pending', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `poll_votes`
--

CREATE TABLE `poll_votes` (
  `id` int(11) NOT NULL,
  `complaint_id` int(11) NOT NULL,
  `vote` enum('support','not_support') NOT NULL,
  `vote_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `poll_votes`
--

INSERT INTO `poll_votes` (`id`, `complaint_id`, `vote`, `vote_timestamp`) VALUES
(8, 17, 'support', '2025-01-03 06:08:42'),
(9, 17, 'not_support', '2025-01-03 06:10:23'),
(10, 17, 'not_support', '2025-01-03 06:10:39'),
(11, 17, 'not_support', '2025-01-03 06:12:33'),
(12, 20, 'support', '2025-01-03 06:33:38'),
(13, 20, 'support', '2025-01-03 08:33:05'),
(14, 26, 'not_support', '2025-01-03 10:21:14'),
(15, 26, 'support', '2025-01-03 10:21:30'),
(17, 46, 'support', '2025-01-06 06:15:38'),
(18, 48, 'support', '2025-01-06 06:44:50'),
(19, 48, 'not_support', '2025-01-06 06:44:57');

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `username` varchar(255) NOT NULL,
  `registration_no` varchar(255) NOT NULL,
  `email_id` varchar(255) NOT NULL,
  `phoneno` varchar(20) NOT NULL,
  `department` varchar(100) NOT NULL,
  `specialization` varchar(100) DEFAULT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`username`, `registration_no`, `email_id`, `phoneno`, `department`, `specialization`, `password`) VALUES
('jobin', '', 'j@gmail.com', '9740319908', 'cse', NULL, 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3'),
('yathish', '12345', 'jm@gmail.com', '778899000', 'it', 'bca', 'eaf89db7108470dc3f6b23ea90618264b3e8f8b6145371667c4055e9c5ce9f52'),
('yamuna', '22222', 'jj@gamil.com', '9740319908', 'mca', 'cse', 'f6e0a1e2ac41945a9aa7ff8a8aaa0cebc12a3bcc981a929ad5cf810a090e11ae'),
('naga', '2345678', 'jj1@gmail.com', '9740319908', 'mca', 'cse', '9af15b336e6a9619928537df30b2e6a2376569fcf9d7e773eccede65606529a0'),
('jacob', '4213333', 'jj@gmail.com', '9740319908', 'mca', 'cse', '234'),
('jobin', 'jobin', 'j@gmail.com', '9740319908mca', 'mca', 'cse', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `admin_complaints`
--
ALTER TABLE `admin_complaints`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `complaints`
--
ALTER TABLE `complaints`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`employee_id`);

--
-- Indexes for table `faculty_complaints`
--
ALTER TABLE `faculty_complaints`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `poll_votes`
--
ALTER TABLE `poll_votes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `complaint_id` (`complaint_id`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`registration_no`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_complaints`
--
ALTER TABLE `admin_complaints`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `complaints`
--
ALTER TABLE `complaints`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;
--
-- AUTO_INCREMENT for table `faculty_complaints`
--
ALTER TABLE `faculty_complaints`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
--
-- AUTO_INCREMENT for table `poll_votes`
--
ALTER TABLE `poll_votes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `poll_votes`
--
ALTER TABLE `poll_votes`
  ADD CONSTRAINT `poll_votes_ibfk_1` FOREIGN KEY (`complaint_id`) REFERENCES `complaints` (`id`) ON DELETE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
