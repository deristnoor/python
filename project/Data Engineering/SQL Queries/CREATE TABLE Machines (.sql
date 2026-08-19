CREATE TABLE Machines (
    MachineID INT PRIMARY KEY,
    MachineName VARCHAR(100) NOT NULL,
    Location VARCHAR(100),
    Status VARCHAR(50),
    LastMaintenanceDate DATE
);

CREATE TABLE Production (
    ProductionID INT PRIMARY KEY,
    MachineID INT,
    ProductName VARCHAR(100) NOT NULL,
    QuantityProduced INT,
    ProductionDate DATE,
    RejectedQuantity INT,
    FOREIGN KEY (MachineID) REFERENCES Machines(MachineID)
);

CREATE TABLE Downtime (
    DowntimeID INT IDENTITY(1,1) PRIMARY KEY,
    MachineID INT,
    StartTime DATETIME,
    EndTime DATETIME,
    Reason VARCHAR(255),
    FOREIGN KEY (MachineID) REFERENCES Machines(MachineID)
);