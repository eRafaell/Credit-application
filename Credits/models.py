from typing import List
import pyodbc


class Models:

    def read_sql(self, query):
        cnxn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-3TBC445;'
                              'Database=Credits;'
                              'Trusted_Connection=yes;')
        cursor = cnxn.cursor()
        cursor.execute(query)
        return list(cursor.fetchall())

    def create_sql_model(self):
        cnxn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-3TBC445;'
                              'Database=Credits;'
                              'Trusted_Connection=yes;')
        return cnxn

    def create_sql_client(self, li: List):
        cnxn = self.create_sql_model()
        cursor = cnxn.cursor()
        query = self.add_client_to_database()
        values = (li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7])
        cursor.execute(query, values)
        cnxn.commit()

    def add_client_to_database(self):
        adding = f"INSERT INTO Client (IdClient, FirstName, LastName, City, Street, Sex, MaritalStatus, PESEL) " \
            f"VALUES (?,?,?,?,?,?,?,?)"
        return adding

    def create_sql_income(self, li: List):
        cnxn = self.create_sql_model()
        cursor = cnxn.cursor()
        query = self.add_income_to_database()
        values = (li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7], li[8])
        cursor.execute(query, values)
        cnxn.commit()

    def add_income_to_database(self):
        adding = f"INSERT INTO Income (IdIncome, Employer, EmploymentCity, EmploymentStreet, NIP, EmploymentType, " \
            f"NetSalary, SpouseSalary, ClientId) VALUES (?,?,?,?,?,?,?,?,?)"
        return adding

    def create_sql_expenses(self, li: List):
        cnxn = self.create_sql_model()
        cursor = cnxn.cursor()
        query = self.add_expenses_to_database()
        values = (li[0], li[1], li[2], li[3])
        cursor.execute(query, values)
        cnxn.commit()

    def add_expenses_to_database(self):
        adding = f"INSERT INTO Expenses (IdExpenses, AllMonthlyCredits, AllMonthlyBills, ClientId) VALUES (?,?,?,?)"
        return adding

    def create_sql_loan(self, li: List):
        cnxn = self.create_sql_model()
        cursor = cnxn.cursor()
        query = self.add_loan_to_database()
        values = (li[0], li[1], li[2], li[3], li[4], li[5], li[6], li[7])
        cursor.execute(query, values)
        cnxn.commit()

    def add_loan_to_database(self):
        adding = f"INSERT INTO Loan (IdLoan, BorrowAmount, InstallmentsNumber, InterestRate, ClientId, " \
            f"MonthlyInstallment, TotalAmountToGiveBack, Status) VALUES (?,?,?,?,?,?,?,?)"
        return adding

    def check_pesel(self, pesel: str):
        if len(pesel) == 11:
            sex = int(pesel[9])
            # 9×a + 7×b + 3×c + 1×d + 9×e + 7×f + 3×g + 1×h + 9×i + 7×j
            check = 9 * int(pesel[0]) + 7 * int(pesel[1]) + 3 * int(pesel[2]) + 1 * int(pesel[3]) + 9 * int(pesel[4]) \
                    + 7 * int(pesel[5]) + 3 * int(pesel[6]) + 1 * int(pesel[7]) + 9 * int(pesel[8]) + 7 * int(pesel[9])
            check = check % 10
            if check == int(pesel[10]):
                if sex % 2 == 0:
                    print(f'The owner of PESEL number: {pesel} is a woman!')
                else:
                    print(f'The owner of PESEL number: {pesel} is a man!')
                return True
            return False
        return False

    def check_nip(self, nip: str):
        if len(nip) == 10:
            control_number = nip[9]
            rest_numbers = int(nip[0]) * 6 + int(nip[1]) * 5 + int(nip[2]) * 7 + int(nip[3]) * 2 + int(
                nip[4]) * 3 + int(nip[5]) * 4 + int(nip[6]) * 5 + int(nip[7]) * 6 + int(nip[8]) * 7
            modulo_number = rest_numbers % 11
            if int(modulo_number) == int(control_number):
                return True
            return False
        return False
