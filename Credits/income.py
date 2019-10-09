from Credits.models import Models
from Credits.client import Client
import sys


class Income:
    def __init__(self):
        self.income = Models()
        self.client = Client()

    def add_income(self):
        income_list = []
        id = self.get_id_income()
        income_list.append(id)
        employer = input("Please, enter a Employer name: ")
        if len(employer) <= 50:
            income_list.append(employer.capitalize())
        else:
            print("Employer name is too long. We cannot continue")
            sys.exit(0)
        employment_city = input("Please, enter a Employment city: ")
        if len(employment_city) <= 50:
            income_list.append(employment_city.capitalize())
        else:
            print("Employment city name is too long. We cannot continue")
            sys.exit(0)
        employment_street = input("Please, enter a Employment street: ")
        if len(employment_street) <= 50:
            income_list.append(employment_street.capitalize())
        else:
            print("Employment street name is too long. We cannot continue")
            sys.exit(0)
        nip = input("Please, enter a NIP of the Employer: ")
        if self.income.check_nip(nip) == True:
            print("NIP is correct")
            income_list.append(nip)
        else:
            print("NIP is incorrect")
            sys.exit(0)
        employment_type = input("Please, enter a Employment type: ")
        if len(employment_type) <= 50:
            income_list.append(employment_type.capitalize())
        else:
            print("Employment type name is too long. We cannot continue")
            sys.exit(0)
        net_salary = float(input("Please, enter the net salary: "))
        income_list.append(round(net_salary, 2))
        spouse_net_salary = float(input("Please, enter your spouse net salary (if the client does not have a spouse. Enter 0): "))
        income_list.append(round(spouse_net_salary, 2))
        clientid = self.client.get_id_client()
        income_list.append(clientid)
        return income_list

    def get_id_income(self):
        query = "select max(IdIncome) from Income"
        idincome = self.income.read_sql(query)
        if len(idincome) > 0:
            idincome = str(idincome).strip('[(,)]')
            idincome = int(idincome.replace(",", "")) + 1
            return idincome
        else:
            return 1
