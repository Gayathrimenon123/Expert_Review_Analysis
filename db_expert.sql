-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 12, 2022 at 10:08 AM
-- Server version: 5.5.8
-- PHP Version: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `db_expert`
--

-- --------------------------------------------------------

--
-- Table structure for table `company`
--

CREATE TABLE IF NOT EXISTS `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `logo` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`id`, `name`, `logo`) VALUES
(1, 'Maruthi Suzuki', '/media/dacdd077253d3562154bc4d518e8969a.jpg'),
(2, 'Ford', '/media/Ford_logo_flat.svg.png');

-- --------------------------------------------------------

--
-- Table structure for table `custreg`
--

CREATE TABLE IF NOT EXISTS `custreg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mob` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `house` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL,
  `district` varchar(50) NOT NULL,
  `state` varchar(50) NOT NULL,
  `pin` varchar(6) NOT NULL,
  `lname` varchar(50) NOT NULL,
  `regDate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `custreg`
--

INSERT INTO `custreg` (`id`, `name`, `email`, `mob`, `username`, `house`, `place`, `district`, `state`, `pin`, `lname`, `regDate`) VALUES
(1, 'ramu', 'ramu@gmail.com', '9947130327', 'ramu', 'arat', 'aluva', 'ernakulam', 'kerala', '683005', 'a', '2022-03-15'),
(2, 'Balu', 'balu@gmail.com', '8596471023', 'balu', '', '', '', '', '', '', '2022-03-15'),
(3, 'Michael', 'michael@gmail.com', '9856023147', 'michael', 'jhb', 'jhbj', 'hjbn', 'jbkb', '658947', '', '2022-03-15'),
(4, 'Xavier', 'xavier@gmail.com', '9652301478', 'xavier', 'Theyambat', 'Perumbavoor', 'Ernakulam', 'Kerala', '684751', 'Thomas', '2022-03-15'),
(5, 'Izin', 'izin@gmail.com', '7485960231', 'izin', 'Dream villa', 'Aluva', 'Ernakulam', 'Kerala', '658941', 'Jasim', '2022-04-12');

-- --------------------------------------------------------

--
-- Table structure for table `custreview`
--

CREATE TABLE IF NOT EXISTS `custreview` (
  `reviewid` int(11) NOT NULL,
  `review` varchar(50) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `cusid` int(11) NOT NULL,
  `date` varchar(50) NOT NULL,
  `vid` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `custreview`
--


-- --------------------------------------------------------

--
-- Table structure for table `expert`
--

CREATE TABLE IF NOT EXISTS `expert` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mob` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `area` varchar(50) NOT NULL,
  `exp` varchar(50) NOT NULL,
  `regDate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `expert`
--

INSERT INTO `expert` (`id`, `name`, `email`, `mob`, `username`, `area`, `exp`, `regDate`) VALUES
(1, 'raju', 'raju@gmail.com', '9947584789', 'raju', '1Year', 'driving', '2022-03-15'),
(2, 'meenu', 'meenu@gmail.com', '9887745698', 'meenu', '1Year', 'driving', '2022-03-15'),
(3, 'Midhun', 'midhun@gmail.com', '741526930', 'midhun', '3Year', 'Distruction', '2022-03-15'),
(4, 'Aswin K', 'aswin@gmail.com', '7489105233', 'aswin', '2Year', 'Fuel technology', '2022-03-15');

-- --------------------------------------------------------

--
-- Table structure for table `expertreview`
--

CREATE TABLE IF NOT EXISTS `expertreview` (
  `reviewid` int(11) NOT NULL AUTO_INCREMENT,
  `review` varchar(50) NOT NULL,
  `rating` varchar(50) NOT NULL,
  `exp_id` int(11) NOT NULL,
  `date` date NOT NULL,
  `vid` int(11) NOT NULL,
  `why_buy` varchar(500) NOT NULL,
  `why_avoid` varchar(500) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`reviewid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `expertreview`
--

INSERT INTO `expertreview` (`reviewid`, `review`, `rating`, `exp_id`, `date`, `vid`, `why_buy`, `why_avoid`, `status`) VALUES
(1, ' All three performance sub-brands are worshipped b', '8', 1, '2022-02-14', 5, 'Daily usability, Strong performance', 'Lacking a few high-end features, In-line six engine lacks aural drama', 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE IF NOT EXISTS `login` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `usertype` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`username`, `password`, `usertype`) VALUES
('admin', 'admin', 'admin'),
('aswin', 'aswin', 'Expert'),
('balu', 'balu', 'Cust'),
('izin', 'izin', 'Cust'),
('meenu', 'meenu', 'Expert'),
('michael', 'michael', 'Cust'),
('midhun', 'midhun', 'Expert'),
('raju', 'raju', 'Expert'),
('ramu', 'ramu123', 'Cust'),
('xavier', 'xavier', 'Cust');

-- --------------------------------------------------------

--
-- Table structure for table `plan`
--

CREATE TABLE IF NOT EXISTS `plan` (
  `planId` int(11) NOT NULL AUTO_INCREMENT,
  `planName` varchar(50) NOT NULL,
  `duration` int(11) NOT NULL,
  `rate` int(11) NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`planId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `plan`
--

INSERT INTO `plan` (`planId`, `planName`, `duration`, `rate`, `status`) VALUES
(1, '3months plan', 3, 1500, '1');

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE IF NOT EXISTS `questions` (
  `qid` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(100) NOT NULL,
  PRIMARY KEY (`qid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`qid`, `question`) VALUES
(1, 'Engine and performance'),
(2, 'Ride and handling'),
(3, 'Interior space and comfort'),
(4, 'Features and equipment');

-- --------------------------------------------------------

--
-- Table structure for table `reviewchild`
--

CREATE TABLE IF NOT EXISTS `reviewchild` (
  `rcid` int(11) NOT NULL AUTO_INCREMENT,
  `reviewid` int(11) NOT NULL,
  `question` varchar(100) NOT NULL,
  `answer` varchar(500) NOT NULL,
  `rating` int(11) NOT NULL,
  PRIMARY KEY (`rcid`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=5 ;

--
-- Dumping data for table `reviewchild`
--

INSERT INTO `reviewchild` (`rcid`, `reviewid`, `question`, `answer`, `rating`) VALUES
(1, 1, 'Engine and performance', 'Basically there’s an integrated starter motor powered by a 48-volt electrical system that makes 21 additional horsepower and more importantly, 250Nm of torque bringing the total output to 429bhp and 520Nm', 5),
(2, 1, 'Ride and handling', 'Controlled, poised and surprisingly sharp. That’s the impression you get after hustling the E53 AMG through some corners. This is mostly down to the clever air suspension and the all-wheel drive system that’s rear biased and if you keep it in Sport+, it turns the E53 into a remarkably involving four-door car to drive', 5),
(3, 1, 'Interior space and comfort', 'If only the E53’s cabin was as impressive as its engine tech or everyday usability. Don’t get me wrong; the build quality is fantastic and there is plenty of room for four adults in here, it’s just that Mercedes should have transformed this interior a bit more or given it more AMG pizzazz.', 5),
(4, 1, 'Features and equipment', 'As standard, the E53 gets twin digital displays that are high on clarity and fluidity, a high-end Burmester surround sound system, adaptive AMG suspension, AMG wheels, a wireless charging pad, ambient lighting, Nappa leather, electric front seats, several airbags, ABS and stability assists. ', 5);

-- --------------------------------------------------------

--
-- Table structure for table `subscription`
--

CREATE TABLE IF NOT EXISTS `subscription` (
  `subId` int(11) NOT NULL AUTO_INCREMENT,
  `planId` int(11) NOT NULL,
  `cusId` int(11) NOT NULL,
  `subDate` date NOT NULL,
  `expDate` date NOT NULL,
  `status` varchar(50) NOT NULL,
  PRIMARY KEY (`subId`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `subscription`
--

INSERT INTO `subscription` (`subId`, `planId`, `cusId`, `subDate`, `expDate`, `status`) VALUES
(1, 1, 5, '2022-04-12', '2022-04-15', 'Active');

-- --------------------------------------------------------

--
-- Table structure for table `vehicle`
--

CREATE TABLE IF NOT EXISTS `vehicle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `cmpid` varchar(50) NOT NULL,
  `model` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `fuel` varchar(50) NOT NULL,
  `torque` varchar(50) NOT NULL,
  `hp` varchar(50) NOT NULL,
  `colors` varchar(50) NOT NULL,
  `price` varchar(50) NOT NULL,
  `groundclearence` varchar(50) NOT NULL,
  `tyrsize` varchar(50) NOT NULL,
  `image` varchar(200) NOT NULL,
  `regDate` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `vehicle`
--

INSERT INTO `vehicle` (`id`, `name`, `cmpid`, `model`, `type`, `fuel`, `torque`, `hp`, `colors`, `price`, `groundclearence`, `tyrsize`, `image`, `regDate`) VALUES
(3, 'swift vxi', '1', '2021', 'huchback', 'petrol', '1.5', '100', 'red,black', '10000', '1.5', '91', 'None', '2022-03-15'),
(4, 'Honda city', '1', 'no', 'hutch', 'petrol', '1.5', '110', 'red', '15000', '1.5', '92', '/media/about_us_2.png', '2022-03-15'),
(5, 'aaa', '2', '2020', 'jn', 'Petrol', '2.5', '110', 'blue', '150000', '1.5', '95', '/media/g4.jpg', '2022-03-15'),
(6, 'Ford Endaeavour', '2', '2022', 'Premium Titanium', 'Petrol', '5.96', '486', 'White, grey, golden,black', '33810000', 'efg', '35.8', '/media/ford-endeavour.jpg', '2022-03-15');
