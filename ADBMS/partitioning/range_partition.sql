USE partitioning;
CREATE TABLE account_info_range_partitioned (
    ID INT,
    Name VARCHAR(50),
    Age INT,
    Email VARCHAR(100)
);
INSERT INTO account_info_range_partitioned (ID, Name, Age, Email) VALUES
(1, 'John Doe', 30, 'johndoe@email.com'),
(2, 'Jane Smith', 25, 'janesmith@email.com'),
(3, 'Michael Johnson', 35, 'michaeljohnson@email.com'),
(4, 'Emily Williams', 28, 'emilywilliams@email.com'),
(5, 'William Brown', 32, 'williambrown@email.com'),
(6, 'Emma Jones', 29, 'emmajones@email.com'),
(7, 'Matthew Davis', 31, 'matthewdavis@email.com'),
(8, 'Olivia Miller', 26, 'oliviamiller@email.com'),
(9, 'Christopher Wilson', 33, 'christopherwilson@email.com'),
(10, 'Ava Garcia', 27, 'avagarcia@email.com'),
(11, 'David Rodriguez', 34, 'davidrodriguez@email.com'),
(12, 'Sophia Martinez', 30, 'sophiamartinez@email.com'),
(13, 'James Anderson', 29, 'jamesanderson@email.com'),
(14, 'Isabella Taylor', 31, 'isabellataylor@email.com'),
(15, 'Joseph Thomas', 28, 'josephthomas@email.com'),
(16, 'Mia Hernandez', 32, 'miahernandez@email.com'),
(17, 'Daniel Moore', 25, 'danielmoore@email.com'),
(18, 'Charlotte Martin', 33, 'charlottemartin@email.com'),
(19, 'Benjamin Jackson', 26, 'benjaminjackson@email.com'),
(20, 'Amelia White', 34, 'ameliawhite@email.com');
ALTER TABLE account_info_range_partitioned PARTITION BY RANGE (AGE)(
    PARTITION p0 VALUES LESS THAN (20),
    PARTITION p1 VALUES LESS THAN (25),
    PARTITION p2 VALUES LESS THAN (30),
    PARTITION p3 VALUES LESS THAN MAXVALUE
);
SELECT * FROM account_info_range_partitioned PARTITION(p2);
