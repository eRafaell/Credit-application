USE [Credits]
GO
INSERT [dbo].[Client] ([IdClient], [FirstName], [LastName], [City], [Street], [Sex], [MaritalStatus], [PESEL]) VALUES (1, N'Jan', N'Kowalski', N'Poznań', N'Wielka 4/12', N'M', N'Bachelor', N'90090515836')
GO
INSERT [dbo].[Client] ([IdClient], [FirstName], [LastName], [City], [Street], [Sex], [MaritalStatus], [PESEL]) VALUES (2, N'Barbara', N'Wiśniewska', N'Szczecin', N'Toruńska 2a/34', N'W', N'Maried', N'80072909146')
GO
INSERT [dbo].[Client] ([IdClient], [FirstName], [LastName], [City], [Street], [Sex], [MaritalStatus], [PESEL]) VALUES (3, N'Anna', N'Stefaniak', N'Gdańsk', N'Brzozowa 141', N'W', N'Divorcee', N'65071209862')
GO
INSERT [dbo].[Client] ([IdClient], [FirstName], [LastName], [City], [Street], [Sex], [MaritalStatus], [PESEL]) VALUES (4, N'Bogusław', N'Wolny', N'Kraków', N'Spacerowa 5/21', N'M', N'Widower', N'67040500538')
GO
INSERT [dbo].[Client] ([IdClient], [FirstName], [LastName], [City], [Street], [Sex], [MaritalStatus], [PESEL]) VALUES (5, N'Piotr', N'Nowak', N'Warszawa', N'Dąbrowskiej 7', N'M', N'Bachelor', N'81100216357')
GO
INSERT [dbo].[Client] ([IdClient], [FirstName], [LastName], [City], [Street], [Sex], [MaritalStatus], [PESEL]) VALUES (6, N'Maria', N'Kaczmarek', N'Poznań', N'Hetmańska 56/22', N'W', N'Bachelor', N'92071314764')
GO
INSERT [dbo].[Client] ([IdClient], [FirstName], [LastName], [City], [Street], [Sex], [MaritalStatus], [PESEL]) VALUES (7, N'Stefan', N'Mikołajczak', N'Suwałki', N'Polna 17a/37', N'M', N'Maried', N'76012227612')
GO
SET IDENTITY_INSERT [dbo].[BlackList] ON 
GO
INSERT [dbo].[BlackList] ([IdBlackList], [Reason], [ClientId]) VALUES (1, N'Attempt to cheat and extort money', 5)
GO
SET IDENTITY_INSERT [dbo].[BlackList] OFF
GO
INSERT [dbo].[Income] ([IdIncome], [Employer], [EmploymentCity], [EmploymentStreet], [NIP], [EmploymentType], [NetSalary], [SpouseSalary], [ClientId]) VALUES (19, N'Zebra Poznań Sp. z o.o.', N'Poznań', N'Krakowska 4', N'7822052334', N'Employment contract', 2900, 0, 1)
GO
INSERT [dbo].[Income] ([IdIncome], [Employer], [EmploymentCity], [EmploymentStreet], [NIP], [EmploymentType], [NetSalary], [SpouseSalary], [ClientId]) VALUES (20, N'Elephant S.A.', N'Police', N'Polna 1', N'8510205573', N'Fixed-term contract', 2500, 3500, 2)
GO
INSERT [dbo].[Income] ([IdIncome], [Employer], [EmploymentCity], [EmploymentStreet], [NIP], [EmploymentType], [NetSalary], [SpouseSalary], [ClientId]) VALUES (21, N'Horse Firma Budowlana Sp. z o.o.', N'Gdańsk', N'Horta 44', N'5842764982', N'Employment contract', 3000, 0, 3)
GO
INSERT [dbo].[Income] ([IdIncome], [Employer], [EmploymentCity], [EmploymentStreet], [NIP], [EmploymentType], [NetSalary], [SpouseSalary], [ClientId]) VALUES (22, N'Scorpion Sp. z o.o.', N'Kraków', N'Łowińska 100', N'6780034235', N'Civil contract', 4000, 0, 4)
GO
INSERT [dbo].[Income] ([IdIncome], [Employer], [EmploymentCity], [EmploymentStreet], [NIP], [EmploymentType], [NetSalary], [SpouseSalary], [ClientId]) VALUES (23, N'Raccoon Sp. z o.o.', N'Warszawa', N'Włoska 111', N'5251347382', N'Civil contract', 2600, 0, 5)
GO
INSERT [dbo].[Income] ([IdIncome], [Employer], [EmploymentCity], [EmploymentStreet], [NIP], [EmploymentType], [NetSalary], [SpouseSalary], [ClientId]) VALUES (24, N'Jellyfish Sp. z o.o.', N'Poznań', N'Św. Pawła 41', N'7851732729', N'Employment contract', 6100, 0, 6)
GO
INSERT [dbo].[Income] ([IdIncome], [Employer], [EmploymentCity], [EmploymentStreet], [NIP], [EmploymentType], [NetSalary], [SpouseSalary], [ClientId]) VALUES (26, N'Cameleon S.A.', N'Suwałki', N'Teatralna 10', N'8440004058', N'Employment contract', 2250, 5125, 7)
GO
INSERT [dbo].[Expenses] ([IdExpenses], [AllMonthlyCredits], [AllMonthlyBills], [ClientId]) VALUES (1, 1000, 700, 5)
GO
INSERT [dbo].[Expenses] ([IdExpenses], [AllMonthlyCredits], [AllMonthlyBills], [ClientId]) VALUES (2, 0, 800, 1)
GO
INSERT [dbo].[Expenses] ([IdExpenses], [AllMonthlyCredits], [AllMonthlyBills], [ClientId]) VALUES (3, 500, 500, 2)
GO
INSERT [dbo].[Expenses] ([IdExpenses], [AllMonthlyCredits], [AllMonthlyBills], [ClientId]) VALUES (4, 0, 900, 3)
GO
INSERT [dbo].[Expenses] ([IdExpenses], [AllMonthlyCredits], [AllMonthlyBills], [ClientId]) VALUES (5, 250, 1000, 4)
GO
INSERT [dbo].[Expenses] ([IdExpenses], [AllMonthlyCredits], [AllMonthlyBills], [ClientId]) VALUES (6, 120, 1100, 6)
GO
INSERT [dbo].[Expenses] ([IdExpenses], [AllMonthlyCredits], [AllMonthlyBills], [ClientId]) VALUES (7, 1900, 750, 7)
GO
INSERT [dbo].[Loan] ([IdLoan], [BorrowAmount], [InstallmentsNumber], [InterestRate], [ClientId], [MonthlyInstallment], [TotalAmountToGiveBack], [Status]) VALUES (41, 10000, 5, 2.1, 1, 2042, 10210, N'Rejected')
GO
INSERT [dbo].[Loan] ([IdLoan], [BorrowAmount], [InstallmentsNumber], [InterestRate], [ClientId], [MonthlyInstallment], [TotalAmountToGiveBack], [Status]) VALUES (42, 2000, 8, 2.25, 2, 255.63, 2045, N'Granted')
GO
INSERT [dbo].[Loan] ([IdLoan], [BorrowAmount], [InstallmentsNumber], [InterestRate], [ClientId], [MonthlyInstallment], [TotalAmountToGiveBack], [Status]) VALUES (44, 6250, 10, 2.5, 3, 640.63, 6406.25, N'Granted')
GO
INSERT [dbo].[Loan] ([IdLoan], [BorrowAmount], [InstallmentsNumber], [InterestRate], [ClientId], [MonthlyInstallment], [TotalAmountToGiveBack], [Status]) VALUES (45, 3220, 6, 2.88, 4, 552.12, 3312.74, N'Granted')
GO
INSERT [dbo].[Loan] ([IdLoan], [BorrowAmount], [InstallmentsNumber], [InterestRate], [ClientId], [MonthlyInstallment], [TotalAmountToGiveBack], [Status]) VALUES (46, 8020, 6, 2.88, 5, 1375.16, 8250.98, N'Rejected')
GO
INSERT [dbo].[Loan] ([IdLoan], [BorrowAmount], [InstallmentsNumber], [InterestRate], [ClientId], [MonthlyInstallment], [TotalAmountToGiveBack], [Status]) VALUES (47, 2999, 10, 1.99, 6, 305.87, 3058.68, N'Granted')
GO
INSERT [dbo].[Loan] ([IdLoan], [BorrowAmount], [InstallmentsNumber], [InterestRate], [ClientId], [MonthlyInstallment], [TotalAmountToGiveBack], [Status]) VALUES (48, 4299, 20, 2.5, 7, 220.32, 4406.48, N'Granted')
GO
