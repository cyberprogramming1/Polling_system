-- Create a new database
CREATE DATABASE PollingSystem_New;


-- Create a table for poll questions
CREATE TABLE Polls (
    PollID INT PRIMARY KEY IDENTITY(1,1),
    Question NVARCHAR(255) NOT NULL
);

CREATE TABLE Users (
    UserID INT PRIMARY KEY IDENTITY(1,1),
    Username NVARCHAR(50) UNIQUE NOT NULL,
    Password NVARCHAR(100) NOT NULL
);

-- Create a table for poll options
CREATE TABLE PollOptions (
    OptionID INT PRIMARY KEY IDENTITY(1,1),
    PollID INT,
    OptionText NVARCHAR(255) NOT NULL,
    Votes INT DEFAULT 0,
    FOREIGN KEY (PollID) REFERENCES Polls(PollID)

);

CREATE TABLE UserVotes (
    VoteID INT PRIMARY KEY IDENTITY(1,1),
    PollID INT,
    OptionID INT,
    UserID INT,
    FOREIGN KEY (PollID) REFERENCES Polls(PollID),
    FOREIGN KEY (OptionID) REFERENCES PollOptions(OptionID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);


select * from Polls;
select * from PollOptions;
select * from Users;
select * from UserVotes;

delete Polls;
delete PollOptions;
delete Users;
delete UserVotes






DBCC CHECKIDENT ('Polls', RESEED, 0);
DBCC CHECKIDENT ('PollOptions', RESEED, 0);
DBCC CHECKIDENT ('UserVotes', RESEED, 0);
DBCC CHECKIDENT ('Users', RESEED, 0);

select @@SERVERNAME
