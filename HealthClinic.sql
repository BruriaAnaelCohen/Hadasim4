CREATE DATABASE HealthClinic --All rights reserved to Bruria Anael Cohen 0548593276

USE HealthClinic
create table City(
	cityCode INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
	cityName varchar(20) NOT NULL
);

create table VaccinationType(
	vaccinationTCode int identity(1,1) NOT NULL PRIMARY KEY,
	vaccinationName varchar(20) NOT NULL
);

create table PAddress(
	addressCode int identity(1,1)  NOT NULL PRIMARY KEY,
	cityCode int NOT NULL,
	street varchar(20),
	addressNum int,
	apartNum int,
	FOREIGN KEY (cityCode) REFERENCES City(cityCode)
);

create table Patient ( 
	patientCode INT IDENTITY(1,1) NOT NULL PRIMARY KEY,
    patientID VARCHAR(9) NOT NULL,
	patientFName VARCHAR(20) NOT NULL,
	patientLName VARCHAR(20) NOT NULL,
	phone varchar(10)  NOT NULL,
	email varchar(255),
	birthDate date NOT NULL, 
	addressCode int,
	img varchar(255),
	stts bit NOT NULL,
	FOREIGN KEY (addressCode) REFERENCES PAddress(addressCode)
);

create table Vaccination(
	vaccinationCode int identity(1,1)  NOT NULL PRIMARY KEY,
	patientCode int NOT NULL,
	vaccinationTCode int NOT NULL, 
	vaccDate date NOT NULL,
	stts bit NOT NULL,
	FOREIGN KEY (patientCode) REFERENCES Patient(patientCode),
	FOREIGN KEY (vaccinationTCode) REFERENCES VaccinationType(vaccinationTCode)
);

create table SicknessPeriod(
	sPeriodCode int identity(1,1)  NOT NULL PRIMARY KEY,
	patientCode int NOT NULL,
	infectionDate date NOT NULL,
	recoveryDate date NOT NULL,
	stts bit NOT NULL,
	FOREIGN KEY (patientCode) REFERENCES Patient(patientCode),
);

INSERT INTO City (cityName) VALUES 
('Rechovot'),
('Tel-Aviv'),
('Jerusalem');

INSERT INTO VaccinationType (vaccinationName) VALUES 
('Pfizer'),
('Modern'),
('AstraZeneca'),
('Novavax');

INSERT INTO PAddress(cityCode,street,addressNum,apartNum) VALUES
(1, 'Bne Moshe',16,9),
(2,'Ezra',20,3),
(3,'Nachmani',5,5),
(1,'Hahagana',1,1);

INSERT INTO Patient (patientID, patientFName, patientLName,phone,email, birthDate, addressCode,img, stts) VALUES 
('123456789', 'Orna', 'Tuvia','0524423687', 'ornaco2@gmail.com','1990-05-15', 1,'', 1),
('987654321', 'Michal', 'Aviel', '0099887765','o@gmail.com','1985-10-20', 2, '',0),
('456123789', 'Tom', 'Johnson','0546576687','ornaco2@gmail.com' ,'1978-03-08', 3,'', 1),
('327550679','Bruria Anael', 'Cohen','0548593276','bruriaac@gmail.com','2004-11-13',4,'',1);

INSERT INTO Vaccination (patientCode, vaccinationTCode, vaccDate,stts) VALUES 
(1, 1, '2023-01-15',1),
(2, 2, '2023-02-20',0),
(1, 3, '2023-03-25',1);

INSERT INTO SicknessPeriod (patientCode, infectionDate, recoveryDate,stts) VALUES 
( 1,'2022-12-01', '2023-01-01',1),
( 2, '2022-11-10', '2022-12-10',0);

