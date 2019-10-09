import sys
from typing import List

from Credits.models import Models
from Credits.client import Client


class Loan:
    def __init__(self):
        self.loan = Models()
        self.client = Client()

    def add_loan(self, liexpenses: List, liincome: List):
        loan_list = []
        id = self.get_id_loan()
        loan_list.append(id)
        borrow_amount = int(input("Please, enter amount to borrow: "))
        loan_list.append(borrow_amount)
        installments_number = int(input("Please, enter number of installments [max. 60]: "))
        if installments_number <= 60:
            loan_list.append(installments_number)
        else:
            answer = input("Maximum number of installments is 60. Please click 'r' if you want to decrease number "
                           "of installments or any other button to quit the application: ")
            if answer.lower() == "r":
                return self.add_loan(liexpenses, liincome)
            else:
                sys.exit(0)
        interest_rate = float(input("Please, enter the interest rate according to bank offer: "))
        loan_list.append(round(interest_rate, 2))
        clientid = self.client.get_id_client()
        loan_list.append(clientid)
        monthly_installment = (borrow_amount * (1 + interest_rate / 100) / installments_number)
        loan_list.append(round(monthly_installment, 2))
        total_amount_to_give_back = monthly_installment * installments_number
        loan_list.append(round(total_amount_to_give_back, 2))
        all_expenses = liexpenses[1] + liexpenses[2] + monthly_installment
        all_income = liincome[6] + liincome[7]
        if all_income * 0.7 > all_expenses:
            status = "Granted"
        else:
            status = "Rejected"
        loan_list.append(status)
        return loan_list

    def get_id_loan(self):
        query = "select max(IdLoan) from Loan"
        idloan = self.loan.read_sql(query)
        if len(idloan) > 0:
            idloan = str(idloan).strip('[(,)]')
            idloan = int(idloan.replace(",", "")) + 1
            return idloan
        else:
            return 1

    def show_history(self):
        query = f"select c.FirstName, c.LastName, l.IdLoan from client c left join loan l on c.IdClient = l.ClientId"
        return self.loan.read_sql(query)

    def show_personal_data(self, id_number: int):
        query = f"select c.FirstName, c.LastName, c.City, c.Street, c.Sex, c.MaritalStatus, c.Pesel from client " \
            f"c left join loan l on c.IdClient = l.ClientId where IdLoan = {id_number};"
        return self.loan.read_sql(query)

    def show_loan_data(self, id_number: int):
        query = f"select l.IdLoan, l.BorrowAmount, l.InstallmentsNumber, l.InterestRate, l.MonthlyInstallment, " \
            f"l.TotalAmountToGiveBack, l.Status from client c left join loan l " \
            f"on c.IdClient = l.ClientId where IdLoan = {id_number};"
        return self.loan.read_sql(query)

    def show_income(self, id_number: int):
        query = f"select i.Employer, i.EmploymentStreet, i.NIP, i.EmploymentType, i.NetSalary, i.SpouseSalary " \
            f"from client c left join loan l on c.IdClient = l.ClientId join income i on c.IdClient = i.ClientId " \
            f"where IdLoan = {id_number};"
        return self.loan.read_sql(query)

    def show_expenses(self, id_number: int):
        query = f"select e.AllMonthlyCredits, e.AllMonthlyBills from client c " \
            f"left join loan l on c.IdClient = l.ClientId join expenses e on c.IdClient = e.ClientId " \
            f"where IdLoan = {id_number};"
        return self.loan.read_sql(query)
