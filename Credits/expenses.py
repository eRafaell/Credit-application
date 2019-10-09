from Credits.models import Models
from Credits.client import Client

class Expenses:
    def __init__(self):
        self.expenses = Models()
        self.client = Client()


    def get_id_expenses(self):
        query = "select max(IdExpenses) from Expenses"
        idexpenses = self.expenses.read_sql(query)
        if len(idexpenses) > 0:
            idexpenses = str(idexpenses).strip('[(,)]')
            idexpenses = int(idexpenses.replace(",", "")) + 1
            return idexpenses
        else:
            return 1

    def add_expenses(self):
        expenses_list = []
        id = self.get_id_expenses()
        expenses_list.append(id)
        all_monthly_credits = int(input("Please, enter all monthly credits: "))
        expenses_list.append(all_monthly_credits)
        all_monthly_bills = int(input("Please, enter all monthly bills, such as a rent, an electricity fee and so on: "))
        expenses_list.append(all_monthly_bills)
        clientid = self.client.get_id_client()
        expenses_list.append(clientid)
        return expenses_list
