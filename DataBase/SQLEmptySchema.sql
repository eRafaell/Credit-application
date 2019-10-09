USE [Credits]
GO
/****** Object:  Table [dbo].[BlackList]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[BlackList](
	[IdBlackList] [int] IDENTITY(1,1) NOT NULL,
	[Reason] [varchar](50) NOT NULL,
	[ClientId] [int] NOT NULL,
 CONSTRAINT [PK_BlackList] PRIMARY KEY CLUSTERED 
(
	[IdBlackList] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Client]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Client](
	[IdClient] [int] NOT NULL,
	[FirstName] [varchar](50) NOT NULL,
	[LastName] [varchar](50) NOT NULL,
	[City] [varchar](20) NOT NULL,
	[Street] [varchar](30) NOT NULL,
	[Sex] [varchar](1) NOT NULL,
	[MaritalStatus] [varchar](20) NOT NULL,
	[PESEL] [varchar](11) NOT NULL,
 CONSTRAINT [PK_Client] PRIMARY KEY CLUSTERED 
(
	[IdClient] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Expenses]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Expenses](
	[IdExpenses] [int] NOT NULL,
	[AllMonthlyCredits] [int] NOT NULL,
	[AllMonthlyBills] [int] NOT NULL,
	[ClientId] [int] NOT NULL,
 CONSTRAINT [PK_Expenses] PRIMARY KEY CLUSTERED 
(
	[IdExpenses] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Income]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Income](
	[IdIncome] [int] NOT NULL,
	[Employer] [varchar](50) NULL,
	[EmploymentCity] [varchar](50) NULL,
	[EmploymentStreet] [varchar](50) NULL,
	[NIP] [varchar](12) NULL,
	[EmploymentType] [varchar](50) NULL,
	[NetSalary] [float] NOT NULL,
	[SpouseSalary] [float] NOT NULL,
	[ClientId] [int] NOT NULL,
 CONSTRAINT [PK_Income] PRIMARY KEY CLUSTERED 
(
	[IdIncome] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Loan]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Loan](
	[IdLoan] [int] NOT NULL,
	[BorrowAmount] [int] NOT NULL,
	[InstallmentsNumber] [smallint] NOT NULL,
	[InterestRate] [float] NOT NULL,
	[ClientId] [int] NOT NULL,
	[MonthlyInstallment] [float] NOT NULL,
	[TotalAmountToGiveBack] [float] NOT NULL,
	[Status] [varchar](20) NULL,
 CONSTRAINT [PK_Loan] PRIMARY KEY CLUSTERED 
(
	[IdLoan] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[BlackList]  WITH CHECK ADD  CONSTRAINT [FK_BlackList_Client] FOREIGN KEY([ClientId])
REFERENCES [dbo].[Client] ([IdClient])
GO
ALTER TABLE [dbo].[BlackList] CHECK CONSTRAINT [FK_BlackList_Client]
GO
ALTER TABLE [dbo].[Expenses]  WITH CHECK ADD  CONSTRAINT [FK_Expenses_CLient] FOREIGN KEY([ClientId])
REFERENCES [dbo].[Client] ([IdClient])
GO
ALTER TABLE [dbo].[Expenses] CHECK CONSTRAINT [FK_Expenses_CLient]
GO
ALTER TABLE [dbo].[Income]  WITH NOCHECK ADD  CONSTRAINT [FK_Income_Client] FOREIGN KEY([ClientId])
REFERENCES [dbo].[Client] ([IdClient])
GO
ALTER TABLE [dbo].[Income] CHECK CONSTRAINT [FK_Income_Client]
GO
/****** Object:  StoredProcedure [dbo].[AddClient]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[AddClient] (@FirstName varchar(50), @LastName varchar(50), @City varchar(20), @Street varchar(30), @Sex varchar(1), @MartialStatus varchar(20), @PESEL varchar(11))

AS
BEGIN

	set @Street = (select trim(replace(@street,'ul.','')))
	if @PESEL in (select PESEL from Client)
		print 'Client is already exist'

	else if @Sex != upper('M') and @Sex != upper('W')
		print 'Sex can be only man - "M" or woman - "W"'

	else
		insert into Client values (@FirstName, @LastName, @City, @Street, @Sex, @MartialStatus, @PESEL)
		
END
GO
/****** Object:  StoredProcedure [dbo].[AddExpenses]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

Create PROCEDURE [dbo].[AddExpenses] (@AllMonthlyCredits int, @AllMonthlyBills int, @ClientId int)

AS
BEGIN

		insert into Expenses values (@AllMonthlyCredits, @AllMonthlyBills, @ClientId)
		
END
GO
/****** Object:  StoredProcedure [dbo].[AddIncome]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[AddIncome] (@Employer varchar(50), @EmploymentCity varchar(20), @EmploymentStreet varchar(30), @NIP varchar(10), @EmploymentType varchar(30), @NetSalary float, @SpouseSalary float, @ClientId int)

AS
BEGIN
	set @EmploymentStreet = (select trim(replace(@EmploymentStreet,'ul.','')))
	if len(@NIP) != 10 
		print 'Wrong NIP. NIP number must have 10 digits'
	else
		insert into Income values (@Employer, @EmploymentCity, @EmploymentStreet, @NIP, @EmploymentType, round(@NetSalary,2), round(@SpouseSalary,2), @ClientId)
END
GO
/****** Object:  StoredProcedure [dbo].[AddLoan]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[AddLoan] (@BorrowAmount int, @InstallmentsNumber smallint, @InterestRate float(4), @ClientId int)

AS
BEGIN
	declare @MonthlyInstallment float(4)
	declare @Number int
	declare @TotalAmountToGiveBack float(4)
	declare @Status varchar(20)
	declare @AllExpenses int
	declare @AllCredits int
	declare @AllBills int

	set @MonthlyInstallment = (@BorrowAmount*(1+@InterestRate/100)/@InstallmentsNumber)
	set @Number = (select NetSalary from income where ClientId=@ClientId) + (select SpouseSalary from income where ClientId=@ClientId)
	set @AllCredits = (select AllMonthlyCredits from Expenses where ClientId=@ClientId)
	set @AllBills = (select AllMonthlyBills from Expenses where ClientId=@ClientId)
	set @AllExpenses = @AllCredits + @AllBills + @MonthlyInstallment
	
	set @TotalAmountToGiveBack = @MonthlyInstallment * @InstallmentsNumber
	
	if @Number * 0.7 > @AllExpenses
		set @Status = 'Granted'
		
	else
		set @Status = 'Rejected'
	
	
	insert into Loan values (@BorrowAmount, @InstallmentsNumber, round(@InterestRate,2), @ClientId, round(@MonthlyInstallment,2), round(@TotalAmountToGiveBack,2), @Status)
		
END
GO
/****** Object:  StoredProcedure [dbo].[AddToBlackList]    Script Date: 09.10.2019 21:05:55 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

CREATE PROCEDURE [dbo].[AddToBlackList] (@Reason varchar(50), @ClientId int)

AS
BEGIN


	if @ClientId in (select ClientId from BlackList)
		print 'The client has already been blacklisted!'

	else
		insert into BlackList values (@Reason, @ClientId)
		
END
GO
